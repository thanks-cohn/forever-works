"""Independent Draft 2020-12 structural proof; not an ecosystem runtime evaluator."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
schema = json.loads((ROOT / 'spec/profiles/ecosystem-composition/v0.1/composition.schema.json').read_text())
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)
fixtures = ROOT / 'conformance/ecosystem-composition/v0.1'
catalog = json.loads((fixtures / 'cases.json').read_text())
for case in catalog['cases']:
    errors = list(validator.iter_errors(json.loads((fixtures / case['path']).read_text())))
    assert (not errors) == case['schemaValid'], (case['name'], [e.message for e in errors])
print(f"Draft 2020-12 schema conformance passed: {len(catalog['cases'])} fixtures")
# Independent normalization proof for the shared, JSON-safe profile fixture.
fixture = json.loads((fixtures / 'valid/four-participant-fan.json').read_text())
normalized = json.dumps(fixture, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
assert normalized == (fixtures / 'expected/four-participant-fan.normalized.json').read_text()
print('Independent profile normalization golden passed')
