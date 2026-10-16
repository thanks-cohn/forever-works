from __future__ import annotations
from .lossless import parse_lossless, canonical_lossless
import json
from .structure import validate_structure, SCHEMAS
from pathlib import Path
from typing import Any

KINDS = {"intent","capability","invariant","constraint","dependency","decision","compatibility","migration","implementation","evidence"}
REF_FIELDS = {"relatedCapabilities","relatedConstraints","relatedInvariants","relatedImplementations","requiredCapabilities","protectedInvariants","compatibilityObligations","relatedEntities","preservedCapabilities","preservedInvariants","compatibilityImpact","verification","satisfiesCapabilities","constrainedByInvariants","satisfiesConstraints","compatibilityContracts","evidence","sourceImplementation","targetImplementation","currentImplementation","scope","validationReferences"}
REQUIRED = {
 "intent":("name","statement","purpose"), "capability":("name","statement"), "invariant":("name","statement","severity"),
 "constraint":("statement","category","classification"), "dependency":("dependencyName","dependencyType","purpose","reasonSelected","replacementClassification"),
 "decision":("title","status","context","decision","rationale"), "compatibility":("contractType","boundary","mustPreserve","migrationPolicy","version"),
 "migration":("sourceImplementation","targetImplementation","reason","status"), "implementation":("type","technology","satisfiesCapabilities"),
 "evidence":("type","source","statementSupported","confidence")}
CLASSIFICATIONS={"LOCKED","SEMANTIC","CAPABILITY","TRANSITIONAL","LEGACY","OPTIONAL"}
class ModelError(ValueError):
    def __init__(self,message,code=None,path=None,stage=None):
        super().__init__(message)
        self.code=code or message.split(':',1)[0]
        self.path=path
        self.stage=stage


def normalize(value: Any) -> str:
    """Portable two-space JSON for the documented binary64 interchange subset."""
    import math
    from decimal import Decimal
    def emit(v,n=0):
        if n>64: raise ModelError('resource-limit: JSON nesting exceeds 64')
        if v is None: return 'null'
        if isinstance(v,bool): return 'true' if v else 'false'
        if isinstance(v,str):
            try: v.encode('utf-8')
            except UnicodeError as e: raise ModelError('invalid-unicode') from e
            return json.dumps(v,ensure_ascii=False)
        if type(v) in (int,float):
            if type(v) is float and not math.isfinite(v): raise ModelError('unsupported-number')
            if abs(v)>9007199254740991: return json.dumps(v,allow_nan=False)
            if v==0: return '0'
            if v==int(v): return str(int(v))
            text=repr(v)
            if 'e' in text:
                mantissa,exponent=text.split('e'); exponent=int(exponent)
                if exponent>=-6: return format(Decimal(text),'f')
                return mantissa.rstrip('0').rstrip('.')+'e'+str(exponent)
            return text
        if not isinstance(v,(dict,list)): raise ModelError('invalid-json-value')
        keys=sorted(v) if isinstance(v,dict) else range(len(v))
        if not len(v): return '{}' if isinstance(v,dict) else '[]'
        items=['  '*(n+1)+(emit(k,n+1)+': ' if isinstance(v,dict) else '')+emit(v[k],n+1) for k in keys]
        return ('{' if isinstance(v,dict) else '[')+'\n'+',\n'.join(items)+'\n'+'  '*n+('}' if isinstance(v,dict) else ']')
    return emit(value)+'\n'

def _refs(record):
    properties=next((s['properties'] for s in SCHEMAS.values() if 'kind' in s.get('properties',{}) and s['properties']['kind']['const']==record.get('kind')), {})
    for key in REF_FIELDS:
        if key not in properties: continue
        value=record.get(key)
        if isinstance(value,str): yield value
        elif isinstance(value,list):
            for item in value:
                if isinstance(item,str): yield item
    for check in record.get("verification",[]) if "verification" in properties and isinstance(record.get("verification"),list) else []:
        if isinstance(check,dict):
            for evidence in check.get("evidence",[]) if isinstance(check.get("evidence"),list) else []:
                if isinstance(evidence,str): yield evidence
    for claim in record.get("claims",[]) if "claims" in properties and isinstance(record.get("claims"),list) else []:
        if isinstance(claim,dict):
            for evidence in claim.get("evidence",[]) if isinstance(claim.get("evidence"),list) else []:
                if isinstance(evidence,str): yield evidence

