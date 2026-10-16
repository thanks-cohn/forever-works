# Next Codex run: earn a dependable foundation

Status: implementation brief, not a new normative standard.
Prepared 2026-10-15 (America/Chicago).
Baseline: main at 7460736afd6083bc56e8f4caa92f2a34f88bd9ee; inspect current HEAD before editing.

## Mission and scope

Implement the core-hardening phase of [the existing two-run request](CORE_HARDENING_AND_SOURCE_INDEPENDENT_PROOF_REQUEST.md). This file is the immediate execution brief; the earlier request retains the subsequent independent inheritance experiment.

The owner's ambition is an enduring, widely usable foundation for human and agent understanding of software. Make the existing promises precise, portable, understandable and independently testable. Optimize for adoption by people who do not know this repository's authors. Becoming a standard is an outcome of utility and trust, not a claim this run can establish.

Complete implementation, tests, CI and official documentation. Do not stop after another plan or architecture essay. Do not execute the source-independent construction experiment in this run: an agent that has read the source cannot claim to be its cold consumer.

Read AGENTS.md, docs/FOUNDATIONAL_PROPOSAL.md, docs/STANDARD.md, docs/API/PUBLIC_API_V0_1.md, the schemas, current conformance documentation, [the audit](../docs/RESEARCH/FOUNDATION_READINESS_AUDIT_2026-10-15.md), and [the product-generation vision](../docs/VISION/DOCUMENTATION_AS_A_FOUNDATION_FOR_NEW_PRODUCTS.md). Inspect applicable nested guidance and preserve unrelated work.

## Architecture principles for every decision

1. Keep the core small. Existing canonical concepts and plain UTF-8 JSON remain sufficient unless a reproduced use case proves otherwise. Put domain specialization in optional profiles.
2. Separate enduring intent, current implementation, supplied claims and observed evidence. Preserve provenance through every transformation; confidence is neither authority nor permission.
3. Specify behavior independently of a library, programming language, cloud, agent or hosted service. JavaScript must remain directly usable without a TypeScript compiler.
4. Prefer one authoritative statement linked from other documents. Keep the human explanation short enough to understand and provide exact contracts and examples through progressive detail.
5. Support incremental adoption and ordinary offline tooling. A small project must obtain value without describing its entire world.
6. Preserve valid unknown fields without giving them execution authority. Do not silently lose information during normalization or round trips.
7. Compatibility is deliberate: retain historical fixtures, distinguish bug fixes from semantic changes, and explain migrations. Do not silently reinterpret an existing version.
8. Quality is demonstrated by independent results and useful behavior. A shared implementation wrapped in another language is not independent semantic evidence.

## Work sequence

### 1. Establish failures and a contract map

Run the current baseline. Turn audit F1–F4 into reproducible regression tests before fixing them. Map each public operation to its authoritative rule, fixtures, supported bindings and known limitations. Include all actual reference fields; exact IDs may contain no dot. Do not treat arbitrary prose or source paths as entity references.

Track F5 separately: existing replacement PASS aggregates supplied claims; it is not independently verified execution. Preserve published evaluation semantics while clarifying the evidence boundary.

For genuine ambiguities, record the competing interpretations and compatibility impact. Implement unambiguous fixes while isolating any normative decision that needs acceptance. A planning note must not silently outrank the standard.

### 2. Make validation consistent

Enforce manifest and record structures, required fields, IDs, supported versions and documented version compatibility, enums/types, provenance, uniqueness and exact references in JavaScript, Python and TypeScript. Validate the self-model and all shipped examples.

Use an independent Draft 2020-12 schema implementation as a structural oracle over the shared corpus. Distinguish structural validity from graph semantics; neither oracle alone establishes both. Keep its dependencies explicit and reproducible.

Test valid unknown fields, undotted IDs, cycles, absent/null distinctions, unsupported and mismatched versions, wrong container types and malformed inventories. Repair the invalid self-model verification enum against the existing contract.

### 3. Make normalization portable

Specify exact key and record ordering, UTF-8 handling, significant array order, whitespace, number representation and accepted number domain. Test mixed case, punctuation, Unicode including supplementary characters, integer-like keys, escaped strings, negative zero, precision boundaries and nested extension objects.

Distinguish a normalized in-memory object from canonical output bytes: JavaScript object enumeration can reorder integer-like keys. Do not assume sorting properties plus JSON.stringify proves canonical serialization.

Compare actual independently produced bytes and digests across advertised implementations. Assess established canonicalization approaches against the current two-space/newline contract before inventing a new one; do not switch formats or add signing guarantees implicitly. Version any incompatible change and retain old fixtures.

