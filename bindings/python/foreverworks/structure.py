from .lossless import JsonNumber
"""Core-schema subset evaluator. Independent Draft 2020-12 oracle lives in scripts."""
import json
import re
from pathlib import Path
SCHEMAS=json.loads(Path(__file__).with_name('contracts.json').read_text())

def structural(value,schema,path,errors):
    def issue(code,suffix=''):
        errors.append(dict(code=code,path=path+suffix,message=f'{code} at {path+suffix}'))
    if '$ref' in schema:
        file,_,fragment=schema['$ref'].partition('#')
        schema=SCHEMAS[file]
        if fragment:
            for part in fragment[1:].split('/'): schema=schema[part]
    types={'object':lambda v:isinstance(v,dict),'array':lambda v:isinstance(v,list),'string':lambda v:isinstance(v,str),'number':lambda v:isinstance(v,JsonNumber) or (type(v) in (int,float) and __import__('math').isfinite(v))}
    if 'type' in schema and not types[schema['type']](value): issue('invalid-type'); return
    if 'const' in schema and value!=schema['const']: issue('invalid-value')
    if 'enum' in schema and value not in schema['enum']: issue('invalid-classification' if path.endswith('.replacementClassification') else 'invalid-value')
    if isinstance(value,str) and 'pattern' in schema and not re.search(schema['pattern'],value): issue('invalid-value')
    if isinstance(value,JsonNumber) and (('minimum' in schema and value.decimal<schema['minimum']) or ('maximum' in schema and value.decimal>schema['maximum'])): issue('invalid-value')
    if type(value) in (int,float) and (value<schema.get('minimum',float('-inf')) or value>schema.get('maximum',float('inf'))): issue('invalid-value')
    if isinstance(value,dict):
        for key in schema.get('required',[]):
            if key not in value: issue('missing-required','.'+key)
        for key,item in value.items():
            if 'propertyNames' in schema: structural(key,schema['propertyNames'],path+'.'+key,errors)
            if key in schema.get('properties',{}): structural(item,schema['properties'][key],path+'.'+key,errors)
            elif schema.get('additionalProperties') is False: issue('unknown-field','.'+key)
    if isinstance(value,list):
        if schema.get('uniqueItems') and len({x.canonical() if isinstance(x,JsonNumber) else json.dumps(x,sort_keys=True,default=lambda v:v.canonical()) for x in value})!=len(value): issue('duplicate-value')
        if 'items' in schema:
            for i,item in enumerate(value): structural(item,schema['items'],f'{path}[{i}]',errors)

def validate_structure(manifest,records):
    errors=[]
    structural(manifest,SCHEMAS['manifest.schema.json'],'manifest',errors)
    kinds={s['properties']['kind']['const']:s for s in SCHEMAS.values() if 'kind' in s.get('properties',{})}
    if not isinstance(records,list): return errors+[dict(code='invalid-type',path='records',message='records must be an array')]
    ids=set()
    for i,record in enumerate(records):
        path=f'records[{i}]'
        if not isinstance(record,dict): errors.append(dict(code='invalid-record',path=path,message='record must be an object')); continue
        kind=record.get('kind')
        schema=kinds.get(kind) if isinstance(kind,str) else None
        if schema: structural(record,schema,path,errors)
        else: errors.append(dict(code='invalid-kind',path=path+'.kind',message='unknown record kind'))
        rid=record.get('id')
        if isinstance(rid,str):
            if rid in ids: errors.append(dict(code='duplicate-id',path=path,message='duplicate ID'))
            ids.add(rid)
        if not isinstance(record.get('foreverVersion'),str) or not re.fullmatch(r'0\.[0-9]+',record['foreverVersion']): errors.append(dict(code='unsupported-version',path=path+'.foreverVersion',message='expected supported 0.x version'))
    if not isinstance(manifest,dict) or not isinstance(manifest.get('foreverVersion'),str) or not re.fullmatch(r'0\.[0-9]+',manifest['foreverVersion']): errors.append(dict(code='unsupported-version',path='manifest.foreverVersion',message='expected supported 0.x version'))
    return errors
