# Proposal: Selective Reconstitution — Capability Recovery from Entangled Software

**Status:** Important research proposal; not normative, not implemented  
**Project:** Forever Works  
**Scope:** Legacy rescue, selective extraction, dependency archaeology, controlled simplification, cross-language reconstruction, agent-verifiable continuity  
**Principle:** **Preserve the capability. Discard the accidental complexity.**  
**Acceptance thesis:** A cold agent can inherit a selected-capability extraction package, rebuild only those capabilities independently, and prove their essential behavior survived without inheriting unrelated machinery.

## 1. Why this matters

Many valuable applications accumulate extraneous and intermeshed dependencies, accidental module couplings, inconsistent state conventions, undocumented side effects and fragile startup ordering. Development may have occurred in parallel, without coherent planning, across multiple generations of maintainers and frameworks. The result can be a powerful product whose valuable features are difficult to repair without triggering failures elsewhere.

A full rewrite often inherits speculative requirements or abandons subtle working behavior. Incremental refactoring may remain trapped inside the original architecture. Keeping every historical feature is not always desirable.

**Selective Reconstitution** instead starts with the owner's explicit choice of capabilities worth retaining. The original repository is an **evidence source**, not an architectural template or a requirement to copy its entire surface. Agents document both (a) abstract capability identity and (b) concrete implementation reality, then progressively peel away unnecessary parts. A recovered capability can have a second life in the same language, a different framework, or another language and platform.

This is a proposed research direction related to program slicing, software archaeology, specification mining, dependency disentanglement, strangler migrations and clean-room reimplementation. Forever Works would integrate these into an explicitly scoped, evidence-backed, cold-agent reproducible recovery workflow.

> No capability is condemned to inherit the defects, dependencies, or architectural accidents of the system in which it was born.

## 2. Owner-selected scope and three-way disposition

A researcher names one or more **capabilities to rescue**, not the source files they assume implement those capabilities. Example: from a larger editor named SUBSTRATE, recover selected Word/DOCX and PDF operations, while leaving unrelated extension UI, cloud sync, asset browser, animation and other systems out of scope.

For each behavior discovered, record an explicit disposition:

- **PRESERVE:** verified intended behavior and associated constraints.
- **CORRECT:** observed defect with an owner-approved corrected expectation and regression test.
- **EXCLUDE:** behavior intentionally outside the extraction boundary.

Do not silently canonize historical bugs or allow agents to redefine the owner's intent. Inferred requirements remain proposals pending acceptance. Unknown, contested, unsupported and needs-human-verification states are first-class outcomes.

The absence of a capability from the rescue scope does **not** authorize deleting it from the original working repository. Reconstruction is isolated until acceptance and an explicitly approved migration.

## 3. Two complementary bodies of knowledge

### A. Abstract capability contract — what survives

Capture, independently of the original framework and language:

1. Selected intent and user-visible outcomes.
2. Inputs, outputs, data shapes, supported file formats and version constraints.
3. State machines, lifecycle, authorization, side effects and irreversible operations.
4. Errors, partial success, retries, recovery, security/privacy boundaries and performance expectations.
5. Observable accessibility and presentation semantics where applicable.
6. Golden fixtures, reference traces, adversarial tests, acceptance thresholds and known unknowns.
7. Deliberate deviations: preserved behavior versus corrected or excluded legacy behavior.

Never mistake screenshot similarity, method names, or matching data structures for semantic parity. For effects, prove authorized real consequences; for interactive systems, prove what users can perceive and do.

### B. Implementation archaeology — how it survives today

Document the original, possibly tangled implementation:

1. Reachable modules, call graphs and real data/control flow for each selected operation.
2. Runtime and build dependencies, deployment assumptions and initialization order.
3. Hidden shared mutable state, event buses, caches, filesystem/network effects and ambient globals.
4. Direct and transitive couplings to **unselected** features.
5. Failure observations, crash triggers, races, memory pressure, duplicated logic and provenance.
6. Evidence of each dependency's necessity or replaceability, with precise source references and runtime traces.
7. A staged disentanglement plan: substitute, isolate, replace, remove, or investigate further.

