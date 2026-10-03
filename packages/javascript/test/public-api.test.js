import assert from "node:assert/strict";
import {test} from "node:test";
import {createForeverApi, ForeverApiError} from "../src/index.js";

const fixture = new URL("../../../conformance/fixtures/complete/forever/", import.meta.url).pathname;

test("Public API discovery and operations are deterministic", async () => {
  const api = await createForeverApi(fixture);
  const description = api.describe();
  assert.equal(description.foreverApiVersion, "0.1");
  assert.deepEqual(description.supportedModelVersions, ["0.1"]);
  assert.deepEqual(description.operations, [...description.operations].sort());
  assert.equal(api.getProjectIntent().kind, "intent");
  assert.deepEqual(api.listCapabilities().map(({id}) => id), [...api.listCapabilities().map(({id}) => id)].sort());
  assert.equal(api.validateModel().valid, true);
  assert.equal(typeof api.normalize(), "string");
});

test("Public API exposes stable machine-readable not-found errors", async () => {
  const api = await createForeverApi(fixture);
  assert.throws(() => api.getEntity("missing.entity"), error => {
    assert.ok(error instanceof ForeverApiError);
    assert.equal(error.code, "entity-not-found");
    assert.deepEqual(error.toJSON(), {error: {code: "entity-not-found", message: "entity not found: missing.entity", details: {id: "missing.entity"}}});
    return true;
  });
  assert.throws(() => api.explainDependency("missing.dependency"), error => error.code === "dependency-not-found");
});
