# Codex handoff: Public API v0.1

**Date:** 2026-10-03  
**Implementation commit:** `e9b1abd7610db03332fb264a1b42d514a7f6e62a`  
**Status:** coherent JavaScript Public API foundation complete; TypeScript and CLI facade parity deferred

## Execution and branch record

The checkout exposed its only branch as environment branch `work`. It was renamed in place to `main` before committing; no branch was created or checked out. Implementation commit `e9b1abd7610db03332fb264a1b42d514a7f6e62a` is on `main`. This handoff is committed separately, so its own commit is necessarily newer than the recorded implementation SHA.

## Implemented

* Added the official transport-neutral contract at `docs/API/PUBLIC_API_V0_1.md`, covering API versus model versions, discovery, operations, results, deterministic ordering, not-found behavior, stable errors, adapter duties, compatibility, and intentional HTTP/MCP deferral.
* Added `createForeverApi(path)` as the recommended Node JavaScript façade and `createForeverApiFromModel(model)` as the host-neutral façade.
* Added `describe`, `getProjectIntent`, `getEntity`, capability/invariant/dependency/implementation lists, `traceEntity`, `explainDependency`, `validateModel`, `audit`, `evaluateReplacement`, `verifyMigration`, and `normalize`.
* Added `ForeverApiError` with stable `code`, `message`, `details`, and JSON serialization. Covered entity and dependency not-found behavior.
* Added independent plain-JavaScript API tests. Existing direct JavaScript conformance and clean packed-consumer proof remain intact and require no TypeScript compiler.
* Corrected the JavaScript package license from Apache-2.0 to the repository's MIT license and included the license in packed artifacts.
* Expanded root and package onboarding with executable initializer, validation, audit, explanation, and JavaScript examples.
* Added accepted self-hosted decision `decision.public-api-v01`, explicitly preserving transport neutrality, authority order, discovery, conservative evidence, CLI/JSON's role, and non-canonical HTTP/MCP.

## Adapter matrix

| Operation | JavaScript façade | TypeScript | Python CLI |
| --- | --- | --- | --- |
| discovery / `describe` | complete | absent | partial legacy `inspect` only |
| project intent | complete | possible via generic list only | absent |
| entity lookup | complete | model-level method | absent |
| four public list operations | complete | generic model-level list | absent |
| trace / dependency explanation | complete | model-level methods | commands present |
| validation | complete | model-level method | command present |
| audit | complete | absent | command present |
| replacement evaluation | complete | model-level method | command present |
| migration verification | complete | absent | command present |
| normalization | complete | model-level method | command present |

The TypeScript binding was not made to re-export JavaScript; its independent proof remains valid but Public API parity is incomplete. The CLI retains equivalent semantics for its existing commands but lacks `describe`, list operations, and stable structured operational errors, so official API documentation accurately labels it incomplete.

## API conformance and tests

New JavaScript tests assert discovery shape and ordering, representative operations, validation, normalization, and stable serialized not-found errors. They run inside the independent JavaScript lane. A separate shared transport-neutral API fixture catalog was not added; that remains the next conformance task.

Commands actually run:

* `node --test packages/javascript/test/*.test.js` — passed: 20 tests (10 top-level tests including 10 shared catalog subtests), packed clean consumer included.
* `make test` — Python and JavaScript passed; TypeScript compilation then failed because checkout dependencies had not been installed (`@types/node` missing). This was an environment/setup failure, not accepted as a passing full run.
* `npm install && make test` — passed: Python 6 tests, JavaScript 20 tests, TypeScript 2 tests, C smoke, C++ smoke, and cross-language golden normalization.
* `git diff --check` — passed before the implementation commit.

## Initializer, release, and onboarding

The existing initializer was inspected. It already creates an explicit unreviewed draft intent, labels TODO content as non-authoritative, and provides an immediate validation/audit path; no semantic initializer change was necessary. Root onboarding now documents that safe flow. The obvious JavaScript package/repository license mismatch was fixed. Package names and the JavaScript `0.1.0` version align with the API initiative. Registry publication and GitHub-hosted CI were not attempted.

## Files changed

* `README.md`
* `docs/API/README.md`
* `docs/API/PUBLIC_API_V0_1.md`
* `docs/public-api-v0.1/CODEX_HANDOFF_PUBLIC_API.md`
* `forever/manifest.json`
* `forever/decisions/public-api-v01.json`
* `packages/javascript/LICENSE`
* `packages/javascript/README.md`
* `packages/javascript/package.json`
* `packages/javascript/src/index.js`
* `packages/javascript/src/model.js`
* `packages/javascript/src/node.js`
* `packages/javascript/test/public-api.test.js`

## Acceptance criteria

**Completed:** official Public API contract; API/model version distinction; capability discovery; stable JavaScript façade above `Model`; host-neutral construction; plain-JavaScript independence; stable JavaScript errors; deterministic public lists; API tests; improved onboarding; release-license consistency; self-hosted decision; preservation of existing model conformance; explicit transport deferral; accurate official adapter-status documentation.

**Partial:** API-level conformance currently consists of JavaScript tests rather than a shared adapter-neutral call/expectation fixture; CLI maps existing operations but is not a complete v0.1 adapter; TypeScript exposes many underlying semantics but not a public façade.

**Deferred:** TypeScript `audit`, `verifyMigration`, discovery, facade, classification validation parity; CLI `describe`, public list commands, and JSON errors; HTTP/MCP adapters; external package publication; deeper release metadata audit.

## Exact continuation point

Define a small plain-JSON API case catalog containing model fixture, operation, arguments, expected result or error code. Make JavaScript consume it first without weakening current tests. Then independently implement `ForeverApi`, `audit`, and `verifyMigration` in TypeScript and consume the same cases. Finally add CLI `describe` and list commands plus a single structured error envelope, update `docs/API/PUBLIC_API_V0_1.md` adapter status in the same commits, and rerun `npm install && make test` plus packed-consumer proof.
