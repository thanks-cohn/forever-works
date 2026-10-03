# Codex Request: Make JavaScript a First-Class Forever Works Target

## Mission

Forever Works must treat **plain JavaScript as a first-class proof target from this point forward**.

JavaScript must not be treated as an incidental artifact emitted by the TypeScript compiler, a compatibility afterthought, or a weaker consumer path. A JavaScript project must be able to adopt, test, validate, query, normalize, evaluate replacements, and verify migrations with Forever Works without writing TypeScript or requiring a TypeScript compiler in the consuming project.

The canonical product remains the language-neutral Forever Works specification, schemas, and conformance behavior. JavaScript is a major proof that those semantics stand independently of TypeScript.

Read these files completely before changing anything:

- `docs/FOUNDATIONAL_PROPOSAL.md`
- `docs/CODEX_FOUNDATIONAL_BUILD_REQUEST.md`
- `docs/STANDARD.md`
- `docs/CONFORMANCE.md`
- `docs/LANGUAGE_BINDINGS.md`
- `AGENTS.md`

## Main-only execution rule

Work **directly on the current `main` branch for the entire task**.

Do not create an implementation branch. Do not switch to another branch. Do not open a pull request for this task.

All implementation, tests, documentation, conformance updates, self-hosting records, and the final handoff must be written and committed directly to `main`.

Before changing anything, confirm that the working branch is `main` and that it contains this request. If the environment normally prefers branch-based work, this request intentionally overrides that preference for this task.

Keep commits coherent and leave `main` in a tested, continuation-ready state.

## 30-minute execution and handoff requirement

This task has an **approximately 30-minute implementation window**.

Use the time deliberately:

- Spend the early portion on the highest-value JavaScript-first work that establishes independent plain-JavaScript capability and conformance.
- As the time window approaches its final several minutes, prioritize stabilization, targeted verification, coherent commits, and the handoff over beginning another large subsystem.
- At approximately 30 minutes, produce and commit `docs/CODEX_HANDOFF_JAVASCRIPT.md` even if every acceptance criterion has not yet been completed.
- The handoff is mandatory. Incomplete implementation is acceptable; an absent or vague handoff is not.
- Preserve partially completed work in a clean, understandable state so the next Codex run can continue immediately.
- Clearly distinguish completed, partially completed, deferred, failing, and unverified work.
- Do not claim tests or conformance passed unless they were actually run successfully.

The handoff should be treated as a deliverable equal in importance to the code. Reserve enough of the time window to make it useful.

## Non-negotiable design rule

A successful TypeScript build is **not** evidence that the JavaScript target works.

JavaScript must have its own implementation surface, tests, examples, CI lane, documentation, and conformance evidence. It must be possible to run the JavaScript proof without invoking `tsc`.

At the same time, do not weaken language neutrality or turn JavaScript into the canonical definition of Forever Works. The authority order remains:

1. normative specification,
2. schemas and conformance fixtures,
3. reference/proof bindings,
4. convenience tooling.

## Architecture

Create a genuine plain-JavaScript proof binding using modern JavaScript and the standard runtime library where practical.

Prefer a dedicated location such as:

`packages/javascript/`

The JavaScript binding should be authored as `.js`, not TypeScript masquerading as JavaScript. It must not import the compiled implementation from `packages/typescript/dist` to satisfy conformance. Shared fixtures, schemas, and expected outputs are encouraged; duplicated semantics should be minimized through the standard and conformance contract rather than by making JavaScript secretly depend on TypeScript.

Use ESM as the primary module format. Keep the semantic core separable from Node-specific filesystem loading so the model logic is not unnecessarily locked to one JavaScript host. Node 20 is the current execution baseline, but the public data model and pure operations should remain portable enough for future browser, Deno, Bun, embedded, or other JavaScript adapters.

Prefer zero runtime dependencies for the JavaScript binding. If a dependency is truly necessary, document its Forever Works dependency intent and replacement policy.

## JavaScript public capability target

The JavaScript binding should reach parity with the meaningful v0.1 operations already demonstrated elsewhere, including:

