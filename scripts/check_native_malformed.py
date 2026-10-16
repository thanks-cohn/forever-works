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
  result=subprocess.run(['bindings/c/build/probe',str(root)],capture_output=True,check=True)
  assert not json.loads(result.stdout)['valid'],i
print(f'{len(payloads)} deterministic malformed inputs: no sanitizer failure and no false valid result')
