from __future__ import annotations
import json
from pathlib import Path
from typing import Any

KINDS = {"intent","capability","invariant","constraint","dependency","decision","compatibility","migration","implementation","evidence"}
REF_FIELDS = {"relatedCapabilities","relatedConstraints","relatedInvariants","relatedImplementations","requiredCapabilities","protectedInvariants","compatibilityObligations","relatedEntities","preservedCapabilities","preservedInvariants","compatibilityImpact","verification","satisfiesCapabilities","constrainedByInvariants","satisfiesConstraints","compatibilityContracts","evidence","sourceImplementation","targetImplementation","currentImplementation"}
REQUIRED = {
 "intent":("name","statement","purpose"), "capability":("name","statement"), "invariant":("name","statement","severity"),
 "constraint":("statement","category","classification"), "dependency":("dependencyName","dependencyType","purpose","reasonSelected","replacementClassification"),
 "decision":("title","status","context","decision","rationale"), "compatibility":("contractType","boundary","mustPreserve","migrationPolicy","version"),
 "migration":("sourceImplementation","targetImplementation","reason","status"), "implementation":("type","technology","satisfiesCapabilities"),
 "evidence":("type","source","statementSupported","confidence")}
CLASSIFICATIONS={"LOCKED","SEMANTIC","CAPABILITY","TRANSITIONAL","LEGACY","OPTIONAL"}
class ModelError(ValueError): pass

def normalize(value: Any) -> str:
    """Canonical JSON: sorted keys, two spaces, UTF-8 text, trailing newline."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2, separators=(",", ": ")) + "\n"

def _refs(record):
    for key in REF_FIELDS:
        value=record.get(key)
        if isinstance(value,str) and ("." in value): yield value
        elif isinstance(value,list):
            for item in value:
                if isinstance(item,str) and "." in item: yield item
    for claim in record.get("claims",[]):
        if isinstance(claim,dict):
            for evidence in claim.get("evidence",[]): yield evidence

class Model:
    def __init__(self, manifest, records, root=None):
        self.manifest, self.records, self.root = manifest, records, root
        self.entities={r.get("id"):r for r in records if isinstance(r,dict) and r.get("id")}
    def validate(self):
        errors=[]
        version=self.manifest.get("foreverVersion")
        if not isinstance(version,str) or version.split(".")[0] != "0": errors.append({"code":"unsupported-version","path":"manifest.foreverVersion","message":f"unsupported version {version!r}"})
        seen=set()
        for i,r in enumerate(self.records):
            where=f"records[{i}]"
            if not isinstance(r,dict): errors.append({"code":"invalid-record","path":where,"message":"record must be an object"}); continue
            for key in ("foreverVersion","id","kind"):
                if not r.get(key): errors.append({"code":"missing-required","path":f"{where}.{key}","message":f"missing {key}"})
            kind=r.get("kind")
            if kind not in KINDS: errors.append({"code":"invalid-kind","path":f"{where}.kind","message":f"unknown kind {kind!r}"})
            for key in REQUIRED.get(kind,()):
                if key not in r: errors.append({"code":"missing-required","path":f"{where}.{key}","message":f"missing {key}"})
            rid=r.get("id")
            if rid in seen: errors.append({"code":"duplicate-id","path":where,"message":f"duplicate ID {rid}"})
            seen.add(rid)
            if kind=="dependency" and r.get("replacementClassification") not in CLASSIFICATIONS: errors.append({"code":"invalid-classification","path":where,"message":"invalid dependency classification"})
        ids={r.get("id") for r in self.records if isinstance(r,dict)}
        for r in self.records:
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
    def normalized(self): return normalize({"foreverVersion":self.manifest["foreverVersion"],"projectId":self.manifest["projectId"],"records":sorted(self.records,key=lambda r:r["id"])})

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

def load_model(root):
    root=Path(root); root=root.parent if root.name=="manifest.json" else root
    try: manifest=json.loads((root/"manifest.json").read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as e: raise ModelError(str(e)) from e
    records=[]
    listed=[]
    for paths in manifest.get("records",{}).values():
        if isinstance(paths,list): listed.extend(paths)
    for rel in listed:
        path=(root/rel).resolve()
        if root.resolve() not in path.parents: raise ModelError(f"record path escapes model root: {rel}")
        try: records.append(json.loads(path.read_text(encoding="utf-8")))
        except (OSError,json.JSONDecodeError) as e: raise ModelError(f"{rel}: {e}") from e
    return Model(manifest,records,root)
