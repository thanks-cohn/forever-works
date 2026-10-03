# Codex Request: Forever Works Public API v0.1 + Early-Adopter Readiness

## Mission

You have approximately **30 minutes** to turn the existing Forever Works foundation into the beginning of a stable, publicly consumable platform.

The primary deliverables are:

1. a carefully scoped **Forever Works Public API v0.1**,
2. a strong JavaScript façade implementing that semantic API,
3. CLI/JSON alignment with the same semantics,
4. meaningful TypeScript parity where practical,
5. API-level conformance evidence,
6. materially better newcomer/adopter readiness,
7. release-consistency cleanup,
8. self-hosted records preserving the API design,
9. and a mandatory continuation handoff committed by approximately the end of the 30-minute window.

The long-term design goal remains:

> **A sufficiently capable agent should be able to inherit the repository cold, understand it, repair it, modernize it, verify the repair, and leave it in a better documented state without needing the original developers.**

The public API should make that future agent able to interrogate a Forever Works repository through stable semantics rather than implementation-specific knowledge.

## Required reading

Before changing anything, read completely:

- `AGENTS.md`
- `docs/STANDARD.md`
- `docs/AGENT_PROTOCOL.md`
- `docs/CONFORMANCE.md`
- `docs/LANGUAGE_BINDINGS.md`
- `docs/VISION_ADOPTION_AND_COMPETITIVE_STRATEGY_PROPOSAL.md`
- `docs/CODEX_HANDOFF_JAVASCRIPT.md`
- `docs/public-api-v0.1/PROPOSAL.md`

Inspect the current JavaScript, TypeScript, Python, CLI, conformance, schema, and self-hosted `forever/` implementations before deciding exact code changes.

## Main-only execution rule

Work **directly on the current `main` branch for the entire task**.

Do not create or switch to another branch.

Do not open a pull request.

Commit coherent work directly to `main`.

This instruction intentionally overrides a normal branch-first workflow for this run.

## 30-minute execution and handoff requirement

Use approximately 30 minutes for implementation.

Prioritize the strongest coherent foundation, not the largest amount of surface area.

Early in the run, establish the semantic contract and highest-leverage implementation work.

As the final several minutes approach, prioritize:

- stabilization,
- targeted verification,
- coherent commits,
- documentation accuracy,
- and the required handoff.

By approximately the end of the 30-minute window, create or update and commit:

`docs/public-api-v0.1/CODEX_HANDOFF_PUBLIC_API.md`

The handoff is mandatory whether every acceptance criterion is complete or not.

Incomplete implementation is acceptable. An absent, vague, or misleading handoff is not.

Clearly distinguish completed, partial, deferred, failing, and unverified work.

Do not claim a test, adapter, package, or conformance result passed unless it was actually executed successfully.

## Authority order

Preserve the existing Forever Works authority model:

1. normative specification,
2. schemas and conformance fixtures,
3. public semantic API contract,
4. reference/proof implementations,
5. transports and convenience tooling.

The API must not contradict the normative standard.

If an existing implementation conflicts with the standard, preserve the standard and fix the implementation or document the conflict.

## 1. Define the Public API v0.1

Create:

`docs/public-api-v0.1/PUBLIC_API_V0_1.md`

This should be a serious, implementation-independent API contract.

Define at minimum:

- API versioning,
- relationship between API version and model version,
- capability/operation discovery,
- operation names,
- arguments,
- success semantics,
- not-found semantics,
- stable machine-readable errors,
- deterministic ordering requirements,
- JSON representation expectations,
- adapter obligations,
- unsupported-operation behavior,
- and compatibility/evolution rules for the API.

The initial semantic operations should cover, at minimum where supported by the standard:

- `describe`
- `getProjectIntent`
- `getEntity`
- capability listing
- invariant listing
- dependency listing
- implementation listing
- `traceEntity`
- `explainDependency`
- `validateModel`
- `audit`
- `evaluateReplacement`
- `verifyMigration`
- `normalize`

You may refine names if doing so creates a demonstrably clearer durable API, but avoid unnecessary proliferation.

Do not add a method merely because one binding happens to expose it easily.

## 2. Add explicit discovery

An unfamiliar client or future agent should be able to discover what an implementation supports.

Define and implement a discovery result that includes appropriate fields such as:

- `foreverApiVersion`,
- supported model versions,
- supported operations/capabilities,
- implementation identity/profile where useful,
- and optional adapter information.

Do not make vendor identity part of semantic correctness.

## 3. JavaScript public façade

Use the first-class JavaScript target as the strongest initial public façade.

Prefer a durable high-level construction shape such as:

```js
import { createForeverApi } from "@forever-works/javascript";

const forever = await createForeverApi("./forever");
```

The façade must sit above internal `Model` details.

It should expose the public semantic API without requiring a consuming project to know the current internal class layout.

Keep the host-neutral core separable from Node filesystem concerns.

Plain JavaScript consumers must not require TypeScript or `tsc`.

Preserve the existing independent JavaScript conformance proof.

## 4. TypeScript parity

Bring the TypeScript proof target into semantic API parity where practical within the time window.

Pay particular attention to known areas where the JavaScript implementation is stronger, including:

- audit behavior,
- migration verification,
- dependency-classification validation,
- discovery/public façade,
- stable errors,
- and output parity.

Do not simply re-export the JavaScript implementation to make TypeScript appear conformant.

TypeScript should remain an independent proof target.

## 5. CLI/JSON adapter

Make the CLI explicitly map to the public semantic API.

Existing commands should correspond predictably to API operations.

Where practical, add a discovery/info command for the public API.

Structured JSON output should be suitable for an external agent or a programming language with no native binding.

