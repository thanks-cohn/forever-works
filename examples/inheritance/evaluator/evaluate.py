"""Held-out published-obligation cases. Never export this source to the consumer."""
import argparse
import base64
from decimal import Decimal
import hashlib
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import json
from pathlib import Path
import secrets
import subprocess
import sys
import threading
import urllib.error
import urllib.request
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from run import request

def reference_adapter(case):
    """Source-aware fixture driver, explicitly not an independent third product."""
    def put(endpoint,path,body,grant,etag=None):
        for attempt in range(3):
            try:return request(endpoint,path,'PUT',body.encode(),grant,etag)[0]
            except (OSError,urllib.error.URLError):
                if attempt==2:raise
    obj=json.loads(case['objectDocument']);item=json.loads(case['itemDocument'])
    status=put(case['objectEndpoint'],'/objects/'+obj['id'],case['objectDocument'],case['objectGrant'])
    if status not in (200,201):return {'outcome':'denied' if status in (401,403) else 'conflict'}
    status=put(case['catalogEndpoint'],'/items/'+item['id'],case['itemDocument'],case['catalogGrant'],case['catalogETag'])
    return {'outcome':'complete' if status in (200,201) else 'partial','detail':'reference driver only'}

def external_adapter(command=None,url=None):
    def invoke(case):
        if url:
            req=urllib.request.Request(url,data=json.dumps(case).encode(),method='POST',headers={'Content-Type':'application/json'})
            with urllib.request.urlopen(req,timeout=30) as r:value=json.loads(r.read())
        else:
            result=subprocess.run(command,input=json.dumps(case).encode(),capture_output=True,timeout=30,check=True)
            value=json.loads(result.stdout)
        if value.get('outcome') not in ['complete','partial','denied','conflict','unknown']:raise ValueError('invalid adapter result')
        return value
    return invoke

class DropOneResponse:
    """Forward a committed PUT, then lose its response through ordinary network effects."""
    def __init__(self,target,bind='127.0.0.1',advertise='127.0.0.1'):self.target=target;self.dropped=False;self.bind=bind;self.advertise=advertise
    def __enter__(self):
        owner=self
        class Handler(BaseHTTPRequestHandler):
            def log_message(self,*_):pass
            def do_PUT(self):
                body=self.rfile.read(int(self.headers['Content-Length']))
                req=urllib.request.Request(owner.target+self.path,data=body,method='PUT',headers={key:value for key,value in self.headers.items() if key.lower() not in ['host','content-length','connection']})
                try:
                    with urllib.request.urlopen(req,timeout=8) as r:status=r.status;headers=dict(r.headers);data=r.read()
                except urllib.error.HTTPError as e:status=e.code;headers=dict(e.headers);data=e.read()
                if not owner.dropped:owner.dropped=True;self.close_connection=True;return
                self.send_response(status)
                for key,value in headers.items():
                    if key.lower() not in ['connection','server','date']:self.send_header(key,value)
                self.end_headers();self.wfile.write(data)
            def do_GET(self):
                req=urllib.request.Request(owner.target+self.path,headers={'Authorization':self.headers.get('Authorization','')})
                try:
                    with urllib.request.urlopen(req,timeout=8) as r:status=r.status;data=r.read()
                except urllib.error.HTTPError as e:status=e.code;data=e.read()
                self.send_response(status);self.send_header('Content-Length',str(len(data)));self.end_headers();self.wfile.write(data)
        self.server=ThreadingHTTPServer((self.bind,0),Handler);self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        return 'http://'+self.advertise+':'+str(self.server.server_port)
    def __exit__(self,*_):self.server.shutdown();self.server.server_close();self.thread.join(timeout=5)