Proposed extraction-specific assessment labels are **essential**, **replaceable**, **extraneous**, **intermeshed** and **unresolved**. These are **research annotations**, not changes to Forever Works 0.1's normative dependency classifications (**LOCKED, SEMANTIC, CAPABILITY, TRANSITIONAL, LEGACY, OPTIONAL**). A future RFC may consider additional schema fields or record kinds only after demonstrated need, backward compatibility and conformance fixtures.

**Crucial distinction:** something that *looks* unrelated can encode essential security validation, timing, consistency or format compatibility. Require evidence before classifying it as extraneous.

## 4. Proposed workflow

**Phase 0 — Consent and scope freeze.** Identify selected capabilities, prohibited scope, target platforms, budgets, owner-approved corrections and unacceptable regressions. Define a baseline repository revision and reproducible environment.

**Phase 1 — Observe.** Execute normal and edge-case workflows of the original; capture source and runtime evidence, sample files, state transitions, outward effects and failure cases. Record failures as failures, not acceptance fixtures.

**Phase 2 — Model.** Map selected behaviors to existing Forever Works intent, capability, invariant, constraint, dependency, implementation, decision, compatibility and evidence records. Produce a portable, human-readable narrative alongside machine-readable JSON and test vectors.

**Phase 3 — Trace and slice.** Construct a selection-rooted dependency graph distinguishing actual runtime reachability, static possibility and uncertain transitive edges. Mark shared state and side effects. Identify candidate seams without deleting the original system.

**Phase 4 — Isolate incrementally.** Introduce adapters or a clean harness for external effects; substitute replaceable mechanisms; preserve behavioral fixtures. After each change, compare observable outputs, side effects, security and performance against the frozen baseline or approved correction.

**Phase 5 — Reconstitute.** Implement the selected capabilities in a minimal, independent package. Do not port unrelated UI, services or infrastructure merely because the original depended on them. Preserve only semantics shown necessary by evidence. Another implementation language/framework is an explicit option, not a mandatory rewrite.

**Phase 6 — Verify and hand off.** Compare original versus reconstruction on matched inputs and situations; audit deviations, unexpected dependencies, coverage gaps, performance and reliability. Produce an evidence-backed migration plan with reversible rollout, owner acceptance and a cold-agent handoff. Retire legacy dependencies only after signoff.

The procedure must support stopping safely when the original cannot be executed, behavior is ambiguous, licenses prohibit reuse, extraction exposes secrets or parity cannot be established.

## 5. Capability Extraction Package (CEP): suggested deliverable

A **CEP** is a portable research artifact, not a new normative Forever Works format in this proposal:

```text
capability-extraction/
├── README.md                   # scope, status, exclusions and cold-agent start
├── scope.json                  # selected capability IDs, accepted disposition
├── forever/                    # existing conforming Forever Works model
├── behavioral-contract.md      # abstract operations, invariants and user effects
├── implementation-map.md       # actual wiring, state and call/effect boundaries
├── dependency-assessment.json  # edge evidence, necessity and extraction labels
├── fixtures/                   # redacted samples and expected outputs
├── tests/                      # replayable comparative tests and harnesses
├── evidence/                   # traces, source pointers, failures, provenance
├── migration-plan.md           # seams, risks, rollback and acceptance
└── unknowns.md                 # unresolved questions, human verification
```

Canonical Forever Works records remain the source of machine-readable project semantics. The proposal should first use **existing kinds and extension fields** where appropriate, retaining provenance and unknown fields; any new public API operation or schema version requires a separate normative RFC, interoperability tests and explicit governance.

The package must say which assertions are **owner accepted**, **observed**, **inferred**, or **agent proposed**; link claims to auditable evidence; declare omissions; and avoid bundling personal or proprietary data without authorization.

## 6. Focused pilot: SUBSTRATE document functionality

**User-selected scope:** supported DOCX import, document inspection/editing, PDF display and/or generation, supported formatting preservation, and save/reopen behavior. Exact features are to be negotiated from observed implemented behavior, not assumed from product naming.

Candidate tests include:

- Given a known DOCX input, preserve accepted paragraph structure and selected formatting through an agreed edit/save/reopen cycle.
- Render PDF pages with expected page ordering, sizing and legibility at specified zoom levels.
- Export documents and verify output format validity and semantic content independent of specific library internals.
- Recover gracefully from malformed files, resource exhaustion and cancellation.
- Compare memory, load time, file correctness and crash rate against explicit budgets.
- Ensure excluded systems are genuinely absent from the reconstructed package, with transitive dependency audits.

The first pilot must **inventory what SUBSTRATE actually implements** before locking these as requirements; unsupported items remain aspirations and cannot be silently marked implemented.

## 7. Evaluation: independent reconstruction, not self-graded success

The flagship experiment has two separate agent sessions:

**Extraction agent:** studies the legacy project and assembles a CEP with verified scope, evidence and tests; does not pre-build the target reconstruction as a disguised template.

**Cold reconstruction agent:** receives the CEP and allowed reference inputs, starts with no repository-specific prior context, builds a conventional independent implementation, and runs the declared comparative tests. Record interventions, time, cost, dependency count, binary/package weight, performance, unknowns and reconstruction correctness.

A successful experiment requires:

- Selected capabilities meet agreed semantic acceptance tests and preserve real state/effects.
- Approved corrections are explicitly separated from baseline behavior.
- Extraneous legacy functionality and dependencies are absent or justified.
- Independent verification can reproduce evidence; human review gates remain when needed.
- The reconstructed code is understandable, maintainable, secure within scope and not simply a hidden wrapper around the entire legacy application.
- New agents can inherit it cold and diagnose failures without original maintainers.
- Failure and uncertainty are reported honestly; no benchmark is marked PASS by assumption.

Compare at least three strategies when possible: conventional targeted refactor, clean rewrite from informal requirements, and CEP-driven selective reconstitution. Measure both **feature fidelity** and **complexity eliminated**, without treating lines of code as a substitute for maintainability.

## 8. Relationship to other initiatives

- **Forever Works** owns durable semantics, dependency and provenance evidence, independent verification and long-lived agent handoff.
- **Any-Shape** may consume accepted extraction contracts to transfer capabilities across desktop, mobile and browser presentations; it is not required for basic extraction.
- **WebScript ICU** may contribute real interface/viewport and visual-behavior evidence when UI continuity matters; it is not a core dependency.
- Extraction may produce a same-language lean library, a cross-language reconstruction, or both.

## 9. Risks and safeguards

1. **False simplification:** deleting hidden necessary behavior; counter with differential fixtures, threat modeling and staged removal.
2. **Specification laundering:** promoting accidental bugs to requirements; counter with explicit PRESERVE/CORRECT/EXCLUDE owner review.
3. **Incomplete observability:** traces miss rare paths; counter with unknowns, fuzzing, differential tests and confidence limits.
4. **Cross-language drift:** encoding, rounding, date, IO, concurrency and library changes; counter with canonical fixtures and environment-specific adapters.
5. **Security/privacy/regulatory issues:** extracting documents, credentials and privileged workflows; counter with minimal redacted fixtures and isolated authorized testing.
6. **False 'clean-room' claims:** clean-room legal requirements vary; document provenance, licensing and access instead of asserting legal independence.
7. **Uncontrolled agent work:** bounded budgets, milestones, checkpoints, rollback, non-destructive default behavior and explicit human acceptance.

## 10. Requested research milestones

1. Publish and review this proposal; identify its relationship to existing `docs/STANDARD.md` and Public API 0.1 without breaking either.
2. Define CEP v0 as **non-normative** documentation/fixture conventions mapped to existing Forever Works records.
3. Run a tightly bounded extraction pilot on one actually working feature and create comparative fixtures.
4. Perform at least one independent cold-agent reconstruction and publish failures as well as successes.
5. Expand to intertwined Word/PDF functionality only after basic seam discovery and original behavior evidence.
6. If experiments establish portable needs not expressible in the current model, propose separately reviewed schema/API/conformance extensions.

**Research question:** Can a valuable capability escape an entangled system—and retain its meaning—without carrying that system's accidental complexity into its next life?
