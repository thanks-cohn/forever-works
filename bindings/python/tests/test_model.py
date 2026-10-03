import json, tempfile, unittest
from pathlib import Path
from foreverworks import load_model
class ModelTests(unittest.TestCase):
 def test_complete(self):
  m=load_model('conformance/fixtures/complete/forever'); self.assertEqual([],m.validate()); self.assertIn('intent.remote-transfer',[x['id'] for x in m.trace('dependency.old-streamer')]); self.assertEqual('partial',m.evaluate_replacement('dependency.old-streamer','implementation.wasm-streamer')['result']); self.assertEqual('partial',m.verify_migration('migration.old-to-wasm')['result'])
 def test_cases(self):
  for case in json.loads(Path('conformance/fixtures/cases.json').read_text())['cases']:
   with self.subTest(case=case['name']): self.assertEqual(case['valid'],not load_model(f"conformance/fixtures/{case['name']}/forever").validate())
 def test_unknown_preserved(self): self.assertIn('futureField',load_model('conformance/fixtures/unknown-future-field/forever').normalized())
 def test_cycle_terminates(self): self.assertEqual(2,len(load_model('conformance/fixtures/circular-relationship/forever').trace('capability.a')))
 def test_preserving_migration_passes(self): self.assertEqual('pass',load_model('conformance/fixtures/migration-preserving/forever').verify_migration('migration.old-to-wasm')['result'])
 def test_violation_fails(self): self.assertEqual('fail',load_model('conformance/fixtures/migration-violating/forever').verify_migration('migration.old-to-wasm')['result'])
