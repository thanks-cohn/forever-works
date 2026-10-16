# Codex request: close foundation gaps and prepare an independent inheritance proof

Prepared: 2026-10-16. Planning and execution brief, not a normative edition.
Observed baseline: main at 16cccc32e0c6ca961a773ac40b0ddc102078038d. Refresh HEAD and CI before work.

## Outcome

Finish the unresolved foundation work, then deliver the runnable preparation for a genuinely separate documentation-only construction experiment. Implement and verify the work; another proposal alone is insufficient.

The owner's objective is a durable standard that humans and AI agents choose because it makes understanding, maintenance, migration and new product construction easier and more dependable. Earn that preference through useful behavior, low adoption cost, interoperability and evidence. Becoming the de facto standard is an ambition, not an acceptance claim.

This continues [the foundation brief](NEXT_RUN_FOUNDATION_HARDENING.md), informed by [the actual results](../docs/RESEARCH/FOUNDATION_HARDENING_RESULTS_2026-10-16.md). Do not redo completed work unnecessarily or discard its compatibility evidence.

Read AGENTS.md, docs/FOUNDATIONAL_PROPOSAL.md, docs/STANDARD.md, spec/VERSIONING.md, docs/API/CORE_INPUT_AND_NORMALIZATION.md, docs/API/OPERATION_COVERAGE.md, the current schemas/fixtures and applicable nested guidance. Read the source-independent product-generation and cumulative semantic inheritance vision for intent. Specification remains authoritative over implementation and handoffs.

Work on main, preserve unrelated changes and use coherent commits. Do not force-push, self-merge PRs, publish packages or create releases. If the execution environment cannot deliver to main, provide the exact changes and delivery blocker without claiming they landed.

## Stage A — finish the hardening gates

### A1. Diagnose and repair Windows

Observed hosted run 38893778197 passed test, javascript, native-sanitizer, Linux core-hardening and ecosystem-schema, but failed Windows core-hardening at its make invocation. Inspect the actual logs and current results; the failing cause has not been established by this brief.

Distinguish toolchain/environment failure from a product defect. Fix the root cause and preserve the meaningful coverage. Do not skip Windows, weaken assertions, accept false-success exit codes or replace filesystem checks with string-only tests.

Exercise actual Windows real-target containment, supported symlink/junction behavior, encoding, resource limits, native compilation and subprocess execution. Explain any unsupported privilege-dependent case precisely. Linux tests with Windows-shaped paths are not Windows filesystem proof.

Run the hosted checks against the delivered revision when the workflow and permissions allow. Record exact run URLs and conclusions; queued, configured or locally simulated checks are not hosted PASS evidence.

### A2. Resolve lossless numbers as an interoperability contract

The observed JS input 9007199254740993 becomes 9007199254740992. Unknown fields can contain numbers, so this affects the promise to preserve information.

Evaluate at least these choices against actual APIs and backward compatibility: lossless numeric tokens/decimal values, an explicitly versioned restricted numeric domain, and separate raw-preserving interchange versus ordinary host-language values. Prefer an additive lossless interchange path that preserves existing 0.1 consumers and ordinary small-number ergonomics, if feasible. Select the smallest coherent design from evidence, not a universal custom arithmetic system.

This request authorizes designing and implementing the compatible API addition and documenting its rationale. It does not authorize silently narrowing Standard 0.1 or presenting a new incompatible edition as accepted. If only an incompatible normative change can meet a requirement, isolate that proposal, keep existing compatibility, complete independent work and mark that gate BLOCKED.

Define exactly what is preserved: mathematical numeric value, original token spelling, or both. Define canonical bytes separately from source-preserving round trips. Specify finite values, exponent handling, negative zero, equivalent decimal spellings and resource bounds before writing goldens. Bound token/exponent processing to avoid huge allocations; unsupported inputs must fail explicitly rather than round silently.

Include signed and unsigned safe-integer boundaries, adjacent integers beyond binary64 precision, high-precision decimals, tiny/huge exponents, equivalent numeric spellings, nested unknown fields, and programmatically constructed host objects whose original precision was already lost. Never promise to reconstruct a number after it was rounded before our API received it.

Check structural schema numeric constraints without lossy conversions. Compare independent implementations and expected bytes; identify genuinely independent algorithms versus generated copies/wrappers. Preserve historical goldens unless an explicitly documented new mode/edition applies. Keep a clear compatibility matrix for old/new input, old/new API and serialization modes.

Turn observe_numeric_gap into a permanent regression with exact expected behavior for each mode. The final report must say whether lossless preservation is universal for the advertised supported domain or still limited.

### A3. Close the loop

Rerun existing tests, shared adverse corpus, oracle, examples, self-model, clean consumers, normalization comparisons and relevant sanitizers. Run only additional tests needed for changed behavior or unresolved gates. Verify plain JavaScript without a TypeScript compiler.

