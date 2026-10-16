"""Executed source-aware producer/harness checks, not cold construction evidence."""
import hashlib
import json
import os
from pathlib import Path
import secrets
import shutil
import subprocess
import sys
import tempfile
import threading
import time
ROOT=Path(__file__).resolve().parents[2]
BASE=Path(__file__).resolve().parent
sys.path.insert(0,str(BASE));sys.path.insert(0,str(BASE/'evaluator'))
from run import request
from evaluate import evaluate,reference_adapter
from export_packages import export,validate
ENV={**os.environ,'PYTHONPATH':str(ROOT/'bindings/python')+os.pathsep+os.environ.get('PYTHONPATH','')}
class Producers:
    def __init__(self,root):
        self.root=root;self.endpoints={};self.children={};self.grants={role:secrets.token_hex(20) for role in ['catalog-read','catalog-write','objects-read','objects-write']}
    def start(self,service):
        self.root.mkdir(parents=True,exist_ok=True);port=self.root/(service+'.port');port.unlink(missing_ok=True)
        command=[sys.executable,str(BASE/service/'server.py'),'--state',str(self.root/(service+'.sqlite')),'--port','0','--port-file',str(port),'--read-grant',self.grants[service+'-read'],'--write-grant',self.grants[service+'-write']]
        child=subprocess.Popen(command,env=ENV,stdout=subprocess.DEVNULL);self.children[service]=child;deadline=time.monotonic()+15
        while not port.exists():
            if child.poll() is not None or time.monotonic()>deadline:raise RuntimeError('producer failed to start')
            time.sleep(.05)
        self.endpoints[service]='http://127.0.0.1:'+port.read_text()
    def __enter__(self):
        self.start('catalog');self.start('objects');return self
    def restart(self,service):self.children[service].terminate();self.children[service].wait(timeout=10);self.start(service)
    def __exit__(self,*_):
        for child in self.children.values():
            if child.poll() is None:child.terminate()
        for child in self.children.values():child.wait(timeout=10)

