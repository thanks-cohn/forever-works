// Permanent compatibility regression: old host mode rounds; new interchange preserves.
import assert from 'node:assert/strict';
import {normalize,parseLossless} from '../packages/javascript/src/index.js';
const raw='{\"unknown\":9007199254740993}';
assert.equal(normalize(JSON.parse(raw)),'{\n  "unknown": 9007199254740992\n}\n');
const doc=parseLossless(raw);
assert.equal(doc.source(),raw);
assert.equal(doc.canonical(),'{\n  "unknown": 9007199254740993\n}\n');
console.log('Legacy rounding unchanged; opt-in exact source and decimal-v1 regression passed');