- load a Forever Works model,
- construct/use a model from already-parsed JSON data where useful,
- validate required semantics,
- get an entity,
- list records by kind,
- trace the relationship graph safely through cycles,
- explain dependency intent,
- find dependencies by replacement classification,
- audit the model,
- normalize deterministically,
- evaluate a dependency replacement,
- verify a migration,
- preserve unknown extension/future fields,
- reject escaping model paths in filesystem adapters,
- preserve pass/fail/unknown semantics and partial overall results exactly as the standard defines them.

Names may be idiomatic JavaScript, but semantic behavior must match the standard and conformance suite.

## First-class JavaScript package

Give JavaScript its own package identity and package metadata. It should be independently consumable by a plain JavaScript project.

At minimum:

- clear `package.json`,
- explicit `exports`,
- an ESM entry point,
- useful JSDoc on public APIs,
- no requirement that the consumer install or run TypeScript,
- a package-consumption smoke test from outside the repository package directory.

If adding a CommonJS compatibility wrapper is simple and does not duplicate semantics, it may be added, but ESM is the primary requirement.

## JavaScript conformance lane

JavaScript must receive its **own conformance lane** rather than piggybacking on TypeScript.

Extend the conformance harness so JavaScript independently consumes the shared fixtures and is checked against canonical expected output. Cover at least:

- minimal valid model,
- complete model,
- invalid required fields,
- duplicate IDs,
- broken references,
- invalid dependency classification,
- unknown future fields,
- older compatible 0.x data,
- circular relationships,
- preserving migration,
- violating migration,
- replacement evaluation,
- deterministic normalization.

The JavaScript lane must compare canonical normalized output to the same golden files used by the other bindings.

Where practical, compare JavaScript results for replacement and migration evaluation against the normative golden outputs as well.

A conformance failure in JavaScript must fail CI even when TypeScript, Python, C, and C++ pass.

## Dedicated JavaScript tests

Add direct JavaScript tests, preferably using the built-in `node:test` runner unless another already-required mechanism is clearly better.

Test more than happy paths. Include:

- stable normalization,
- graph cycles,
- unknown-field preservation,
- error handling,
- missing evidence becoming `unknown`,
- any failed requirement causing overall `fail`,
- all-pass requirements producing `pass`,
- mixed pass/unknown producing `partial`,
- path traversal protection,
- defensive behavior around malformed records,
- public package import from a clean temporary consumer.

Do not treat these as duplicates of TypeScript tests. They are independent evidence for the JavaScript target.

## JavaScript example

Add a complete plain JavaScript example under a clearly named location such as:

`examples/javascript/`

It must contain no TypeScript source and require no TypeScript build step.

The example should demonstrate the whole conceptual chain:

intent → capability/invariant → implementation/dependency → replacement evaluation → migration verification.

Keep it small enough that a new user can understand it quickly.

## JavaScript CLI proof

Provide a JavaScript CLI proof or adapter if it can be done cleanly without distorting the architecture. It should exercise the same structured operations that matter to agents, such as:

- validate,
- inspect,
- audit,
- explain,
- trace,
- normalize,
- evaluate-replacement,
- verify-migration.

This JavaScript CLI does not need to replace the existing portable CLI. Its purpose is to prove that JavaScript can independently drive the standard end-to-end.

Structured JSON output should remain available for agents.

## CI and Makefile

Add JavaScript as an explicit independent target.

The top-level workflow should make failures attributable to the JavaScript lane. Add commands equivalent in spirit to:

`make test-javascript`

and include it in `make test`.

The JavaScript test path must not rely on TypeScript being built first.

Keep existing TypeScript, Python, C, C++, and cross-language tests intact.

## Cross-language conformance

Expand cross-language conformance so the documented proof set becomes:

- JavaScript,
- TypeScript,
- C,
- Python,
- C++ where its wrapper surface is applicable.

JavaScript and TypeScript are separate proof targets even though they share a language ecosystem.

The conformance documentation must say this explicitly.

Where the C/C++ surface is intentionally smaller, document the exact conformance level rather than pretending all bindings expose identical convenience APIs.

## Documentation

Give JavaScript its own substantive section in `docs/LANGUAGE_BINDINGS.md`.

Update the README, roadmap, conformance documentation, and any other relevant docs so JavaScript is described as a first-class target.

The documentation must distinguish:

- **JavaScript proof binding**: runs directly as JavaScript and has independent conformance evidence.
- **TypeScript proof binding**: adds static types and TypeScript-oriented ergonomics.
- **Canonical standard**: belongs to neither language.

