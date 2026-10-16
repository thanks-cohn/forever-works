"""Reproducible local producer lifecycle. No private/production credentials."""
import argparse
import base64
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
ROOT=Path(__file__).resolve().parents[2]
MARKER='forever-works inheritance fixture state\n'
def request(endpoint,path,method='GET',body=None,grant=None,etag=None):
    headers={}
    if grant:headers['Authorization']='Bearer '+grant
    if etag:headers['If-Match']=etag
    req=urllib.request.Request(endpoint+path,data=body,method=method,headers=headers)
    try:
        with urllib.request.urlopen(req,timeout=8) as response:return response.status,dict(response.headers),response.read()
    except urllib.error.HTTPError as e:return e.code,dict(e.headers),e.read()

def main():
    parser=argparse.ArgumentParser();sub=parser.add_subparsers(dest='command',required=True)
    start=sub.add_parser('start');start.add_argument('--state',required=True);start.add_argument('--ready',required=True)
    reset=sub.add_parser('reset');reset.add_argument('--state',required=True)
    seed=sub.add_parser('seed');seed.add_argument('--ready',required=True)
    args=parser.parse_args()
    if args.command=='seed':
        endpoints=json.loads(Path(args.ready).read_text())
        obj=json.dumps({'id':'sample-asset','contentBase64':base64.b64encode(b'synthetic fixture').decode(),'metadata':{'license':'test-only'}}).encode()
        assert request(endpoints['objects'],'/objects/sample-asset','PUT',obj,'objects-write')[0] in (200,201)
        item=b'{"id":"sample-item","assetId":"sample-asset","title":"Synthetic item","tags":["example"],"metadata":{"revision":9007199254740993}}'
        assert request(endpoints['catalog'],'/items/sample-item','PUT',item,'catalog-write','"0"')[0] in (200,201)
        print('Synthetic test state seeded idempotently');return
    state=Path(args.state).resolve();marker=state/'.inheritance-fixture-state'
    if args.command=='reset':
        if not marker.is_file() or marker.read_text()!=MARKER:raise SystemExit('Refusing reset outside a marked fixture state directory')
        for name in ['catalog.sqlite','objects.sqlite']:
            for suffix in ['', '-wal','-shm']:(state/(name+suffix)).unlink(missing_ok=True)
        print('Fixture databases reset; stop producers first');return
    if state.exists() and any(state.iterdir()) and not marker.is_file():raise SystemExit('Choose an empty or previously marked fixture state directory')
    state.mkdir(parents=True,exist_ok=True);marker.write_text(MARKER)
    env={**os.environ,'PYTHONPATH':str(ROOT/'bindings/python')+os.pathsep+os.environ.get('PYTHONPATH','')}
    children=[];endpoints={}
    def stop(*_):raise KeyboardInterrupt()
    signal.signal(signal.SIGTERM,stop)
    try:
        for service in ['catalog','objects']:
            portfile=state/(service+'.port');portfile.unlink(missing_ok=True)
            child=subprocess.Popen([sys.executable,str(Path(__file__).parent/service/'server.py'),'--state',str(state/(service+'.sqlite')),'--port','0','--port-file',str(portfile)],env=env,stdout=subprocess.DEVNULL)
            children.append(child);deadline=time.monotonic()+15
            while not portfile.exists():
                if child.poll() is not None or time.monotonic()>deadline:raise RuntimeError('Producer startup failed: '+service)
                time.sleep(.05)
            endpoints[service]='http://127.0.0.1:'+portfile.read_text()
            assert request(endpoints[service],'/health')[0]==200
        ready=Path(args.ready);temporary=ready.with_suffix('.tmp');temporary.write_bytes((json.dumps(endpoints,indent=2)+'\n').encode());temporary.replace(ready);print(json.dumps(endpoints),flush=True)
        while all(child.poll() is None for child in children):time.sleep(.2)
        raise RuntimeError('Producer exited unexpectedly')
    except KeyboardInterrupt:pass
    finally:
        for child in children:
            if child.poll() is None:child.terminate()
        for child in children:child.wait(timeout=10)
if __name__=='__main__':main()
