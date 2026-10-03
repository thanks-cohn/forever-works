import test from "node:test";
import assert from "node:assert/strict";
import {execFile} from "node:child_process";
import {mkdtemp, readFile, writeFile} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join, resolve} from "node:path";
import {promisify} from "node:util";

const exec = promisify(execFile);

test("a clean JavaScript consumer imports the packed package without TypeScript", async () => {
  const packageRoot = resolve("packages/javascript");
  const consumer = await mkdtemp(join(tmpdir(), "forever-js-consumer-"));
  const {stdout: packOutput} = await exec("npm", ["pack", "--json", "--pack-destination", consumer], {cwd: packageRoot});
  const [{filename}] = JSON.parse(packOutput);
  await writeFile(join(consumer, "package.json"), JSON.stringify({type: "module", dependencies: {"@forever-works/javascript": `file:./${filename}`}}));
  await exec("npm", ["install", "--ignore-scripts", "--no-audit", "--no-fund"], {cwd: consumer});
  const modelPath = resolve("conformance/fixtures/migration-preserving/forever");
  await writeFile(join(consumer, "proof.js"), `import {loadModel} from "@forever-works/javascript";\nconst m=await loadModel(${JSON.stringify(modelPath)});\nconsole.log(JSON.stringify({valid:m.validate().length===0,explanation:m.explainDependency("dependency.old-streamer").replacementClassification,replacement:m.evaluateReplacement("dependency.old-streamer","implementation.wasm-streamer").result,migration:m.verifyMigration("migration.old-to-wasm").result}));\n`);
  const {stdout} = await exec("node", ["proof.js"], {cwd: consumer});
  assert.deepEqual(JSON.parse(stdout), {valid: true, explanation: "CAPABILITY", replacement: "partial", migration: "pass"});
  assert.ok((await readFile(join(consumer, "proof.js"), "utf8")).includes("loadModel"));
});
