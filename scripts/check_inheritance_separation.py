"""Source-aware container-boundary smoke, not a fresh-agent construction trial."""
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
BASE=Path('examples/inheritance').resolve()
project='fw-proof-smoke-'+secrets.token_hex(4)
env={**os.environ,**{name:secrets.token_hex(20) for name in ['CATALOG_READ_GRANT','CATALOG_WRITE_GRANT','OBJECTS_READ_GRANT','OBJECTS_WRITE_GRANT']}}
# Explicit daemon selection; preserve inherited proxy/config/credentials.
for name in ['DOCKER_HOST','DOCKER_CONTEXT','DOCKER_TLS','DOCKER_TLS_VERIFY','DOCKER_CERT_PATH']:env.pop(name,None)
command=['docker','--host=unix:///var/run/docker.sock','compose','-f',str(BASE/'compose.yaml'),'-p',project,'--profile','evaluation']
def run(args,**kwargs):return subprocess.run([*command,*args],env=env,check=True,**kwargs)
try:
 run(['up','-d','--build'],stdout=sys.stderr)
 script="""import hashlib,json,pathlib,socket,time,urllib.request,sys,sqlite3
print(json.dumps({'python':sys.version.split()[0],'sqlite':sqlite3.sqlite_version}))
p=pathlib.Path('/packages');index=json.loads((p/'index.json').read_text())
for product,digest in index['packages'].items():
 r=p/product;raw=(r/'package.json').read_bytes();assert hashlib.sha256(raw).hexdigest()==digest
 manifest=json.loads(raw)
 for name,h in manifest['files'].items():assert hashlib.sha256((r/name).read_bytes()).hexdigest()==h
for forbidden in ['/workspace','/app','/evaluator','/var/run/docker.sock']:assert not pathlib.Path(forbidden).exists(),forbidden
try:(p/'unauthorized.txt').write_text('no')
except OSError:pass
else:raise AssertionError('packages writable')
pathlib.Path('/consumer/output.txt').write_text('isolated workspace works')
for host in ['catalog','objects','catalog-clean','objects-clean']:
 for attempt in range(50):
  try:
   with urllib.request.urlopen('http://'+host+':8080/health',timeout=1) as r:assert r.status==200
   break
  except OSError:
   if attempt==49:raise
   time.sleep(.1)
try:s=socket.create_connection(('1.1.1.1',443),timeout=1)
except OSError:pass
else:s.close();raise AssertionError('undeclared external route available')
print('package hashes, source/evaluator absence, read-only input, writable output, both reference services and external-route denial passed')
"""
 run(['exec','-T','consumer','python','-I','-c',script])
 print(json.dumps({'containerBoundarySmoke':'PASS','construction':'NOT_RUN','limitation':'Fresh agent tool/connector restrictions must also be enforced by operator'}))
finally:run(['down','--volumes','--remove-orphans','--rmi','local'],stdout=sys.stderr)
