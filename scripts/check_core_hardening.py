"""Independent structural oracle and common runtime/loader corpus. Run from repo root."""
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
from jsonschema import Draft202012Validator
from referencing import Registry, Resource
sys.path.insert(0,'bindings/python')
from foreverworks.model import load_model, normalize
ROOT=Path.cwd()
SCHEMAS=[json.loads(p.read_text()) for p in Path('spec/schemas').glob('*.json')]
registry=Registry().with_resources((s['$id'],Resource.from_contents(s)) for s in SCHEMAS)
manifest_schema=next(s for s in SCHEMAS if 'manifest' in s['$id'])
kinds={s['properties']['kind']['const']:s for s in SCHEMAS if 'kind' in s.get('properties',{})}
def oracle(manifest,records):
 return Draft202012Validator(manifest_schema,registry=registry).is_valid(manifest) and all(isinstance(r,dict) and isinstance(r.get('kind'),str) and r['kind'] in kinds and Draft202012Validator(kinds[r['kind']],registry=registry).is_valid(r) for r in records)
def command(args):
 result=subprocess.run(args,capture_output=True,check=True)
 return result.stdout
bindings={'javascript':str(ROOT/'packages/javascript/src/index.js'),'typescript':str(ROOT/'packages/typescript/dist/index.js')}
def check(root,expected,name,count=None):
 results={}
 try:
  m=load_model(root);results['python']={'valid':not m.validate(),'count':len(m.records)}
 except (ValueError,OSError,TypeError): results['python']={'valid':False}
 for binding,module in bindings.items(): results[binding]=json.loads(command(['node','scripts/core_probe.mjs',module,str(root)]))
 for binding,probe in [('c','bindings/c/build/probe'),('cpp','bindings/cpp/build/probe')]: results[binding]=json.loads(command([probe,str(root)]))
 for binding,result in results.items():
  assert result['valid']==expected,(name,binding,result)
  if count is not None and 'count' in result: assert result['count']==count,(name,binding,'silent record loss',result)
 return results
started=time.monotonic();total=0
for case in json.loads(Path('conformance/hardening/cases.json').read_text()):
 assert oracle(case['manifest'],case['records'])==case['structural'],('oracle',case['name'])
 with tempfile.TemporaryDirectory() as d:
  root=Path(d);(root/'manifest.json').write_text(json.dumps(case['manifest']))
  for i,r in enumerate(case['records']): (root/('record.json' if i==0 else 'second.json')).write_text(json.dumps(r))
  check(root,case['valid'],case['name'],len(case['records']));total+=1
  if case['valid']:
   expected={**case['manifest'],'records':case['records']}
   for probe in ['bindings/c/build/probe','bindings/cpp/build/probe']:
    result=json.loads(command([probe,str(root),'serialize']))
    assert result==expected,('native roundtrip',case['name'],probe,result)
for case in json.loads(Path('conformance/fixtures/cases.json').read_text())['cases']:
 check(Path('conformance/fixtures')/case['name']/'forever',case['valid'],case['name']);total+=1
# Every shipped manifest, including self model and examples, must validate independently.
for path in [Path('forever/manifest.json'),*Path('examples').rglob('manifest.json')]:
 manifest=json.loads(path.read_text());records=[json.loads((path.parent/p).read_text()) for paths in manifest['records'].values() for p in paths]
 assert oracle(manifest,records),('shipped structural model',str(path))
 check(path.parent,True,str(path));total+=1