def evaluate(endpoints,grants,adapter,proxy_bind="127.0.0.1",proxy_host="127.0.0.1"):
    # These values do not appear in public package fixtures; obligations do.
    suffix=secrets.token_hex(5);objid='asset-'+suffix;itemid='item-'+suffix
    content=b'held-out\x00content\xff'+suffix.encode()
    obj=json.dumps({'id':objid,'contentBase64':base64.b64encode(content).decode(),'metadata':{'label':'h\u00e9ld-out','tags':['second','first'],'permissions':['inert assertion']}})
    item='{"id":"'+itemid+'","assetId":"'+objid+'","title":"Held out","tags":["z","a"],"metadata":{"precision":9007199254740993,"decimal":0.10000000000000000001,"claims":[{"status":"pass"}]}}'
    case={'objectEndpoint':endpoints['objects'],'catalogEndpoint':endpoints['catalog'],'objectGrant':grants['objects-write'],'catalogGrant':grants['catalog-write'],'objectDocument':obj,'itemDocument':item,'catalogETag':'"0"'}
    observations=[]
    def get(service,path):return request(endpoints[service],path,grant=grants[service+'-read'])
    def preserved():
        status,headers,data=get('objects','/objects/'+objid);assert status==200 and data.decode()==obj
        assert headers['X-Content-SHA256']==hashlib.sha256(content).hexdigest()
        assert base64.b64decode(json.loads(data)['contentBase64'])==content
        status,headers,data=get('catalog','/items/'+itemid);assert status==200 and data.decode()==item
        assert json.loads(data,parse_float=Decimal)['metadata']['precision']==9007199254740993
        return headers['ETag']
    # Deliberately deny writes first: no state may appear and no default grant may be guessed.
    denied=adapter({**case,'objectGrant':grants['objects-read'],'catalogGrant':grants['catalog-read']})
    assert denied.get('outcome')!='complete'
    assert get('objects','/objects/'+objid)[0]==404 and get('catalog','/items/'+itemid)[0]==404
    observations.append('read-only grants cause no writes')
    with DropOneResponse(endpoints['objects'],proxy_bind,proxy_host) as proxy:
        adapter({**case,'objectEndpoint':proxy})
    etag=preserved();observations.append('lost committed response recovered; both real effects and exact metadata verified')
    adapter(case);assert preserved()==etag;observations.append('byte-identical retry has no extra revision')
    conflict=obj.replace('held-out','changed') if 'held-out' in obj else obj+' '
    adapter({**case,'objectDocument':conflict});assert preserved()==etag
    observations.append('immutable identity conflict preserves original state')
    adapter({**case,'itemDocument':item.replace('Held out','Changed'),'catalogETag':'"0"'})
    assert preserved()==etag;observations.append('stale catalog revision cannot overwrite state')
    # A denied second store may leave an object behind; never invent atomic rollback.
    partial_obj=obj.replace(objid,objid+'-partial');partial_item=item.replace(itemid,itemid+'-partial').replace(objid,objid+'-partial')
    limited={**case,'objectDocument':partial_obj,'itemDocument':partial_item,'catalogGrant':grants['catalog-read']}
    result=adapter(limited);assert result.get('outcome')!='complete'
    assert get('catalog','/items/'+itemid+'-partial')[0]==404
    status,_,data=get('objects','/objects/'+objid+'-partial')
    assert status==404 or (status==200 and data.decode()==partial_obj)
    adapter({**limited,'catalogGrant':grants['catalog-write']})
    assert get('catalog','/items/'+itemid+'-partial')[2].decode()==partial_item
    assert get('objects','/objects/'+objid+'-partial')[2].decode()==partial_obj
    observations.append('partial cross-store denial disclosed; explicit grant recovery preserves identities and data')
    # Round-trip via newly addressed IDs is not allowed to silently replace identity.
    # The exported bytes are returned to an outer controller for a clean-store import.
    return {'checks':observations,'exported':{'objectDocument':obj,'itemDocument':item,'catalogETag':'"0"'},'construction':'NOT_RUN' if adapter is reference_adapter else 'consumer execution; isolation must be separately evidenced'}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--endpoints',required=True);p.add_argument('--grants',required=True)
    choice=p.add_mutually_exclusive_group(required=True);choice.add_argument('--adapter-argv');choice.add_argument('--adapter-url')
    p.add_argument('--clean-endpoints',required=True);p.add_argument('--clean-grants',required=True)
    p.add_argument('--restart-argv',required=True,help='operator-controlled lifecycle hook, never from package content')
    p.add_argument('--proxy-bind',default='127.0.0.1');p.add_argument('--proxy-host',default='127.0.0.1');args=p.parse_args()
    endpoints=json.loads(Path(args.endpoints).read_text());grants=json.loads(Path(args.grants).read_text())
    command=json.loads(Path(args.adapter_argv).read_text()) if args.adapter_argv else None
    adapter=external_adapter(command,args.adapter_url)
    report=evaluate(endpoints,grants,adapter,args.proxy_bind,args.proxy_host)
    exported=report.pop('exported');item=json.loads(exported['itemDocument'])['id'];obj=json.loads(exported['objectDocument'])['id']
    subprocess.run(json.loads(Path(args.restart_argv).read_text()),check=True,timeout=60)
    # Hook returns only after ready; it may update endpoint locations, never identities.
    endpoints=json.loads(Path(args.endpoints).read_text())
    for service,collection,identity,document in [('catalog','items',item,exported['itemDocument']),('objects','objects',obj,exported['objectDocument'])]:
        assert request(endpoints[service],'/'+collection+'/'+identity,grant=grants[service+'-read'])[2].decode()==document
    report['checks'].append('operator restart preserves both original identities/documents')
    clean=json.loads(Path(args.clean_endpoints).read_text());clean_grants=json.loads(Path(args.clean_grants).read_text())
    assert request(clean['catalog'],'/items/'+item,grant=clean_grants['catalog-read'])[0]==404
    assert request(clean['objects'],'/objects/'+obj,grant=clean_grants['objects-read'])[0]==404
    adapter({**exported,'objectEndpoint':clean['objects'],'catalogEndpoint':clean['catalog'],'objectGrant':clean_grants['objects-write'],'catalogGrant':clean_grants['catalog-write']})
    assert request(clean['catalog'],'/items/'+item,grant=clean_grants['catalog-read'])[2].decode()==exported['itemDocument']
    assert request(clean['objects'],'/objects/'+obj,grant=clean_grants['objects-read'])[2].decode()==exported['objectDocument']
    report['checks'].append('clean-store import preserves original identities and exact document bytes')
    report['independence']='NOT_ESTABLISHED by evaluator; require operator access/intervention evidence'
    print(json.dumps(report,indent=2))
