import {loadModel} from "@forever-works/javascript";

const model = await loadModel("../../conformance/fixtures/complete/forever");
const intent = model.getEntity("intent.remote-transfer");
const dependency = model.explainDependency("dependency.old-streamer");
const replacement = model.evaluateReplacement("dependency.old-streamer", "implementation.wasm-streamer");
const migration = model.verifyMigration("migration.old-to-wasm");

console.log(JSON.stringify({
  intent: intent.statement,
  capabilities: dependency.requiredCapabilities,
  invariants: dependency.protectedInvariants,
  implementation: dependency.id,
  replacement,
  migration
}, null, 2));