Update official API, input/error contract, binding coverage and evolution docs alongside implementation. Maintain provenance and UNKNOWN boundaries. Do not promote supplied PASS claims to verified software behavior.

Produce a new evidence report without rewriting the historical report. Map each outstanding gate to commands, regression files, actual outputs, final revision and hosted CI results. Any failed mandatory gate leaves hardening INCOMPLETE.

## Stage B — prepare a small real proof of the distinctive promise

After Stage A gates pass, implement two small, distinct, independently running example products and their documentation-package exports. Reuse existing profiles and contracts where sufficient; keep new package conventions experimental and optional.

Use examples with real persisted state and controlled interaction, such as a local collection/catalog service and a separate asset store. Avoid paid infrastructure, real credentials and personal data. They should be simple enough to audit but substantial enough to expose identity, data preservation, authorization and interrupted-operation issues.

Each frozen package should efficiently convey:
- Purpose, user outcomes, non-goals and essential invariants.
- Current architecture, rationale, replaceable mechanisms and actual implementation limitations.
- Exact data/wire formats, stable identity, state ownership, operations and observable effects.
- Errors, retries, idempotency where applicable, recovery and version compatibility.
- Authority boundaries and safe test access.
- Examples, acceptance fixtures, package version and checksums.
- Known unknowns, provenance and a map to deeper details.

Existing machine-readable records should carry the structured meaning; avoid narrative-only packages that bypass Forever Works. Documentation may explain algorithms and contracts, but must not smuggle original implementation source into the consumer package. Record allowed dependencies and references explicitly.

Create an exporter/validator and a clean package-consumption smoke check using the smallest existing tooling extension possible. Validate the manifest, required content, cross-links and integrity; distinguish these checks from semantic sufficiency. Export only allowlisted public material. Verify no secrets, private paths or unintended source files enter the package.

Prepare reproducible producer startup, reset and test-data setup. Supply a broad consumer objective such as "create a useful complementary product that works with both systems and preserves their contracts." Leave the third product's design to the fresh consumer; do not prescribe the entire solution.

Create a separate evaluator with held-out cases derived only from published obligations: interact with both producers, preserve metadata and identities, obey authority, survive interruption/retry and round-trip data. Separate package export, construction inputs and evaluator-only artifacts with enforceable access boundaries. Do not claim that mere separate directories isolate an agent with unrestricted filesystem access.

This source-aware run may build producers and the harness; it must not claim independent consumer success. Finish with a ready-to-run fresh-session handoff and objective evidence criteria. Mark construction NOT_RUN until a genuinely fresh consumer session is restricted to the frozen packages, declared public platform references, toolchain and explicitly permitted reference services. If isolation cannot be enforced, disclose it and downgrade the experiment. Log questions and interventions; never coach missing knowledge invisibly.

If Stage A remains blocked, finish the directly useful hardening work and the next-proof design/access manifest, but defer building the new products. Do not bury an incomplete foundation beneath new examples.

## Stage C — ensure humans can use and maintain it

Keep adoption lightweight: a small project should begin with intent, a few invariants, one dependency rationale and links to evidence. Do not require exhaustive modeling.

Extend the newcomer path only where needed to demonstrate the delivered behavior. Provide an indexed overview answering why the system exists, how its parts relate, what must survive, what implements it now, and what is verified. Link exact details underneath. Verify commands from a clean consumer environment.

Provide one concrete maintenance example showing a human behavior change or bug fix updating its contract, reasoning, affected implementation links and evidence. Preserve uncertain discoveries as inferred or agent-proposed. Detect stale referenced artifacts where practical; do not equate link existence with semantic freshness or turn all source changes into documentation failures.

Do not invent shorthand terms or mandatory new concepts without measured benefit. Do not write another broad competitor essay. Record a small future test portfolio—extension, CLI, stateful service, native library and language rewrite—as follow-on hypotheses, not claimed coverage of this run.

## Required delivery

1. Implemented and documented numeric decision with compatibility fixtures, explicit losslessness scope and independent output evidence.
2. Root-cause Windows fix and actual platform/hosted evidence, or a precise outstanding blocker.
3. Updated acceptance report with PASS / FAIL / BLOCKED / NOT_RUN and links to supporting artifacts.
4. If hardening passes: two runnable producers, frozen documentation packages, exporter/validator, separated evaluator and a fresh-consumer starter handoff. Otherwise: a bounded preparation document and remaining gates.
5. A short user-facing explanation of what works, what remains and what the next independent run will establish.

Stop expanding scope when these deliverables are satisfied. No result establishes universal AI preference, complete documentation sufficiency or future market dominance. A successful outcome gives independent adopters stronger reasons to trust and choose the format.
