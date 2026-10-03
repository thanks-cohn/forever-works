import test from "node:test";
import assert from "node:assert/strict";
import {mkdtemp, mkdir, writeFile} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join} from "node:path";
import {Model, loadModel} from "../src/index.js";

const fixture = name => `conformance/fixtures/${name}/forever`;

test("loads, validates, queries, traces cycles, and audits", async () => {
  const model = await loadModel(fixture("complete"));
  assert.deepEqual(model.validate(), []);
  assert.equal(model.getEntity("dependency.old-streamer").kind, "dependency");
  assert.deepEqual(model.list("capability").map(record => record.id), ["capability.resumability", "capability.streaming"]);
  assert.equal(model.explainDependency("dependency.old-streamer").replacementClassification, "CAPABILITY");
  assert.deepEqual(model.findDependencies("CAPABILITY").map(record => record.id), ["dependency.old-streamer"]);
  assert.ok(model.traceEntity("dependency.old-streamer").some(record => record.id === "intent.remote-transfer"));
  assert.equal(model.audit().some(issue => issue.code === "broken-reference"), false);
  const circular = await loadModel(fixture("circular-relationship"));
  assert.deepEqual(circular.traceEntity("capability.a").map(record => record.id), ["capability.a", "capability.b"]);
});

test("normalizes deterministically and preserves unknown fields", async () => {
  const model = await loadModel(fixture("unknown-future-field"));
  assert.deepEqual(model.validate(), []);
  assert.equal(model.normalized(), model.normalized());
  assert.match(model.normalized(), /futureField/);
});

test("replacement aggregation preserves fail, pass, unknown, and partial", () => {
  const manifest = {foreverVersion: "0.1", projectId: "states"};
  const dependency = {foreverVersion: "0.1", id: "dependency.x", kind: "dependency", dependencyName: "x", dependencyType: "library", purpose: "test", reasonSelected: "test", replacementClassification: "CAPABILITY", requiredCapabilities: ["capability.a", "capability.b"]};
  const candidate = claims => ({foreverVersion: "0.1", id: "implementation.x", kind: "implementation", type: "library", technology: "x", satisfiesCapabilities: [], claims});
  const evaluate = claims => new Model(manifest, [dependency, candidate(claims)]).evaluateReplacement("dependency.x", "implementation.x");
  assert.equal(evaluate([{requirement: "capability.a", status: "pass"}, {requirement: "capability.b", status: "pass"}]).result, "pass");
  assert.equal(evaluate([{requirement: "capability.a", status: "pass"}, {requirement: "capability.b", status: "fail"}]).result, "fail");
  const partial = evaluate([{requirement: "capability.a", status: "pass"}]);
  assert.equal(partial.result, "partial");
  assert.equal(partial.checks[1].status, "unknown");
});

test("replacement and migration match shared goldens", async () => {
  const complete = await loadModel(fixture("complete"));
  assert.equal(complete.evaluateReplacement("dependency.old-streamer", "implementation.wasm-streamer").result, "partial");
  assert.equal(complete.verifyMigration("migration.old-to-wasm").result, "partial");
  assert.equal((await loadModel(fixture("migration-preserving"))).verifyMigration("migration.old-to-wasm").result, "pass");
  assert.equal((await loadModel(fixture("migration-violating"))).verifyMigration("migration.old-to-wasm").result, "fail");
});

test("reports malformed records and rejects escaping paths", async () => {
  const malformed = new Model({foreverVersion: "0.1"}, [null, {foreverVersion: "0.1", kind: "dependency", replacementClassification: "INVALID"}]);
  assert.ok(malformed.validate().some(issue => issue.code === "invalid-record"));
  assert.ok(malformed.validate().some(issue => issue.code === "invalid-classification"));
  const root = await mkdtemp(join(tmpdir(), "forever-js-path-"));
  await mkdir(join(root, "forever"));
  await writeFile(join(root, "outside.json"), "{}");
  await writeFile(join(root, "forever", "manifest.json"), JSON.stringify({foreverVersion: "0.1", projectId: "x", records: {intent: ["../outside.json"]}}));
  await assert.rejects(loadModel(join(root, "forever")), /escapes model root/);
});
