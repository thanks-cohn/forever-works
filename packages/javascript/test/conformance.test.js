import test from "node:test";
import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import {loadModel, normalize} from "../src/index.js";

test("shared case catalog", async t => {
  const {cases} = JSON.parse(await readFile("conformance/fixtures/cases.json", "utf8"));
  for (const entry of cases) await t.test(entry.name, async () => {
    const model = await loadModel(`conformance/fixtures/${entry.name}/forever`);
    const issues = model.validate();
    assert.equal(issues.length === 0, entry.valid, normalize(issues));
    if (entry.error) assert.ok(issues.some(issue => issue.code === entry.error));
  });
});

test("normalization and evaluations equal canonical goldens", async () => {
  for (const name of ["minimal", "complete"]) {
    const expected = await readFile(`conformance/expected/${name}.normalized.json`, "utf8");
    assert.equal((await loadModel(`conformance/fixtures/${name}/forever`)).normalized(), expected);
  }
  const complete = await loadModel("conformance/fixtures/complete/forever");
  assert.equal(normalize(complete.evaluateReplacement("dependency.old-streamer", "implementation.wasm-streamer")), await readFile("conformance/expected/replacement.json", "utf8"));
  for (const name of ["migration-preserving", "migration-violating"]) {
    const model = await loadModel(`conformance/fixtures/${name}/forever`);
    assert.equal(normalize(model.verifyMigration("migration.old-to-wasm")), await readFile(`conformance/expected/${name}.json`, "utf8"));
  }
});
