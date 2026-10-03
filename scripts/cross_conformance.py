import json,subprocess,sys
from pathlib import Path
sys.path.insert(0,'bindings/python')
from foreverworks import load_model
fail=[]
for name in ('minimal','complete'):
 expected=(Path('conformance/expected')/f'{name}.normalized.json').read_text()
 py=load_model(f'conformance/fixtures/{name}/forever').normalized()
 if py!=expected: fail.append(f'Python normalization differs: {name}')
 script=f'import {{loadModel}} from "./packages/typescript/dist/index.js"; console.log((await loadModel("conformance/fixtures/{name}/forever")).normalized().trimEnd())'
 ts=subprocess.run(['node','--input-type=module','-e',script],capture_output=True,text=True)
 if ts.returncode or ts.stdout.rstrip()+"\n"!=expected: fail.append(f'TypeScript normalization differs: {name}: {ts.stderr}')
if fail: print('\n'.join(fail),file=sys.stderr);raise SystemExit(1)
print('cross-language golden normalization passed')
