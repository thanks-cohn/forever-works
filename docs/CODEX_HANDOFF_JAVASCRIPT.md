# Codex handoff: JavaScript first-class target

**Date:** 2026-10-03  
**Implementation baseline commit:** `5338356ff23d568d5e0ac8672ec8ad6bac5a5017`  
**Handoff status:** coherent JavaScript foundation implemented and verified; CLI and some fixture expansion remain follow-up work.

## Branch and execution record

The checkout initially exposed its sole current branch under the environment name `work`, at request commit `d69510e8d12b7935f69366074845faf95fccf822`. The existing branch was renamed in place to `main`; no branch was created and no branch checkout/switch occurred. The implementation commit above and this handoff are committed directly on `main`. The SHA above is the latest `main` implementation commit immediately before the handoff-only commit; the handoff commit itself necessarily receives its SHA only after this file is written.

## Completed work

### Architecture and package

* Added `packages/javascript`, a zero-runtime-dependency ESM package authored entirely as `.js`. It does not import TypeScript source or compiled TypeScript output.
* Split the binding into a host-neutral `Model`/`normalize` semantic core and a Node filesystem adapter. Consumers that already have parsed JSON can import `@forever-works/javascript/core`; the main entry point also exposes safe filesystem loading.
* Added explicit package exports, Node 20 engine metadata, JSDoc on public entry points, and an independently packable package identity.
* Preserved unknown fields by retaining input records and recursively normalizing all JSON properties.

### Public JavaScript API

* `new Model(manifest, records)` for already-parsed JSON.
* `loadModel(path)` for Node filesystem loading with model-root escape rejection.
* `normalize(value)` for canonical sorted-key, two-space, trailing-newline JSON.
* `Model.validate()`, `getEntity()`, `list()`, `traceEntity()`, `explainDependency()`, `findDependencies()`, `audit()`, `normalized()`, `evaluateReplacement()`, and `verifyMigration()`.
* Replacement and migration aggregation implements normative `pass` / `fail` / `unknown` checks and `pass` / `fail` / `partial` overall results. Migration passes require referenced verification evidence.

### Independent evidence

* Added direct `node:test` coverage for validation, sorted lookup, cycle-safe tracing, auditing, deterministic normalization, unknown-field preservation, malformed records, missing evidence, all-pass/fail/partial aggregation, migration outcomes, and filesystem traversal rejection.
* Added a JavaScript conformance test over the complete shared case catalog and the canonical normalization, replacement, and migration goldens.
* Added a realistic clean-consumer test. It runs `npm pack`, installs the tarball in a temporary plain-JavaScript project, imports the public package, loads a shared complete fixture, then validates, explains, evaluates replacement, and verifies migration. It invokes no TypeScript compiler.
* Added `make test-javascript`, included it in `make test`, added JavaScript to cross-language golden normalization, and added a separately attributable JavaScript CI job.

### Example, documentation, and self-hosting

* Added `examples/javascript`, containing only JavaScript and package metadata, to demonstrate intent → capabilities/invariants → implementation/dependency → replacement → migration.
* Updated the README, binding documentation, conformance documentation, and roadmap to distinguish the canonical standard, JavaScript proof binding, and TypeScript proof binding.
* Added explicit self-hosted decision, invariant, and implementation records. These record that JavaScript evidence is independent, plain-JavaScript consumers need no TypeScript compiler, and the canonical standard remains language-neutral.

## Verification performed

* `make test-javascript` — passed: 18 tests, including 10 shared catalog subtests, golden comparisons, security behavior, and clean package consumption.
* `git diff --check` — passed before the implementation commit.
* Initial `make test` — JavaScript and Python passed, then TypeScript setup failed because checkout dependencies were not installed (`@types/node` unavailable).
* `npm install && make test` — passed after installing declared development dependencies: Python (6 tests), JavaScript (18 tests), TypeScript (2 tests), C smoke conformance, C++ wrapper smoke conformance, and cross-language golden normalization including JavaScript.

No test result is inferred from the TypeScript lane; JavaScript runs before TypeScript and directly executes its `.js` sources.

## Acceptance criteria

1. **Complete:** A plain JavaScript consumer can install and use the packed artifact without TypeScript or `tsc`.
2. **Complete:** The runtime-visible proof surface is independently authored JavaScript and does not import the TypeScript implementation.
3. **Complete:** Dedicated JavaScript tests cover core success, conservative evaluation, malformed data, cycles, unknown fields, and path security.
4. **Complete:** Dedicated JavaScript conformance consumes the shared catalog and canonical normalization/evaluation goldens.
5. **Complete:** A plain-JavaScript end-to-end example exists.
6. **Complete:** JavaScript has explicit Makefile and independently attributable CI targets.
7. **Complete:** README, roadmap, conformance, and language-binding documentation describe JavaScript as a first-class proof target.
8. **Complete:** The self-hosted model records the decision, invariant, implementation, provenance, and verification command.
9. **Complete for the current suite:** Existing Python, TypeScript, C, C++, and cross-language checks pass.
10. **Complete:** No canonical standard/schema semantics were made JavaScript-specific.

## Partial, deferred, and unverified

* **Deferred:** A dedicated JavaScript CLI adapter. The request made this conditional when it can be added cleanly; the library proof was prioritized. The existing portable CLI remains unchanged.
* **Partial:** The case catalog lacks explicit standalone cases named for duplicate IDs and invalid dependency classification. JavaScript validates both behaviors (invalid classification is exercised in its direct tests), but shared fixtures should be added for binding-wide conformance. This run did not change canonical fixture semantics merely to increase count.
* **Partial:** The root package entry includes the Node adapter. The host-neutral core is separately exported at `@forever-works/javascript/core`, but browser/Deno/Bun consumer smoke tests are not yet present.
* **Deferred:** CommonJS compatibility; ESM is the requested primary format and avoids duplicated semantics.
* **Unverified:** Publishing to an external npm registry. Local tarball construction and clean installation passed.
* **Unverified:** CI execution on GitHub Actions itself; the workflow was updated and equivalent commands passed locally.

## Exact continuation point

Start by adding canonical shared fixtures for `invalid-duplicate-id` and `invalid-dependency-classification` to `conformance/fixtures/cases.json`, then make every full-surface binding assert their stable error codes. Next, add a small `packages/javascript/bin/forever.js` CLI that delegates exclusively to the JavaScript package for `validate`, `inspect`, `audit`, `explain`, `trace`, `normalize`, `evaluate-replacement`, and `verify-migration`, with structured JSON output. Add CLI tests that run without a TypeScript build. After those changes, add a runtime-neutral consumer test importing `@forever-works/javascript/core`, rerun `npm install && make test`, and update this handoff with the new commit and results.

The most useful implementation entry points are `packages/javascript/src/model.js` (semantic core), `packages/javascript/src/node.js` (filesystem boundary), and `packages/javascript/test/conformance.test.js` (shared evidence).