class Model:
    def __init__(self, manifest, records, root=None):
        self.manifest, self.records, self.root = manifest, records, root
        self.entities={r.get("id"):r for r in (records if isinstance(records,list) else []) if isinstance(r,dict) and isinstance(r.get("id"),str)}
    def validate(self):
        errors=validate_structure(self.manifest,self.records)
        ids=set(self.entities)
        for r in self.records if isinstance(self.records,list) else []:
            if isinstance(r,dict):
                for ref in _refs(r):
                    if ref not in ids: errors.append({"code":"broken-reference","path":r.get("id","?"),"reference":ref,"message":f"unknown reference {ref}"})
        return sorted(errors,key=lambda e:(e["code"],e["path"],e.get("reference","")))
    def get_entity(self,id): return self.entities.get(id)
    def list(self,kind): return sorted((r for r in self.records if r.get("kind")==kind),key=lambda r:r["id"])
    def trace(self,id):
        if id not in self.entities: raise ModelError(f"entity not found: {id}")
        adjacency={x:set() for x in self.entities}
        for r in self.records:
            for ref in _refs(r):
                if ref in adjacency: adjacency[r["id"]].add(ref); adjacency[ref].add(r["id"])
        found=set(); todo=[id]
        while todo:
            cur=todo.pop()
            if cur in found: continue
            found.add(cur); todo.extend(adjacency[cur]-found)
        return [self.entities[x] for x in sorted(found)]
    def explain_dependency(self,id):
        r=self.entities.get(id)
        if not r or r.get("kind")!="dependency": raise ModelError(f"dependency not found: {id}")
        keys=("id","dependencyName","purpose","reasonSelected","replacementClassification","requiredCapabilities","protectedInvariants","relatedConstraints","replacementRequirements","compatibilityObligations","historicalContext","provenance")
        return {k:r[k] for k in keys if k in r}
    def find_dependencies(self,*classes): return [r for r in self.list("dependency") if r.get("replacementClassification") in classes]
    def audit(self):
        issues=list(self.validate())
        for r in self.records:
            rid=r.get("id","?"); kind=r.get("kind")
            if kind not in ("evidence",) and "provenance" not in r: issues.append({"code":"missing-provenance","path":rid,"message":"record has no provenance"})
            if kind=="capability" and not r.get("relatedImplementations"): issues.append({"code":"capability-no-implementation","path":rid,"message":"capability has no implementation"})
            if kind=="dependency" and not r.get("purpose"): issues.append({"code":"dependency-no-purpose","path":rid,"message":"dependency has no purpose"})
            if kind=="invariant" and not r.get("verification"): issues.append({"code":"invariant-no-verification","path":rid,"message":"invariant has no verification"})
            if kind=="compatibility" and not r.get("validationReferences"): issues.append({"code":"compatibility-no-validation","path":rid,"message":"compatibility contract has no validation"})
            if kind=="dependency" and r.get("replacementClassification")=="TRANSITIONAL" and not r.get("revisitCondition"): issues.append({"code":"transitional-no-revisit","path":rid,"message":"transitional dependency has no revisit condition"})
            if kind=="migration" and not r.get("verification"): issues.append({"code":"migration-unverified","path":rid,"message":"migration has no verification evidence"})
        return sorted(issues,key=lambda x:(x["code"],x["path"]))
    def evaluate_replacement(self,current,candidate):
        dep=self.entities.get(current); cand=self.entities.get(candidate)
        if not dep or dep.get("kind")!="dependency": raise ModelError(f"dependency not found: {current}")
        if not cand or cand.get("kind")!="implementation": raise ModelError(f"implementation not found: {candidate}")
        requirements=[]
        for field in ("requiredCapabilities","protectedInvariants","relatedConstraints","replacementRequirements","compatibilityObligations"):
            requirements += dep.get(field,[])
        return _evaluation(candidate,requirements,cand.get("claims",[]))
    def verify_migration(self,id):
        migration=self.entities.get(id)
        if not migration or migration.get("kind")!="migration": raise ModelError(f"migration not found: {id}")
        requirements=migration.get("preservedCapabilities",[])+migration.get("preservedInvariants",[])+migration.get("compatibilityImpact",[])
        result=_evaluation(id,requirements,migration.get("claims",[]))
        evidence=set(migration.get("verification",[]))
        for check in result["checks"]:
            if check["status"]=="pass" and not evidence.intersection(check.get("evidence",[])):
                check["status"]="unknown"; check["reason"]="No referenced migration verification evidence"
        result["result"]=_overall(result["checks"])
        return result
    def normalized(self): return normalize({**self.manifest,"records":sorted(self.records,key=lambda r:r["id"])})

