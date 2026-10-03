import argparse, json, sys
from pathlib import Path
from .model import ModelError, load_model
DIRS={"capabilities":"capabilities","invariants":"invariants","constraints":"constraints","dependencies":"dependencies","decisions":"decisions","compatibility":"compatibility","migrations":"migrations","implementations":"implementations","evidence":"evidence"}
def emit(value, structured=True):
    if structured: print(json.dumps(value,indent=2,sort_keys=True,ensure_ascii=False))
    elif isinstance(value,list):
        for item in value: print(item.get("id",item))
    elif isinstance(value,dict):
        for k,v in value.items(): print(f"{k}: {v}")
    else: print(value)
def init(path):
    root=Path(path)/"forever"; root.mkdir(parents=True,exist_ok=True)
    for d in DIRS.values(): (root/d).mkdir(exist_ok=True)
    intent={"foreverVersion":"0.1","id":"intent.todo","kind":"intent","name":"TODO project name","statement":"TODO describe why this project exists","purpose":["TODO author the enduring purpose"],"priorities":[],"nonGoals":[],"supportedEnvironments":[],"status":"draft","relatedCapabilities":[],"relatedConstraints":[],"provenance":{"sourceType":"explicit","sourceReference":"forever init placeholder; author review required","confidence":1,"reviewStatus":"unreviewed"}}
    (root/"project.intent.json").write_text(json.dumps(intent,indent=2)+"\n")
    manifest={"foreverVersion":"0.1","projectId":"todo-project-id","records":{"intent":["project.intent.json"],**{k:[] for k in DIRS}}}
    (root/"manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
    return {"created":str(root),"files":["manifest.json","project.intent.json"],"note":"TODO values are not architectural facts"}
def main(argv=None):
    p=argparse.ArgumentParser(prog="forever"); p.add_argument("--root",default="forever"); p.add_argument("--json",action="store_true")
    sub=p.add_subparsers(dest="command",required=True)
    q=sub.add_parser("init"); q.add_argument("path",nargs="?",default=".")
    for name in ("validate","inspect","audit","normalize"): sub.add_parser(name)
    for name in ("explain","trace","verify-migration"): x=sub.add_parser(name); x.add_argument("id")
    x=sub.add_parser("evaluate-replacement"); x.add_argument("current"); x.add_argument("candidate")
    args=p.parse_args(argv)
    try:
        if args.command=="init": out=init(args.path)
        else:
            model=load_model(args.root)
            if args.command=="validate": out={"valid":not model.validate(),"errors":model.validate()}
            elif args.command=="inspect": out={"projectId":model.manifest.get("projectId"),"foreverVersion":model.manifest.get("foreverVersion"),"counts":{k:len(model.list(k)) for k in sorted(__import__('foreverworks.model',fromlist=['KINDS']).KINDS)}}
            elif args.command=="audit": out={"issues":model.audit(),"issueCount":len(model.audit())}
            elif args.command=="explain": out=model.explain_dependency(args.id)
            elif args.command=="trace": out={"start":args.id,"entities":[r["id"] for r in model.trace(args.id)]}
            elif args.command=="evaluate-replacement": out=model.evaluate_replacement(args.current,args.candidate)
            elif args.command=="verify-migration": out=model.verify_migration(args.id)
            elif args.command=="normalize": sys.stdout.write(model.normalized()); return 0
        emit(out,args.json or args.command in ("validate","inspect","audit","evaluate-replacement","verify-migration","normalize")); return 0
    except ModelError as e: print(str(e),file=sys.stderr); return 2
if __name__=="__main__": raise SystemExit(main())
