"""Decimal-v1 independent implementation/structural-oracle and native source checks."""
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
sys.path.insert(0,'bindings/python')
from foreverworks import parse_lossless,load_model_lossless,canonical_lossless,JsonNumber
from jsonschema import Draft202012Validator
from referencing import Registry,Resource
ROOT=Path.cwd()
vectors=json.loads(Path('conformance/lossless/numbers.json').read_text(encoding='utf-8'))
def run(args):return subprocess.check_output(args)
modules=[str(ROOT/'packages/javascript/src/index.js'),str(ROOT/'packages/typescript/dist/index.js')]
for module in modules:
 result=json.loads(run(['node','scripts/lossless_probe.mjs',module,'vectors']))
 for v,r in zip(vectors,result):assert r==dict(source=v['token'],canonical=v['canonical']+'\n'),(module,v,r)
for v in vectors:
 d=parse_lossless(v['token']);assert d.source()==v['token'];assert d.canonical()==v['canonical']+'\n'
 assert parse_lossless(d.canonical()).canonical()==d.canonical()
 assert Decimal(v['token'])==Decimal(v['canonical'])
manifest=Path('conformance/lossless/forever/manifest.json').read_text(encoding='utf-8')
record=Path('conformance/lossless/forever/record.json').read_text(encoding='utf-8')
expected=Path('conformance/lossless/model.expected.json').read_bytes()
schemas=[json.loads(p.read_text()) for p in Path('spec/schemas').glob('*.json')]
registry=Registry().with_resources((s['$id'],Resource.from_contents(s)) for s in schemas)
capability=next(s for s in schemas if s.get('properties',{}).get('kind',{}).get('const')=='capability')
def oracle(record):return Draft202012Validator(capability,registry=registry).is_valid(json.loads(record,parse_int=Decimal,parse_float=Decimal))
with tempfile.TemporaryDirectory() as d:
 root=Path(d);(root/'manifest.json').write_bytes(manifest.encode());(root/'record.json').write_bytes(record.encode())
 m=load_model_lossless(root);assert not m.validate();assert m.normalized().encode()==expected
 assert m.source_documents()[0]['document'].source()==manifest
 for module in modules:
  r=json.loads(run(['node','scripts/lossless_probe.mjs',module,str(root)]));assert r['valid'] and r['normalized'].encode()==expected;assert r['sources']==[manifest,record]
 for probe in ['bindings/c/build/probe','bindings/cpp/build/probe']:
  serialized=run([probe,str(root),'serialize','lossless']).decode()
  assert record in serialized
  parsed=json.loads(serialized,parse_int=Decimal,parse_float=Decimal)
  assert parsed=={**json.loads(manifest,parse_int=Decimal,parse_float=Decimal),'records':[json.loads(record,parse_int=Decimal,parse_float=Decimal)]}
 # Exact numeric constraints, including values that legacy binary64 rounds into 0..1.
 for token,valid in [('1',True),('0',True),('0.999999999999999999999999',True),('1e-400',True),('-1e-400',False),('1.000000000000000000000001',False)]:
  raw='{"foreverVersion":"0.1","id":"good","kind":"capability","name":"Good","statement":"Good","provenance":{"sourceType":"explicit","confidence":'+token+'}}'
  assert oracle(raw)==valid
  (root/'record.json').write_bytes(raw.encode())
  assert (not load_model_lossless(root).validate())==valid
  for module in modules:assert json.loads(run(['node','scripts/lossless_probe.mjs',module,str(root)]))['valid']==valid
  for probe in ['bindings/c/build/probe','bindings/cpp/build/probe']:assert json.loads(run([probe,str(root),'lossless']))['valid']==valid
 # Unsupported resource domains fail explicitly, rather than silently projecting.
 for token in ['1e1000001','1e-1000001','11e1000000','1'*4001,'1'+'0'*4096]:
  try:parse_lossless(token)
  except ValueError:pass
  else:raise AssertionError('accepted out-of-domain number')
  raw='{"foreverVersion":"0.1","id":"good","kind":"capability","name":"Good","statement":"Good","future":'+token+'}'
  (root/'record.json').write_bytes(raw.encode())
  for module in modules:assert not json.loads(run(['node','scripts/lossless_probe.mjs',module,str(root)]))['valid']
  for probe in ['bindings/c/build/probe','bindings/cpp/build/probe']:assert not json.loads(run([probe,str(root),'lossless']))['valid']
print(json.dumps({'numericVectors':len(vectors),'exactConstraintCases':6,'domainRejections':5,'canonicalSHA256':hashlib.sha256(expected).hexdigest(),'independent':'Python Decimal + Draft oracle; C exact comparison; JS/TS shared algorithm'},indent=2))