def _overall(checks):
    statuses={c["status"] for c in checks}
    return "fail" if "fail" in statuses else "pass" if checks and statuses=={"pass"} else "partial"
def _evaluation(candidate,requirements,claims):
    claimmap={c.get("requirement"):c for c in claims if isinstance(c,dict)}; checks=[]
    for req in dict.fromkeys(requirements):
        c=claimmap.get(req)
        if c: checks.append({k:c[k] for k in ("requirement","status","evidence","reason") if k in c})
        else: checks.append({"requirement":req,"status":"unknown","reason":"No candidate evidence supplied"})
    return {"candidate":candidate,"result":_overall(checks),"checks":checks}

def _load_model(root,lossless=False):
    from pathlib import PureWindowsPath
    root=Path(root); root=root.parent if root.name=="manifest.json" else root
    root=root.resolve(strict=True)
    total=0;documents=[]
    def pairs(items):
        result={}
        for key,value in items:
            if key in result: raise ModelError("duplicate-member")
            result[key]=value
        return result
    def depth(value,n=0):
        if n>64: raise ModelError("resource-limit: nesting exceeds 64")
        if isinstance(value,str):
            try: value.encode('utf-8')
            except UnicodeError as e: raise ModelError('invalid-unicode') from e
        elif type(value) is float and not __import__('math').isfinite(value): raise ModelError('unsupported-number')
        elif isinstance(value,dict):
            for key,item in value.items(): depth(key,n+1);depth(item,n+1)
        elif isinstance(value,list):
            for item in value: depth(item,n+1)
    def read(path):
        nonlocal total
        try:
            path=path.resolve(strict=True)
            if root not in path.parents: raise ModelError("path-escape: target outside model root")
            size=path.stat().st_size
            total+=size
            if size>1048576 or total>16777216: raise ModelError("resource-limit: model byte limit")
            with path.open('rb') as stream: data=stream.read(1048577)
            if len(data)>1048576: raise ModelError("resource-limit: file byte limit")
            if lossless:
                document=parse_lossless(data)
                documents.append({'path':path.relative_to(root).as_posix(),'document':document})
                return document.value
            value=json.loads(data.decode('utf-8'),object_pairs_hook=pairs,parse_constant=lambda _: (_ for _ in ()).throw(ModelError('invalid-json-number')))
            depth(value)
            return value
        except (OSError,UnicodeError,json.JSONDecodeError,RecursionError) as e: raise ModelError("invalid-input: cannot read bounded UTF-8 JSON") from e
    manifest=read(root/'manifest.json')
    issues=[e for e in validate_structure(manifest,[]) if e['path'].startswith('manifest')]
    if issues: raise ModelError('invalid-manifest: '+issues[0]['path'])
    records=[]; seen=set()
    for paths in manifest['records'].values():
        for rel in paths:
            if Path(rel).is_absolute() or PureWindowsPath(rel).is_absolute() or "\\" in rel or '..' in rel.split('/'): raise ModelError('path-escape: expected portable relative path')
            path=root/rel
            if path in seen: raise ModelError('duplicate-path')
            seen.add(path)
            if len(seen)>4096: raise ModelError('resource-limit: record count exceeds 4096')
            records.append(read(path))
    if lossless: return LosslessModel(manifest,records,root,documents)
    return Model(manifest,records,root)

def _load(root,lossless=False):
    try: return _load_model(root,lossless)
    except ModelError as e:
        e.stage='load'
        if e.path is None: e.path=str(root)
        raise
    except ValueError as e:
        code=str(e).split(':',1)[0]
        if code not in {'invalid-number','duplicate-member','resource-limit'}:code='invalid-input'
        raise ModelError(code+': cannot read lossless JSON',code=code,path=str(root),stage='load') from e
    except (OSError,RecursionError) as e:
        raise ModelError('io: model input cannot be read',code='io',path=str(root),stage='load') from e

class LosslessModel(Model):
    def __init__(self,manifest,records,root,documents):
        super().__init__(manifest,records,root);self.documents=tuple(documents)
    def normalized(self):return canonical_lossless({**self.manifest,'records':sorted(self.records,key=lambda r:r['id'])})
    def source_documents(self):return self.documents

def load_model(root):return _load(root)
def load_model_lossless(root):return _load(root,True)
