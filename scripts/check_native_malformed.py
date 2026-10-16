"""Bounded deterministic parser stress; run against the sanitizer probe."""
import json
from pathlib import Path
import random
import subprocess
import tempfile
rng=random.Random(20261016)
with tempfile.TemporaryDirectory() as d:
 root=Path(d);(root/'manifest.json').write_text(json.dumps({'foreverVersion':'0.1','projectId':'stress','records':{'intent':['record.json']}}))
 payloads=[b'{',b'\xff',b'"\\ud800"',b'"\\udfff"',b'[1,]',b'{"a":1,"a":2}',b'{"a":1,"\\u0061":2}',b'['*65+b'0'+b']'*65,b' ' *1048577]
 payloads += [bytes(rng.randrange(256) for _ in range(rng.randrange(0,512))) for _ in range(128)]
 for i,data in enumerate(payloads):
  (root/'record.json').write_bytes(data)
  for mode in [[],['lossless']]:
   result=subprocess.run(['bindings/c/build/probe',str(root),*mode],capture_output=True,check=True)
   assert not json.loads(result.stdout)['valid'],i
 for case in json.loads(Path('conformance/lossless/numbers.json').read_text()):
  raw='{"foreverVersion":"0.1","id":"good","kind":"capability","name":"Good","statement":"Good","future":'+case['token']+'}'
  (root/'record.json').write_bytes(raw.encode())
  result=subprocess.run(['bindings/c/build/probe',str(root),'serialize','lossless'],capture_output=True,check=True)
  assert raw.encode() in result.stdout

 for token,valid in [('0',True),('-0',True),('1e-1000000',True),('-1e-400',False),('1.00000000000000000001',False),('1e1000000',False),('0.'+'9'*4000,True),('1.'+'0'*3998+'1',False)]:
  raw='{"foreverVersion":"0.1","id":"good","kind":"capability","name":"Good","statement":"Good","provenance":{"sourceType":"explicit","confidence":'+token+'}}'
  (root/'record.json').write_bytes(raw.encode())
  result=subprocess.run(['bindings/c/build/probe',str(root),'lossless'],capture_output=True,check=True)
  assert json.loads(result.stdout)['valid']==valid

print(f'{len(payloads)*2} malformed-mode checks and 25 lossless serializations plus 8 exact-constraint cases: no sanitizer failure or false valid result')
