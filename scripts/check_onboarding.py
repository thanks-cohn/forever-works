"""Execute the documented CLI learning path, without running evidence commands."""
import json
import subprocess
from pathlib import Path
cli=str(Path('packages/cli/bin/forever').resolve())
# Use the documented executable on POSIX; Python module adapter works on Windows.
def run(root,*args):
 return json.loads(subprocess.check_output([cli,'--root',root,*args],text=True))
assert run('conformance/fixtures/minimal/forever','validate')['valid']
root='examples/file-transfer/forever'
assert run(root,'validate')['valid']
trace=run(root,'--json','trace','dependency.old-streamer')
assert 'intent.remote-transfer' in trace['entities']
assert run(root,'--json','explain','dependency.old-streamer')['replacementClassification']=='CAPABILITY'
evaluation=run(root,'evaluate-replacement','dependency.old-streamer','implementation.wasm-streamer')
assert evaluation['result']=='partial'
assert next(c for c in evaluation['checks'] if c['requirement']=='invariant.bounded-memory')['status']=='unknown'
print('Documented validate, trace, explain and unknown-claim path passed')