The CLI is a lowest-common-denominator adapter, not the canonical definition.

Do not rewrite the CLI merely for stylistic consistency if a smaller adapter-layer change can produce the required semantic alignment.

## 6. API conformance

Add API-level conformance fixtures/tests.

The conformance model should be able to express the equivalent of:

```text
Given model X
Call operation Y with arguments Z
Expect semantic result R
```

At minimum, cover the highest-value public operations and stable error behavior.

JavaScript must have independent API conformance.

TypeScript and CLI should consume the same expected semantics where practical.

Preserve all existing model-level conformance and golden files.

Do not weaken tests to obtain parity.

## 7. Public onboarding

Improve the README and/or add a concise getting-started document so an unfamiliar developer can understand and exercise Forever Works in roughly five minutes.

The path should make it easy to discover:

```sh
forever init
forever validate
forever audit
forever explain dependency.example
```

Use real commands that actually exist after the run.

Do not document commands or package-install flows that are not implemented.

Show the public JavaScript API with a minimal working example.

Make the first page answer why Forever Works is useful, not only how its repository is organized.

## 8. Harden `forever init`

Improve the initializer where practical so it creates a safe and understandable starter model.

Generated placeholders or inferred material must never masquerade as accepted architectural truth.

Ensure a newly initialized project has a clear path into validation and auditing.

Do not attempt the full intelligent repository-discovery system in this run.

## 9. Release-readiness consistency audit

Audit and fix clear inconsistencies that would confuse an early adopter.

Check:

- root and package license metadata,
- package names,
- versions,
- exports,
- runtime requirements,
- README installation/use instructions,
- CLI naming,
- API terminology,
- model/API/standard version terminology,
- schema references,
- examples,
- command exit behavior,
- structured errors,
- and claims about implemented features.

A known issue to inspect: the repository root currently contains an MIT license while the JavaScript package metadata declares `Apache-2.0`.

Do not choose a new license policy. Preserve repository licensing intent and make package metadata consistent with it unless repository evidence establishes otherwise.

## 10. Self-host the API decision

Update the repository's own `forever/` model so future agents can discover the architectural intent behind the public API.

Record, with appropriate provenance, that:

- the public API is semantic and transport-neutral,
- specification and conformance remain authoritative,
- JavaScript/TypeScript/CLI are adapters or proof implementations,
- capability discovery supports cold inheritance,
- CLI/JSON is a lowest-common-denominator path,
- missing evidence remains unknown,
- and HTTP/MCP are intentionally not canonical transports.

Keep the model valid.

## 11. Explicitly defer HTTP and MCP

Do not build a REST server or MCP server in this run.

If useful, document how those future adapters should map onto the semantic API.

The project must stabilize the semantic contract before proliferating transports.

## 12. Verification

Run the strongest practical verification that fits inside the time window.

At minimum, prioritize:

- JavaScript public-API tests,
- JavaScript existing tests,
- API conformance,
- TypeScript tests if modified,
- CLI behavior tests if modified,
- Python tests,
- C/C++ smoke tests where the full suite permits,
- cross-language conformance,
- self-hosted model validation,
- package-consumer proof if JavaScript exports change,
- JSON parsing/validation,
- `git diff --check`,
- and the full `make test` path when practical.

If environment setup consumes time, report it accurately.

Do not hide failures.

## 13. Handoff

By approximately the end of the 30-minute window, create and commit:

`docs/public-api-v0.1/CODEX_HANDOFF_PUBLIC_API.md`

The handoff must include:

- what was implemented,
- public API operations actually defined,
- public API operations actually implemented per adapter,
- JavaScript façade state,
- TypeScript parity state,
- CLI parity state,
- API conformance state,
- onboarding state,
- initializer changes,
- release-readiness issues found and fixed,
- release-readiness issues remaining,
- self-hosted model changes,
- exact commands/tests run and their results,
- files changed,
- intentional deferrals,
- failures or unverified claims,
- acceptance criteria completed versus outstanding,
- confirmation that work was performed on `main`,
- latest `main` commit SHA available to the run,
- and the exact best continuation point for the next Codex session.

The handoff is a first-class deliverable.

## 14. Acceptance criteria

A strong completion should satisfy as many of these as possible without sacrificing correctness:

1. A written transport-neutral Public API v0.1 exists.
2. API/version/capability discovery exists.
3. JavaScript exposes a stable façade above internal model details.
4. Plain JavaScript consumers still require no TypeScript compiler.
5. TypeScript materially approaches or reaches the same semantic contract.
6. CLI JSON maps predictably onto the public semantic API.
7. API-level conformance exists.
8. Existing model-level conformance remains intact.
9. Newcomer onboarding is materially clearer and executable.
10. `forever init` is safe and understandable for an early adopter.
11. Obvious release metadata inconsistencies are corrected.
12. The self-hosted Forever Works model records the API design.
13. Existing JavaScript, TypeScript, Python, C, and C++ proof behavior is not weakened.
14. No HTTP/MCP transport is made canonical.
15. The mandatory handoff is committed on `main`.

## 15. Design test

For every public operation, ask:

> **Would this operation still make sense if today's JavaScript implementation, CLI layout, package manager, and agent ecosystem disappeared?**

If yes, it may belong in the durable API.

If no, keep it in an adapter or implementation-specific layer.

## 16. Desired outcome

The run should move Forever Works from:

> strong working research foundation

toward:

> **early, coherent, publicly usable standard with a stable interrogation surface**

without pretending the project is more mature than the evidence supports.

The next major phase after this should be discovery, recovery, and autonomous maintenance—not another round of unnecessary API expansion.
