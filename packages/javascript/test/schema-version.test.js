import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile, readdir} from 'node:fs/promises';

test('published record schema version patterns accept documented and old model versions', async () => {
  let count = 0;
  for (const path of await readdir('spec/schemas')) {
    const schema = JSON.parse(await readFile(`spec/schemas/${path}`, 'utf8'));
    const pattern = schema.properties?.foreverVersion?.pattern;
    if (!pattern) continue;
    const regex = new RegExp(pattern);
    assert.equal(regex.test('0.1'), true, path);
    assert.equal(regex.test('0.0'), true, path);
    assert.equal(regex.test('1.0'), false, path);
    assert.equal(regex.test('0x1'), false, path);
    assert.equal(regex.test('0\\x1'), false, path);
    count++;
  }
  assert.equal(count, 10);
});