def main():
    with tempfile.TemporaryDirectory() as d:
        root=Path(d)
        with Producers(root/'primary') as producers:
            report=evaluate(producers.endpoints,producers.grants,reference_adapter)
            exported=report.pop('exported');identity=json.loads(exported['itemDocument'])['id'];asset=json.loads(exported['objectDocument'])['id']
            for service in ['catalog','objects']:producers.restart(service)
            assert request(producers.endpoints['catalog'],'/items/'+identity,grant=producers.grants['catalog-read'])[2].decode()==exported['itemDocument']
            assert request(producers.endpoints['objects'],'/objects/'+asset,grant=producers.grants['objects-read'])[2].decode()==exported['objectDocument']
            report['checks'].append('independent producer restarts preserve committed identities/data')
            assert request(producers.endpoints['catalog'],'/items',grant=producers.grants['objects-write'])[0]==401
            for service,collection in [('catalog','items'),('objects','objects')]:
                assert request(producers.endpoints[service],'/'+collection,grant=producers.grants[service+'-read'])[0]==200
            # Canonical base64 and duplicate-member errors are independently observable.
            bad=b'{"id":"bad","contentBase64":"Zh=="}'
            assert request(producers.endpoints['objects'],'/objects/bad','PUT',bad,producers.grants['objects-write'])[0]==400
            bad=b'{"id":"bad","id":"bad","contentBase64":"Zg=="}'
            assert request(producers.endpoints['objects'],'/objects/bad','PUT',bad,producers.grants['objects-write'])[0]==400
            report['checks'].append('cross-service grant rejected; invalid Base64/duplicate members rejected')
        # Clean-store round trip retains identities, exact metadata, content and ownership.
        with Producers(root/'fresh') as fresh:
            case={**exported,'objectEndpoint':fresh.endpoints['objects'],'catalogEndpoint':fresh.endpoints['catalog'],'objectGrant':fresh.grants['objects-write'],'catalogGrant':fresh.grants['catalog-write']}
            assert reference_adapter(case)['outcome']=='complete'
            assert request(fresh.endpoints['catalog'],'/items/'+identity,grant=fresh.grants['catalog-read'])[2].decode()==exported['itemDocument']
            assert request(fresh.endpoints['objects'],'/objects/'+asset,grant=fresh.grants['objects-read'])[2].decode()==exported['objectDocument']
        report['checks'].append('clean-store round trip preserves both identities and all document bytes')
        # Exercise the delivered external evaluator CLI with a clearly source-aware fixture adapter.
        # This verifies stdin/result/lifecycle plumbing, not independent construction.
        with Producers(root/'external-primary') as primary, Producers(root/'external-clean') as clean:
            control=root/'control';control.mkdir();endpoints=control/'endpoints.json';endpoints.write_text(json.dumps(primary.endpoints))
            for name,value in [('grants',primary.grants),('clean-endpoints',clean.endpoints),('clean-grants',clean.grants)]: (control/(name+'.json')).write_text(json.dumps(value))
            driver=control/'reference_driver.py'
            driver.write_text('import sys,json\nsys.path.insert(0,'+repr(str(BASE/'evaluator'))+')\nfrom evaluate import reference_adapter\nprint(json.dumps(reference_adapter(json.load(sys.stdin))))\n')
            (control/'adapter.json').write_text(json.dumps([sys.executable,str(driver)]))
            hook=control/'trusted_hook.py';requested=control/'restart-request';completed=control/'restart-complete'
            hook.write_text('import pathlib,time\np=pathlib.Path('+repr(str(requested))+');p.write_text("request")\ndeadline=time.monotonic()+15\nwhile not pathlib.Path('+repr(str(completed))+').exists():\n if time.monotonic()>deadline:raise RuntimeError("restart timeout")\n time.sleep(.05)\n')
            (control/'hook.json').write_text(json.dumps([sys.executable,str(hook)]))
            stop=threading.Event();errors=[]
            def restart_control():
                try:
                    while not requested.exists():
                        if stop.wait(.05):return
                    primary.restart('catalog');primary.restart('objects');endpoints.write_text(json.dumps(primary.endpoints));completed.write_text('ready')
                except Exception as e:errors.append(e)
            thread=threading.Thread(target=restart_control);thread.start()
            try:
                command=[sys.executable,str(BASE/'evaluator/evaluate.py'),'--endpoints',str(endpoints),'--grants',str(control/'grants.json'),'--adapter-argv',str(control/'adapter.json'),'--clean-endpoints',str(control/'clean-endpoints.json'),'--clean-grants',str(control/'clean-grants.json'),'--restart-argv',str(control/'hook.json')]
                result=subprocess.run(command,check=True,capture_output=True,text=True,env=ENV,timeout=45)
                assert 'clean-store import' in result.stdout
            finally:stop.set();thread.join(timeout=10)
            assert not errors,errors
        report['checks'].append('external evaluator CLI, trusted restart hook and clean-store import passed with source-aware fixture adapter')
        # Real CLI lifecycle, synthetic setup and safe bounded reset.
        state=root/'cli-state';ready=root/'ready.json'
        child=subprocess.Popen([sys.executable,str(BASE/'run.py'),'start','--state',str(state),'--ready',str(ready)],env=ENV,stdout=subprocess.DEVNULL)
        try:
            deadline=time.monotonic()+15
            while not ready.exists():
                if child.poll() is not None or time.monotonic()>deadline:raise RuntimeError('CLI startup failed')
                time.sleep(.05)
            for _ in range(2):subprocess.run([sys.executable,str(BASE/'run.py'),'seed','--ready',str(ready)],check=True,capture_output=True,env=ENV)
        finally:child.terminate();child.wait(timeout=10)
        subprocess.run([sys.executable,str(BASE/'run.py'),'reset','--state',str(state)],check=True,capture_output=True,env=ENV)
        assert not (state/'catalog.sqlite').exists() and not (state/'objects.sqlite').exists()
        report['checks'].append('documented startup, idempotent seed and marked-state reset passed')
        # Record only observed reference scope; independent construction remains NOT_RUN.
        for product in ['catalog','objects']:
            evidence={'referenceProducerTests':'PASS','checks':report['checks'],'sourceAware':True,'construction':'NOT_RUN','limitations':['not an independent consumer','not production authentication','no commercial evidence']}
            (BASE/'public'/product/'producer-evidence.json').write_bytes((json.dumps(evidence,indent=2)+'\n').encode())
        export(root/'exports')
        for product in ['catalog','objects']:
            package=root/'exports'/product;assert validate(package)['construction']=='NOT_RUN'
            # A fresh stdlib process consumes only copied package files. This is a smoke, not agent isolation.
            consumer=root/'consumer'/product;shutil.copytree(package,consumer)
            script="""import hashlib,json,pathlib
r=pathlib.Path('.');p=json.loads((r/'package.json').read_text());assert p['experimentalPackageVersion']=='1'
for n,h in p['files'].items():assert hashlib.sha256((r/n).read_bytes()).hexdigest()==h
m=json.loads((r/'forever/manifest.json').read_text());records=[json.loads((r/'forever'/n).read_text()) for a in m['records'].values() for n in a]
assert any(x['kind']=='intent' for x in records) and any(x['kind']=='invariant' for x in records)
print('clean package smoke passed; sufficiency UNKNOWN')
"""
            result=subprocess.run([sys.executable,'-I','-c',script],cwd=consumer,check=True,capture_output=True,text=True)
            assert 'clean package smoke passed' in result.stdout
            # Tamper and unintended material must fail, not be silently trusted/exported.
            target=consumer/'CONTRACT.md';target.write_bytes(target.read_bytes()+b'\n')
            try:validate(consumer)
            except ValueError:pass
            else:raise AssertionError('tampering accepted')
        (BASE/'public/catalog/unintended.py').write_text('raise RuntimeError("must never export")')
        try:
            try:export(root/'unintended')
            except ValueError:pass
            else:raise AssertionError('unintended source accepted')
        finally:(BASE/'public/catalog/unintended.py').unlink()
        report['checks'].append('allowlisted export, integrity/model/link validation, clean stdlib consumption and tamper/source rejection passed')
        print(json.dumps(report,indent=2))
if __name__=='__main__':main()
