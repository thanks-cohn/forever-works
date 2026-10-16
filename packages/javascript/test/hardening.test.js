import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {Model,normalize} from '../src/model.js';
import {parseInput} from '../src/json-input.js';
const cases=JSON.parse(await readFile('conformance/hardening/cases.json','utf8'));
test('core adverse corpus is available without Python, native tools, or TypeScript',()=>{
 for(const c of cases) assert.equal(new Model(c.manifest,c.records).validate().length===0,c.valid,c.name);
});
test('canonical bytes match independently reviewed scalar-order golden',async()=>{
 const input=JSON.parse(await readFile('conformance/hardening/normalization.input.json','utf8'));
 assert.equal(normalize(input),await readFile('conformance/hardening/normalization.expected.json','utf8'));
 assert.throws(()=>normalize({x:Infinity}),/unsupported-number/);
 assert.throws(()=>normalize({x:'\ud800'}),/invalid-unicode/);
});
test('bounded parser rejects decoded duplicate members and preserves inert content',()=>{
 assert.throws(()=>parseInput(Buffer.from('{"x":1,"\\u0078":2}')),/duplicate-member/);
 assert.throws(()=>parseInput(Buffer.from('{"x":"\xff"}','latin1')));
 assert.deepEqual(parseInput(Buffer.from('{"command":"never execute","x":null}')),{command:'never execute',x:null});
});
