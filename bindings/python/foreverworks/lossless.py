"""Optional exact-decimal JSON interchange; no arithmetic or Decimal context rounding."""
import copy
from dataclasses import dataclass
from decimal import Decimal
import json
import math
import re
NUMBER=re.compile(r'-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\Z')
@dataclass(frozen=True)
class JsonNumber:
    token: str
    def __post_init__(self):
        if not isinstance(self.token,str) or not NUMBER.fullmatch(self.token): raise ValueError('invalid-number')
        if len(self.token)>4096: raise ValueError('resource-limit: numeric token exceeds 4096 bytes')
        raw=re.split('[eE]',self.token)[1] if re.search('[eE]',self.token) else '0'
        digits=raw.lstrip('+-').lstrip('0')
        if len(digits)>7 or abs(int(raw))>1000000: raise ValueError('resource-limit: exponent magnitude exceeds 1000000')
        d=Decimal(self.token);coefficient=list(d.as_tuple().digits)
        while len(coefficient)>1 and coefficient[-1]==0:coefficient.pop()
        if len(coefficient)>4000 or (d and abs(d.adjusted())>1000000):raise ValueError('resource-limit: decimal precision or adjusted exponent')
    @property
    def decimal(self): return Decimal(self.token)
    def canonical(self):
        sign,digits,exponent=self.decimal.as_tuple()
        digits=list(digits)
        if not any(digits): return '0'
        while digits[-1]==0: digits.pop();exponent+=1
        coefficient=''.join(map(str,digits));adjusted=len(digits)+exponent-1
        if -6<=adjusted<=20:
            point=len(digits)+exponent
            if point<=0: text='0.'+'0'*(-point)+coefficient
            elif point>=len(digits): text=coefficient+'0'*(point-len(digits))
            else: text=coefficient[:point]+'.'+coefficient[point:]
        else: text=coefficient[0]+('.'+coefficient[1:] if len(digits)>1 else '')+'e'+str(adjusted)
        return ('-' if sign else '')+text

def canonical_lossless(value):
    def emit(v,depth=0):
        if depth>64: raise ValueError('resource-limit: nesting exceeds 64')
        if isinstance(v,JsonNumber): return v.canonical()
        if v is None: return 'null'
        if isinstance(v,bool): return 'true' if v else 'false'
        if type(v) is int:
            if abs(v)>9007199254740991: raise ValueError('unsafe-host-number: supply an explicit JsonNumber token')
            return str(v)
        if type(v) is float: raise ValueError('unsafe-host-number: supply an explicit JsonNumber token')
        if isinstance(v,str): v.encode('utf-8');return json.dumps(v,ensure_ascii=False)
        if not isinstance(v,(list,dict)): raise ValueError('invalid-json-value')
        if not v:return '{}' if isinstance(v,dict) else '[]'
        keys=sorted(v) if isinstance(v,dict) else range(len(v))
        items=['  '*(depth+1)+(emit(k,depth+1)+': ' if isinstance(v,dict) else '')+emit(v[k],depth+1) for k in keys]
        return ('{' if isinstance(v,dict) else '[')+'\n'+',\n'.join(items)+'\n'+'  '*depth+('}' if isinstance(v,dict) else ']')
    return emit(value)+'\n'

class LosslessDocument:
    def __init__(self,text,value): self.__text=text;self.__value=value
    @property
    def value(self): return copy.deepcopy(self.__value)
    def source(self): return self.__text
    def canonical(self): return canonical_lossless(self.__value)
    def to_host(self,allow_loss=False):
        def project(v):
            if isinstance(v,JsonNumber):
                number=float(v.token)
                if not math.isfinite(number): raise ValueError('unsupported-host-number')
                if not allow_loss and Decimal(str(number))!=v.decimal: raise ValueError('lossy-number-projection')
                return int(number) if number.is_integer() and abs(number)<=9007199254740991 else number
            if isinstance(v,list):return [project(x) for x in v]
            if isinstance(v,dict):return {k:project(x) for k,x in v.items()}
            return v
        return project(self.__value)

def parse_lossless(data):
    raw=data.encode('utf-8') if isinstance(data,str) else data
    if not isinstance(raw,bytes): raise TypeError('expected UTF-8 text or bytes')
    if len(raw)>1048576: raise ValueError('resource-limit: document bytes')
    text=raw.decode('utf-8')
    def pairs(items):
        out={}
        for key,value in items:
            if key in out:raise ValueError('duplicate-member')
            out[key]=value
        return out
    def constant(_):raise ValueError('invalid-number')
    try:value=json.loads(text,parse_int=JsonNumber,parse_float=JsonNumber,parse_constant=constant,object_pairs_hook=pairs)
    except RecursionError as e:raise ValueError('resource-limit: nesting exceeds 64') from e
    def check(v,depth=0):
        if depth>64:raise ValueError('resource-limit: nesting exceeds 64')
        if isinstance(v,str):v.encode('utf-8')
        elif isinstance(v,dict):
            for key,item in v.items():key.encode('utf-8');check(item,depth+1)
        elif isinstance(v,list):
            for item in v:check(item,depth+1)
    check(value)
    return LosslessDocument(text,value)
