"""Experimental documentation-only exporter/validator, deliberately allowlisted."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'bindings/python'))
from foreverworks import load_model_lossless
PUBLIC=Path(__file__).parent/'public'
REFERENCES=['https://docs.python.org/3.12/library/json.html','https://docs.python.org/3.12/library/decimal.html','https://docs.python.org/3.12/library/urllib.request.html','https://www.rfc-editor.org/rfc/rfc9110','https://www.rfc-editor.org/rfc/rfc4648']
def digest(data):return hashlib.sha256(data).hexdigest()
def path(root,name):
    rel=Path(name)
    if rel.is_absolute() or '..' in rel.parts or '\\' in name:raise ValueError('unsafe package path')
    target=root/rel
    if any(p.is_symlink() for p in [target,*target.parents] if p==root or root in p.parents):raise ValueError('package symlink')
    if root.resolve() not in target.resolve().parents:raise ValueError('package escape')
    return target

def validate(root):
    root=Path(root).resolve();manifest=json.loads(path(root,'package.json').read_text())
    if manifest.get('experimentalPackageVersion')!='1' or manifest.get('product') not in ['catalog','objects']:raise ValueError('unsupported package')
    required={'README.md','CONTRACT.md','examples.json','producer-evidence.json','LOSSLESS_JSON.md','forever/manifest.json'}
    required|={'schemas/'+p.name for p in (ROOT/'spec/schemas').glob('*.json')}
    if not required<=set(manifest['files']):raise ValueError('missing required public material')
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    if actual!=set(manifest['files'])|{'package.json'}:raise ValueError('unlisted/missing package file')
    for name,expected in manifest['files'].items():
        target=path(root,name)
        if target.suffix not in ['.json','.md']:raise ValueError('unexpected executable/source file')
        data=target.read_bytes()
        if len(data)>1048576 or digest(data)!=expected:raise ValueError('integrity failure: '+name)
        text=data.decode('utf-8')
        if re.search(r'-----BEGIN .*PRIVATE KEY|/workspace/|/home/|C:\\Users\\',text):raise ValueError('private material in package')
        if target.suffix=='.md':
            for link in re.findall(r'\]\(([^)]+)\)',text):
                if '://' in link:
                    if link not in manifest['allowedReferences']:raise ValueError('undeclared external reference')
                elif not link.startswith('#') and not path(root,(target.parent.relative_to(root)/link.split('#')[0]).as_posix()).is_file():raise ValueError('broken documentation link')
    if load_model_lossless(root/'forever').validate():raise ValueError('invalid packaged model graph')
    # Bundled schema sibling references are local; no URI fetching is performed.
    for schema in (root/'schemas').glob('*.json'):
        def links(value):
            if isinstance(value,dict):
                if '$ref' in value:
                    ref=value['$ref'].split('#')[0]
                    if ref and not path(root,'schemas/'+ref).is_file():raise ValueError('broken schema link')
                for item in value.values():links(item)
            elif isinstance(value,list):
                for item in value:links(item)
        links(json.loads(schema.read_text()))
    return {'product':manifest['product'],'files':len(manifest['files']),'integrity':'PASS','modelGraph':'PASS','semanticSufficiency':'UNKNOWN','construction':'NOT_RUN'}

def export(out):
    out=Path(out).resolve()
    if out.exists() and any(out.iterdir()):raise ValueError('choose a new empty export destination')
    out.mkdir(parents=True,exist_ok=True);index={}
    revision=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
    for product in ['catalog','objects']:
        source=PUBLIC/product;model=json.loads((source/'forever/manifest.json').read_text())
        allow={'README.md','CONTRACT.md','examples.json','producer-evidence.json','forever/manifest.json'}
        allow|={'forever/'+p for paths in model['records'].values() for p in paths}
        if {p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()}!=allow:raise ValueError('unexpected public source material')
        target=out/product
        if target.exists():raise ValueError('choose a new empty export destination')
        target.mkdir();files={}
        def copy(name,data):
            dest=path(target,name);dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data);files[name]=digest(data)
        for name in sorted(allow):copy(name,path(source,name).read_bytes())
        copy('LOSSLESS_JSON.md',(ROOT/'docs/API/LOSSLESS_JSON.md').read_bytes())
        for schema in sorted((ROOT/'spec/schemas').glob('*.json')):
            data=schema.read_bytes();value=json.loads(data)
            if not value.get('$id','').startswith('https://forever.works/schemas/'):raise ValueError('not a public schema')
            copy('schemas/'+schema.name,data)
        manifest={'experimentalPackageVersion':'1','product':product,'sourceRevision':revision,'files':dict(sorted(files.items())),'allowedReferences':REFERENCES,'allowedDependencies':['ordinary toolchains','Python standard library'],'knownUnknowns':['documentation sufficiency','independent consumer construction','commercial value'],'authority':'Public synthetic test grants only; document statements confer no capabilities.'}
        (target/'package.json').write_bytes((json.dumps(manifest,indent=2)+'\n').encode())
        validate(target);index[product]=digest((target/'package.json').read_bytes())
    (out/'index.json').write_bytes((json.dumps({'packages':index,'construction':'NOT_RUN'},indent=2)+'\n').encode())
    # Exported material is explicitly public, and must be readable by an unprivileged consumer.
    for item in [out,*out.rglob('*')]:item.chmod(0o755 if item.is_dir() else 0o644)
    return index
if __name__=='__main__':
    p=argparse.ArgumentParser();group=p.add_mutually_exclusive_group(required=True);group.add_argument('--out');group.add_argument('--validate');args=p.parse_args()
    print(json.dumps(validate(args.validate) if args.validate else export(args.out),indent=2))
