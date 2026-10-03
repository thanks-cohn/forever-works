import json,sys
from pathlib import Path
sys.path.insert(0,'bindings/python')
from foreverworks import load_model
out=Path('conformance/expected');out.mkdir(exist_ok=True)
for name in ('minimal','complete'):
 m=load_model(f'conformance/fixtures/{name}/forever');(out/f'{name}.normalized.json').write_text(m.normalized())
m=load_model('conformance/fixtures/complete/forever')
(out/'replacement.json').write_text(json.dumps(m.evaluate_replacement('dependency.old-streamer','implementation.wasm-streamer'),indent=2,sort_keys=True)+'\n')
(out/'migration-preserving.json').write_text(json.dumps(m.verify_migration('migration.old-to-wasm'),indent=2,sort_keys=True)+'\n')
m=load_model('conformance/fixtures/migration-preserving/forever')
(out/'migration-preserving.json').write_text(json.dumps(m.verify_migration('migration.old-to-wasm'),indent=2,sort_keys=True)+'\n')
m=load_model('conformance/fixtures/migration-violating/forever')
(out/'migration-violating.json').write_text(json.dumps(m.verify_migration('migration.old-to-wasm'),indent=2,sort_keys=True)+'\n')