### 4. Repair native parsing and loader boundaries

Replace C string-fragment parsing with proper bounded JSON parsing. Evaluate a small maintained parser versus existing dependencies; record license, portability, maintenance and dependency rationale. Missing or invalid records must never disappear into a successful validation result.

Apply shared applicable positive and negative fixtures to C and its C++ wrapper. Fix supported validation operations; explicitly report unsupported operations. Do not remove failing tests or redefine advertised support merely to obtain green CI.

Harden loaders for real target containment, traversal, absolute paths, symlinks, missing files, malformed UTF-8/JSON, duplicate JSON members, excessive depth, byte/record limits and deterministic failure. Define duplicate-member and resource-limit policies explicitly, checking compatibility before enforcing them.

Exercise Windows path behavior as well as POSIX when runners are available. State filesystem race assumptions honestly: a realpath check alone does not establish protection against concurrent hostile mutation.

Treat loaded model content as untrusted data. Do not execute commands, fetch arbitrary evidence URIs or grant capabilities from a document's assertions.

### 5. Make failures understandable and proof reproducible

Use the existing error mechanism where possible. Document stable codes, affected record/path, failure stage and actionable explanation without leaking sensitive content. Keep diagnostic representation compatible or explicitly version it.

Extend CI to run the same relevant corpus through each supported binding, the independent structural oracle, serialization goldens, self-model and examples. Run parser memory checks/sanitizers where supported and include bounded deterministic malformed-input tests. Record platform coverage and unavailable checks accurately.

Never regenerate expected outputs solely from the implementation being tested. Establish independent expected behavior from the normative contract and review intentional changes.

### 6. Make the foundation easy to adopt

Update official docs/API, conformance documentation and binding support status in the same changes as behavior. Provide a concise newcomer path using existing CLI/API capabilities: read a minimal model, validate, trace a dependency, explain why it exists, and inspect an unknown claim. Verify the documented commands in a clean consumer environment.

Link the explanation to exact contracts, fixture examples and a simple map of intent → requirements → implementation → evidence. State explicitly where a reader must supply project-specific knowledge. Do not add a new mandatory ontology, service, SDK or onboarding wizard.

Document an evolution policy covering clarification versus breaking change, optional-profile status, compatibility fixtures, deprecation and independent implementation evidence required before stronger conformance claims. Present any new governance proposal as proposed, not already accepted.

## Required evidence and completion gates

Produce a checked-in report under docs/RESEARCH with:

- Audited starting and finishing commits, environment/toolchain versions and exact reproducible commands.
- Every audit finding mapped to its regression, implementation change and result.
- Per-binding operation/fixture coverage, distinguishing independent implementations from wrappers.
- Structural versus semantic validation and declared versus executed verification results.
- Byte-level normalization agreement, loader boundary results and relevant resource measurements.
- Compatibility decisions, known gaps and any unresolved normative questions.
- A compact acceptance table marked PASS, FAIL, BLOCKED or NOT_RUN, supported by evidence.

Acceptance requires all previously valid baseline cases and new applicable adverse cases to pass; no silent record loss; no unreported schema/runtime disagreements; documented cross-language normalization agreement; tested loader containment within stated assumptions; and no inflated conformance claims. A blocked mandatory check means the run is incomplete, even if other checks pass.

Use coherent reviewable commits. Follow the repository's delivery workflow; do not rewrite history or publish packages/releases as a side effect. If environment limits prevent completion, leave exact continuation instructions and report the blocker rather than treating unexecuted work as success.

## Prepare the next proof, without claiming it

End with a short, concrete handoff for a separate experiment: two independently running small products export frozen documentation packages; a fresh agent receives only those packages and declared public platform references, then creates a useful third product from a broad objective. Evaluation must test actual interaction with both originals, data preservation, authority and recovery against published contracts, including held-out cases.

The packages must convey rationale AND exact current behavior, formats, errors, state ownership, compatibility and test examples. Do not supply the original implementation disguised as documentation, choose the entire third product in advance, or coach missing knowledge invisibly.

Record allowed access, checksums, interventions and failures. If genuine separation cannot be established, mark the construction trial NOT_RUN. This is the eventual path to the Atlas + Redown companion vision; successful hardening alone does not prove documentation sufficiency or commercial demand.

## Definition of a strong outcome

A maintainer can understand the core, implement its contracts without copying our internals, discover a bad model reliably, preserve valid data across tools, and explain exactly what has and has not been proven. That is the next credible step toward a foundation others can build on for decades.