Do not describe JavaScript as merely “compiled TypeScript.”

## Self-hosting requirement

Forever Works describes itself, so the repository's own `forever/` model should record this decision.

Add/update appropriate self-hosted records so future agents can discover that:

- JavaScript is a first-class proof target,
- JavaScript conformance cannot be inferred solely from TypeScript conformance,
- the canonical standard remains language-neutral,
- plain JavaScript consumption must not require a TypeScript compiler.

Use the existing provenance model and keep this architectural decision explicit.

## Security and portability

Do not weaken current model-root path protections.

Use standard UTF-8 JSON and deterministic output.

Avoid JavaScript-specific values that cannot round-trip through canonical JSON.

Do not introduce assumptions that would prevent non-JavaScript bindings from remaining authoritative peers.

## Packaging acceptance test

Perform a realistic consumer test:

1. build or prepare the JavaScript package if preparation is needed,
2. create a clean temporary plain-JavaScript consumer,
3. install or reference the packaged artifact,
4. import it with ordinary JavaScript,
5. load the complete conformance fixture or equivalent copied fixture,
6. execute validation, dependency explanation, replacement evaluation, and migration verification,
7. verify expected structured results.

The consumer test must not invoke `tsc`.

## Required final verification

Before declaring the work complete, run the strongest practical set of checks, including:

- JavaScript unit tests,
- JavaScript conformance tests,
- package-consumer smoke test,
- existing TypeScript tests,
- existing Python tests,
- existing C tests,
- existing C++ tests,
- cross-language golden comparison,
- repository JSON parsing/validation checks already used by the project,
- `git diff --check`,
- the full `make test` path.

Fix regressions rather than weakening tests.

## Handoff

By approximately the end of the 30-minute implementation window, create or update and commit:

`docs/CODEX_HANDOFF_JAVASCRIPT.md`

This handoff is required whether the JavaScript-first-class work is complete or partial.

Document:

- what changed,
- JavaScript architecture,
- public JavaScript API,
- test and conformance coverage,
- commands run and results,
- package-consumer proof,
- files changed,
- any intentionally deferred work,
- any remaining differences between JavaScript and the other bindings,
- confirmation that the work was performed directly on `main`,
- latest `main` commit SHA,
- exact next recommended work,
- acceptance criteria completed versus still outstanding,
- any work that was started but not fully verified,
- the most useful continuation point for the next Codex run.

## Commit and completion workflow

Do not create a branch and do not open a pull request.

Implement and commit directly to `main`.

Use the 30-minute window to produce the strongest coherent JavaScript foundation possible. As the handoff window approaches, prioritize the most relevant verification that can be completed reliably, fix regressions where practical, and preserve unresolved failures explicitly in the handoff rather than hiding them.

By approximately 30 minutes:

1. have the current implementation committed coherently to `main`,
2. run the strongest relevant verification that fits within the time window,
3. create/update `docs/CODEX_HANDOFF_JAVASCRIPT.md`,
4. commit the handoff directly to `main`,
5. report the latest `main` commit SHA in the handoff.

The deliverable for this run is **working progress plus a precise continuation handoff on `main`**. Full acceptance may continue in a later run if the 30-minute window is reached first.

## Acceptance criteria

This request is complete only when all of the following are true:

1. A plain JavaScript project can use Forever Works without TypeScript source or a TypeScript compiler.
2. JavaScript has an independently authored/runtime-visible proof surface rather than importing the TypeScript implementation to pass.
3. JavaScript has dedicated tests.
4. JavaScript has dedicated conformance checks against shared fixtures/goldens.
5. JavaScript has a plain-JS example.
6. JavaScript is an explicit CI/Makefile target.
7. JavaScript is documented as a first-class proof target.
8. The self-hosted Forever Works model records the JavaScript-first-class decision.
9. Existing TypeScript, C, Python, and C++ behavior remains passing.
10. The standard remains language-neutral.

## North star

A future maintainer should be able to delete every TypeScript source file from a copy of the repository and still point to the JavaScript proof binding as independent evidence that Forever Works semantics are usable from ordinary JavaScript.

JavaScript is now a main target. Give it the same seriousness as the existing proof bindings, and where JavaScript's ecosystem allows stronger packaging, consumption, and agent-integration tests, use that opportunity to make its proof especially rigorous.
