# Small Reference Corpus for Cold-Agent Reconstitution

**Status:** research and teaching proposal; not a normative standard, executed benchmark, or claim of universal conversion. **Design target:** 7–10 deliberately varied examples, expandable only when an example reveals a genuinely new representational need.

## Thesis
The core Forever Works contract should remain small, generic, implementation-independent and stable. Agents learn its intended use through a **compact reference corpus** of substantially different software problems: what was extracted, why it matters, which facts are fixed compatibility obligations, which decisions remain fluid, how to reconstruct, and what objective evidence supports each claim.

The corpus must not hardcode a particular programming language, OS, GUI toolkit, runtime, agent, or application class. Any-Shape is one possible experimental producer and consumer, not a dependency of the standard.

## Ten candidate cases (begin with seven, expand when valuable)
1. Chrome extension → native desktop app: capability extraction, browser privilege substitution, preserving real user effects.
2. Desktop GUI → mobile app: semantic UX preservation without pixel copying; touch, lifecycle, storage and accessibility adaptations.
3. Python helper → browser extension: helper functions preserved while host architecture and permitted interfaces change.
4. Browser extension → Python or C++ utility: changing product shape and implementation language.
5. One source → multiple independent targets: target-specific context and independent proof against cross-target assumption leakage.
6. Multiple source products → interconnected suite: many-to-many interactions, shared service, state ownership, authority and ecosystem-wide validation.
7. Existing app → non-identical companion/assistant: new purpose, explicitly permitted integration, no false parity claims.
8. Specification-only → new product: source-independent construction with acceptance requirements rather than inherited behavior.
9. One service ↔ multiple services: fluid architectural topology while preserving externally required contracts and allowed variability.
10. Minimal Linux userspace ABI case: extract a single bounded Linux kernel-facing interface (e.g., pipe/file-descriptor semantics) including syscall ABI, observable semantics, errors, concurrency, test oracle, adjacent dependencies, and justified free implementation choices. This is **not** a claim to have extracted an entire Linux kernel or to have produced an ABI-compatible kernel.

## Per-case teaching packet (small, consistent, machine-readable where applicable)
- **Question and economic/use context:** WHY this transformation is useful.
- **Original artifact or reproducible fixture** and source authority/license, exact version/configuration/hash.
- **Intake observations:** observable source facts separated from inferred intent and human-reviewed requirements.
- **Preserved contract:** WHAT capabilities, invariants, UI meanings, security boundaries, state and ecosystem interactions are required.
- **Compatibility envelope:** operating environments and interfaces in scope, version, ABI/protocol, preconditions, externally observable behavior, failure semantics.
- **Variation map:** fixed obligations; bounded/constrained variations; implementation freedoms. Distinguish semantic necessity from historical implementation choice.
- **Derivation request:** WHAT new product(s) are required, preserve/transform/exclude/add, form, runtime, language preferences, and authorized relationships.
- **Reference reconstruction attempt:** HOW the new implementation was developed; architecture changes and design alternatives.
- **Independent oracle and evidence:** PROOF of actual behavior, integration and target-specific results, plus explicitly UNKNOWN/NOT_RUN cases.
- **Cold-agent challenge:** minimal unambiguous instructions giving agent the inheritance packet but not original source, with permitted tooling and a blinded acceptance suite.
- **Failure analysis:** missing meaning, negative transfer, unjustified authority, false equivalence, test failures, cost and context size.
- **Succinct lessons:** reusable abstractions that should or should not affect the generic standard.

Store each example as a separate leaf under a stable corpus index (suggested `examples/reconstitution/<case-id>/`). Keep core schemas and API free of fixture assumptions. Source samples and generated artifacts should be small or stored separately with reproducible hashes; keep the main repository lightweight. Case metadata should declare `proposed`, `specified`, `implemented`, `tested` and `independently-verified` distinctly rather than using one success boolean.

## Research protocol and adoption criteria
1. First establish source/requirement/evidence provenance and a bounded behavior contract; do not ask an agent to infer hidden truth from documentation alone.
2. Give a cold agent a neutral inheritance package and target request, not implementation source unless part of a separate control experiment.
3. Independently execute held-out tests and compare reconstructed behavior, labor, time, compute cost, portability and required corrections.
4. Repeat across dissimilar cases; compare with source-only and ordinary-documentation baselines before claiming the format causes faster reconstruction.
5. Promote a new generic field/API concept **only when multiple cases require it** or when one counterexample reveals a foundational correctness/security gap. Prefer optional versioned profiles for specialized technical detail.
6. Document negative and partial outcomes as carefully as successful ones; a case can be pedagogically valuable without full target parity.

## Kernel microcase: why it belongs
Use a fixed Linux ABI reference and a tiny selected surface to demonstrate **contractual fixity and implementation fluidity**. Record syscall numbering/signature on chosen architecture, flags, errors, blocking/nonblocking behavior, descriptor lifecycle, concurrency, user-visible invariants and observed reference traces. State explicitly whether musl/BusyBox/Alpine userspace dependencies belong to the test fixture. Let the agent construct a substitute component or model in a different language; independently verify the chosen envelope. Never present a userspace mock as proof of a bootable compatible kernel.

## Relation to standards and implementations
Forever Works owns generic record meaning, provenance, compatibility envelopes, optional ecosystem composition profiles and conformance semantics. Any-Shape owns source/target adapters, user `specifications.json`, reconstruction and actual independent execution. Do not make a request manifest and an inheritance corpus interchangeable: mapping between them should be explicit, versioned and reviewable.

**Research objective:** determine whether compact, deeply explained, heterogeneous examples enable cold agents to reconstitute unfamiliar software with fewer incorrect assumptions while leaving the core contract smaller, more portable and more durable.
