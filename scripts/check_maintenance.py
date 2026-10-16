"""Check only explicitly recorded artifact bytes; existence is not semantic freshness."""
import argparse
import hashlib
import json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--root',default='.');args=p.parse_args()
root=Path(args.root).resolve()
evidence=json.loads((root/'docs/RESEARCH/evidence/lossless/maintenance-artifacts.json').read_text())
stale=[]
for item in evidence['artifacts']:
 relative=Path(item['path']);target=(root/relative).resolve()
 if relative.is_absolute() or root not in target.parents:raise ValueError('artifact path outside root')
 if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest()!=item['sha256']:stale.append(item['path'])
print(json.dumps({'valid':not stale,'staleArtifacts':stale,'scope':'recorded byte identity only; not semantic freshness or executed verification'},indent=2))
raise SystemExit(bool(stale))
