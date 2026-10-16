"""Example HTTP/persistence mechanism, not part of the Forever Works core."""
import argparse
import base64
import binascii
import hashlib
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import json
import re
import sqlite3
from pathlib import Path
from foreverworks import parse_lossless
ID=re.compile(r'[a-z][a-z0-9-]{0,63}\Z')

def serve(service):
    p=argparse.ArgumentParser();p.add_argument('--state',required=True);p.add_argument('--port',type=int,required=True);p.add_argument('--host',default='127.0.0.1');p.add_argument('--port-file');p.add_argument('--read-grant',default=service+'-read');p.add_argument('--write-grant',default=service+'-write');args=p.parse_args()
    path=Path(args.state);path.parent.mkdir(parents=True,exist_ok=True)
    with sqlite3.connect(path) as db:
        db.execute('CREATE TABLE IF NOT EXISTS entries(id TEXT PRIMARY KEY, revision INTEGER NOT NULL, document TEXT NOT NULL, digest TEXT)')
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*_):pass
        def respond(self,status,value=None,raw=None,revision=None,digest=None):
            data=raw.encode('utf-8') if raw is not None else json.dumps(value,separators=(',',':'),ensure_ascii=False).encode('utf-8')
            self.send_response(status);self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Content-Length',str(len(data)))
            if revision is not None:self.send_header('ETag',f'"{revision}"')
            if digest:self.send_header('X-Content-SHA256',digest)
            self.end_headers()
            try:self.wfile.write(data)
            except (BrokenPipeError,ConnectionResetError):pass # Commit may already have happened; callers retry by contract.
        def error(self,status,code):self.respond(status,{'error':{'code':code}})
        def auth(self,write=False):
            grant=self.headers.get('Authorization','')
            if grant not in {'Bearer '+args.read_grant,'Bearer '+args.write_grant}:self.error(401,'unauthorized');return False
            if write and grant!='Bearer '+args.write_grant:self.error(403,'forbidden');return False
            return True
        def route(self):
            prefix='/items/' if service=='catalog' else '/objects/'
            value=self.path[len(prefix):] if self.path.startswith(prefix) else ''
            return value if ID.fullmatch(value) else None
        def do_GET(self):
            if self.path=='/health':self.respond(200,{'service':service,'version':'1'});return
            if not self.auth():return
            listing='/items' if service=='catalog' else '/objects'
            with sqlite3.connect(path) as db:
                if self.path==listing:self.respond(200,{'ids':[r[0] for r in db.execute('SELECT id FROM entries ORDER BY id')]});return
                identity=self.route()
                if identity is None:self.error(404,'not-found');return
                row=db.execute('SELECT revision,document,digest FROM entries WHERE id=?',(identity,)).fetchone()
            if row is None:self.error(404,'not-found');return
            self.respond(200,raw=row[1],revision=row[0],digest=row[2])
        def do_PUT(self):
            if not self.auth(True):return
            identity=self.route()
            if identity is None:self.error(404,'not-found');return
            try:
                length=int(self.headers.get('Content-Length','-1'))
                if length<0 or length>131072:self.error(413,'body-limit');return
                self.connection.settimeout(5)
                raw=self.rfile.read(length)
                if len(raw)!=length:self.error(400,'incomplete-body');return
                document=parse_lossless(raw);value=document.value
                if not isinstance(value,dict) or value.get('id')!=identity:raise ValueError('id')
                digest=None
                if service=='catalog':
                    if not isinstance(value.get('title'),str) or not isinstance(value.get('assetId'),str) or not ID.fullmatch(value['assetId']):raise ValueError('catalog fields')
                    if not isinstance(value.get('tags'),list) or any(not isinstance(t,str) for t in value['tags']):raise ValueError('tags')
                else:
                    if not isinstance(value.get('contentBase64'),str):raise ValueError('content')
                    content=base64.b64decode(value['contentBase64'],validate=True)
                    if base64.b64encode(content).decode('ascii')!=value['contentBase64']:raise ValueError('noncanonical Base64')
                    if len(content)>65536:self.error(413,'content-limit');return
                    digest=hashlib.sha256(content).hexdigest()
            except (ValueError,UnicodeError,TypeError,binascii.Error):self.error(400,'invalid-document');return
            except (TimeoutError,OSError):self.error(400,'incomplete-body');return
            text=document.source()
            try:
                with sqlite3.connect(path,timeout=5) as db:
                    db.execute('PRAGMA synchronous=FULL');db.execute('BEGIN IMMEDIATE')
                    old=db.execute('SELECT revision,document,digest FROM entries WHERE id=?',(identity,)).fetchone()
                    if old and old[1]==text:
                        # Byte-identical retry has no extra effect, including after a lost response.
                        revision=old[0];status=200
                    elif service=='objects' and old:self.error(409,'identity-conflict');return
                    elif service=='catalog' and self.headers.get('If-Match')!=f'"{old[0] if old else 0}"':self.error(412,'revision-conflict');return
                    else:
                        revision=old[0]+1 if old else 1;status=200 if old else 201
                        db.execute('INSERT INTO entries VALUES(?,?,?,?) ON CONFLICT(id) DO UPDATE SET revision=excluded.revision,document=excluded.document,digest=excluded.digest',(identity,revision,text,digest))
                self.respond(status,{'id':identity,'revision':revision},revision=revision,digest=digest)
            except sqlite3.OperationalError:self.error(503,'store-busy')
    server=ThreadingHTTPServer((args.host,args.port),Handler)
    if args.port_file:
        portfile=Path(args.port_file);temporary=portfile.with_suffix('.tmp');temporary.write_bytes(str(server.server_port).encode());temporary.replace(portfile)
    print(json.dumps({'service':service,'port':server.server_port}),flush=True)
    server.serve_forever()
