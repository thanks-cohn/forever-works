import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile,mkdtemp,writeFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {parseLossless,JsonNumber,canonicalLossless,loadModelLossless,loadModel,normalize} from '../src/index.js';
const vectors=JSON.parse(await readFile('conformance/lossless/numbers.json','utf8'));
test('exact decimal vectors preserve source and canonical mathematical value',()=>{
  for(const {token,canonical} of vectors){const raw=` {"n":${token},"array":[${token},null],"__proto__":{"kept":true}}\n`;const d=parseLossless(raw);assert.equal(d.source(),raw);assert.equal(d.value.n.token,token);assert.equal(d.value.n.canonical(),canonical);assert.equal(parseLossless(d.canonical()).canonical(),d.canonical());assert.equal(d.value.__proto__.kept,true);assert.ok(Object.isFrozen(d.value));}
});
test('legacy rounding is retained; additive interchange fixes the exact regression',()=>{
  const raw='{"unknown":9007199254740993}';
  assert.equal(normalize(JSON.parse(raw)),'{\n  "unknown": 9007199254740992\n}\n');
  const d=parseLossless(raw);assert.equal(d.canonical(),'{\n  "unknown": 9007199254740993\n}\n');
  assert.throws(()=>d.toHost(),/lossy-number-projection/);assert.equal(d.toHost({allowLoss:true}).unknown,9007199254740992);
  assert.throws(()=>canonicalLossless({n:9007199254740993}),/unsafe-host-number/);
  assert.equal(parseLossless(JSON.stringify({n:9007199254740993})).value.n.token,'9007199254740992'); // Input was rounded before ingestion; do not invent precision.
  assert.throws(()=>JSON.stringify(d.value),/lossless-writer-required/);
  assert.throws(()=>+d.value.unknown,/explicit-number-projection-required/);
});
test('explicit resource, Unicode, duplicate and syntax failures do not round',()=>{
  for(const raw of ['1e1000001','1e-1000001','11e1000000','1'.repeat(4001),'1'+'0'.repeat(4096),'['.repeat(66)+'0'+']'.repeat(66)])assert.throws(()=>parseLossless(raw),/resource-limit/);
  for(const raw of ['NaN','Infinity','01','[1,]','{"x":1,"\\u0078":2}','"\\ud800"'])assert.throws(()=>parseLossless(raw));
  assert.throws(()=>parseLossless(new Uint8Array([255])));
  assert.equal(parseLossless('0.1').toHost(),0.1);
  assert.throws(()=>parseLossless('1e400').toHost({allowLoss:true}),/unsupported-host-number/);
});
test('model lossless loading checks confidence exactly and preserves all documents',async()=>{
  const root=await mkdtemp(join(tmpdir(),'fw-numbers-'));
  const manifest='{ "foreverVersion":"0.1","projectId":"numbers","future":9007199254740993,"records":{"capabilities":["record.json"]}}';
  await writeFile(join(root,'manifest.json'),manifest);
  const record=confidence=>`{"foreverVersion":"0.1","id":"good","kind":"capability","name":"Good","statement":"Good","provenance":{"sourceType":"explicit","confidence":${confidence}},"future":1e400}`;
  await writeFile(join(root,'record.json'),record('1.0000000000000000000000001'));
  let m=await loadModelLossless(root);assert.ok(m.validate().some(e=>e.path.endsWith('.confidence')&&e.code==='invalid-value'));
  await writeFile(join(root,'record.json'),record('0.9999999999999999999999999'));
  m=await loadModelLossless(root);assert.deepEqual(m.validate(),[]);assert.ok(m.normalized().includes('9007199254740993'));assert.ok(m.normalized().includes('1e400'));
  assert.equal(m.sourceDocuments()[0].document.source(),manifest);
  assert.equal(m.getEntity('good').future.token,'1e400');
  await assert.rejects(loadModel(root)); // Legacy finite-host policy remains unchanged.
});
