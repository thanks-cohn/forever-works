"""Read-only probes of the audited starting commit; no checkout/history changes."""
import json
from pathlib import Path
import subprocess
import tempfile
START='ecb3369ae1f92b5710e8dd07d277ee2d63083097'
def run(args):return subprocess.check_output(args,text=True)
def source(path):return run(['git','show',START+':'+path])
Path('work').mkdir(exist_ok=True)
with tempfile.TemporaryDirectory(dir='work') as d:
 root=Path(d).resolve();js=root/'javascript';js.mkdir()
 (js/'package.json').write_text('{"type":"module"}')
 for name in ['model.js','node.js','index.js']:(js/name).write_text(source('packages/javascript/src/'+name))
 (root/'forever.c').write_text(source('bindings/c/src/forever.c'))
 (root/'forever.h').write_text(source('bindings/c/include/forever.h'))
 run(['cc','-std=c11','-I'+str(root),str(root/'forever.c'),'bindings/c/tests/probe.c','-o',str(root/'probe')])
 results={}
 for case in ['invalid-missing-id','invalid-reference']:
  results['F3-'+case]=json.loads(run([str(root/'probe'),f'conformance/fixtures/{case}/forever']))
 patches=[{'id':'INVALID ID!'},{'foreverVersion':'99.0'},{'name':42,'statement':None},{'provenance':{'sourceType':'made-up','confidence':99}},{'relatedInvariants':['missing']}]
 base={'foreverVersion':'0.1','id':'good','kind':'capability','name':'Good','statement':'Good'}
 script=f'import {{Model}} from {json.dumps(str(js/"model.js"))};const patches={json.dumps(patches)};console.log(JSON.stringify(patches.map(p=>new Model({{foreverVersion:"0.1"}},[{{...{json.dumps(base)},...p}}]).validate())));'
 results['F1-runtime-errors']=json.loads(run(['node','--input-type=module','-e',script]))
 model=root/'model';model.mkdir();outside=root/'outside.json'
 outside.write_text(json.dumps({'foreverVersion':'0.1','id':'good','kind':'capability','name':'Good','statement':'Good'}))
 (model/'record.json').symlink_to(outside)
 (model/'manifest.json').write_text(json.dumps({'foreverVersion':'0.1','projectId':'test','records':{'capabilities':['record.json']}}))
 results['F4-symlink-escape']=json.loads(run(['node','scripts/core_probe.mjs',str(js/'index.js'),str(model)]))
 script=f'import {{normalize}} from {json.dumps(str(js/"model.js"))};process.stdout.write(normalize({{Z:1,a:2,A:3,z:4}}));'
 results['F2-baseline-bytes']=run(['node','--input-type=module','-e',script])
 print(json.dumps(results,indent=2))