# Loader failures are not semantic validation findings. No binding may return success.
base={'foreverVersion':'0.1','projectId':'test','records':{'capabilities':['record.json']}}
good={'foreverVersion':'0.1','id':'good','kind':'capability','name':'Good','statement':'Good'}
raws=[('duplicate-member',b'{"kind":"capability","kind":"intent"}'),('escaped-duplicate',b'{"id":1,"\\u0069d":2}'),('invalid-utf8',b'{"x":"\xff"}'),('broken-json',b'{'),('leading-zero',b'{"future":01}'),('unescaped-control',b'{"future":"a\x01b"}'),('depth',('['*66+'0'+']'*66).encode()),('oversized',b' ' * 1048577),('missing',None)]
for name,raw in raws:
 with tempfile.TemporaryDirectory() as d:
  root=Path(d);(root/'manifest.json').write_text(json.dumps(base))
  if raw is not None:(root/'record.json').write_bytes(raw)
  check(root,False,name);total+=1
for name,rel in [('traversal','../outside.json'),('absolute','/tmp/outside.json'),('windows-drive','C:\\outside.json'),('windows-unc','\\\\server\\share\\record.json')]:
 with tempfile.TemporaryDirectory() as d:
  root=Path(d);manifest=copy.deepcopy(base);manifest['records']['capabilities']=[rel];(root/'manifest.json').write_text(json.dumps(manifest));check(root,False,name);total+=1
with tempfile.TemporaryDirectory() as d:
 root=Path(d)/'model';root.mkdir();(root/'manifest.json').write_text(json.dumps(base));outside=Path(d)/'outside.json';outside.write_text(json.dumps(good))
 try:(root/'record.json').symlink_to(outside)
 except OSError:print('BLOCKED: platform symlink creation unavailable');raise
 check(root,False,'symlink-escape');total+=1
# Genuine within-root file symlinks must remain usable, not merely rejected wholesale.
with tempfile.TemporaryDirectory() as d:
 root=Path(d);(root/'manifest.json').write_text(json.dumps(base));(root/'inside.json').write_text(json.dumps(good));(root/'record.json').symlink_to(root/'inside.json')
 check(root,True,'within-root-symlink');total+=1
# Junctions are a distinct Windows real-target case, not a string simulation.
if os.name=='nt':
 for outside in [False,True]:
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)/'model';root.mkdir();target=Path(d)/'outside' if outside else root/'inside';target.mkdir();(target/'record.json').write_text(json.dumps(good))
   subprocess.run(['cmd','/c','mklink','/J',str(root/'linked'),str(target)],check=True,capture_output=True)
   manifest=copy.deepcopy(base);manifest['records']['capabilities']=['linked/record.json'];(root/'manifest.json').write_text(json.dumps(manifest))
   check(root,not outside,'junction-escape' if outside else 'junction-contained');total+=1
# Count and aggregate-byte limits with otherwise-valid unique records.
for name,count,padding in [('record-limit',4097,0),('aggregate-byte-limit',18,950000)]:
 with tempfile.TemporaryDirectory() as d:
  root=Path(d);manifest=copy.deepcopy(base);manifest['records']['capabilities']=[f'r{i}.json' for i in range(count)]
  (root/'manifest.json').write_text(json.dumps(manifest))
  for i in range(count):
   r={**good,'id':f'r{i}','future':' '*padding};(root/f'r{i}.json').write_text(json.dumps(r))
  check(root,False,name);total+=1
# Actual bytes and digest, not parsed-object equivalence.
source=Path('conformance/hardening/normalization.input.json');expected=Path('conformance/hardening/normalization.expected.json').read_bytes()
outputs={'python':normalize(json.loads(source.read_text())).encode()}
for binding,module in bindings.items():outputs[binding]=command(['node','scripts/core_normalize.mjs',module,str(source)])
for binding,data in outputs.items():assert data==expected,(binding,'normalization bytes',data)
print(json.dumps({'cases':total,'semanticBindings':['python','javascript','typescript','c','cpp (C wrapper)'],'oracle':'jsonschema Draft 2020-12','normalizationSHA256':hashlib.sha256(expected).hexdigest(),'seconds':round(time.monotonic()-started,3),'maxChildRSSKiB':__import__('resource').getrusage(__import__('resource').RUSAGE_CHILDREN).ru_maxrss if sys.platform!='win32' else None},indent=2))
