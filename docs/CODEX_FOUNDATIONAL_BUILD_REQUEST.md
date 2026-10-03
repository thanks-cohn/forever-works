# Codex Foundational Build Request
## Forever Works — Language-Agnostic Longevity Standard for Agent-Maintainable Software

**Status:** Implementation request  
**Audience:** Codex / software agents implementing the first working foundation  
**Repository:** Forever Works  
**Primary objective:** Turn the foundational proposal into a working, testable, language-independent standard with initial reference implementations for TypeScript, C, and Python, followed by C++.

---

# 1. Mission

Build the first practical implementation of Forever Works.

Forever Works is intended to become a durable standard for software projects that need to remain understandable, maintainable, and modernizable across changes in languages, runtimes, frameworks, operating systems, dependencies, package managers, hardware, and development tooling.

The project must allow a future agent to understand:

- why a project exists,
- what capabilities it must preserve,
- what invariants must remain true,
- what implementation choices are temporary,
- why dependencies were chosen,
- what can be safely replaced,
- what cannot be changed without explicit architectural approval,
- how to evaluate a modernization candidate,
- and how to verify that a migration preserved the original project intent.

The project must be designed around the assumption that today's languages and ecosystems are temporary.

The standard itself must remain understandable and usable even if:

- Node.js disappears,
- npm disappears,
- Python changes substantially,
- C compilers evolve,
- today's JSON tooling changes,
- today's agent protocols disappear,
- or future software is written in languages that do not yet exist.

The implementation languages are proof vehicles.

They are not the standard.

---

# 2. Long-Term Vision

The long-term goal is:

> Any software project, written in any language, old or new, should be able to adopt a small set of Forever Works conventions and become intelligible to future software agents.

A future agent should be able to inspect a project and ask:

```text
What is this project for?
What are its enduring goals?
What must remain true?
What is merely implementation detail?
Why does this dependency exist?
What capability does this subsystem provide?
Can this library be replaced?
If so, what properties must a replacement preserve?
What compatibility boundaries must survive?
What assumptions are historical and may now be retired?
What modernization path preserves the project's identity?
```

The project should make those answers available in structured form.

The end state is not "support TypeScript, C, Python, and C++."

The end state is:

> **Define a language-neutral preservation model that can be implemented by any language, including languages that do not yet exist.**

TypeScript, C, Python, and C++ are the first proof that the standard is genuinely portable.

---

# 3. Immediate Language Targets

Implementation order:

1. **TypeScript**
2. **C**
3. **Python**
4. **C++**

Do not design the standard around TypeScript just because it is implemented first.

The canonical data model must be expressible in all four languages without distortion.

The following should remain language-neutral:

- entity names,
- identifiers,
- schemas,
- serialized formats,
- capability model,
- invariant model,
- dependency intent model,
- migration model,
- compatibility contract model,
- conformance rules,
- validation semantics.

Language bindings may differ ergonomically.

Semantics must not.

---

# 4. First Principles

Use these as architectural constraints.

## 4.1 Intent above implementation

The standard preserves:

- purpose,
- capability,
- invariant,
- constraint,
- compatibility,
- rationale.

It does not preserve obsolete machinery for its own sake.

## 4.2 Meaning must survive language changes

A record describing:

```text
Capability: streaming transfer
Invariant: bounded memory
Dependency class: CAPABILITY
```

must mean the same thing in TypeScript, C, Python, C++, and any future binding.

## 4.3 Plain formats first

The durable project record must be readable without specialized tooling.

Prefer:

- JSON for canonical machine interchange,
- JSON Schema for validation,
- YAML optionally for human-authored convenience,
- Markdown for narrative rationale.

Do not make a database, binary format, generated code, or proprietary tool mandatory.

## 4.4 Stable IDs

Every meaningful entity should support durable identifiers.

Examples:

```text
intent.remote-file-transfer
capability.streaming-transfer
invariant.bounded-memory
dependency.package-x
decision.use-wasm-core
compatibility.save-format-v1
migration.package-x-to-wasm
```

IDs must be independent of file names and language bindings.

## 4.5 Explicit provenance

The standard must distinguish:

- authored truth,
- inferred knowledge,
- imported evidence,
- agent hypothesis.

Agents must never silently convert inference into project truth.

## 4.6 Progressive adoption

A project should gain value from a minimal Forever Works model.

Do not require exhaustive architectural documentation.

## 4.7 Machine-queryable, human-readable

Every important record must be understandable by both.

## 4.8 Transport independence

Do not make MCP, HTTP, CLI, or any specific agent protocol part of the core standard.

Those are adapters.

## 4.9 Testability

Whenever possible, invariants and compatibility contracts should link to executable verification.

## 4.10 Conservative modernization

Newer technology is not automatically better.

A modernization is valid only when it preserves declared intent, capabilities, invariants, and compatibility requirements.

---

# 5. Canonical Domain Model

Create a language-neutral specification for the following entities.

## 5.1 Project Intent

Required concepts:

- id
- name
- statement
- purpose
- priorities
- non-goals
- supported environments
- status
- provenance
- related capabilities
- related constraints

## 5.2 Capability

Required concepts:

- id
- name
- statement
- inputs
- outputs
- required properties
- related invariants
- related implementations
- verification references
- criticality
- status

## 5.3 Invariant

Required concepts:

- id
- name
- statement
- scope
- verification
- thresholds
- change policy
- severity
- related capabilities
- provenance

## 5.4 Constraint

Required concepts:

- id
- statement
- category
- scope
- hard/soft classification
- verification
- rationale

## 5.5 Dependency Intent

Required concepts:

- id
- dependency name
- dependency type
- current implementation identifier/version
- purpose
- reason selected
- required capabilities
- protected invariants
- replacement classification
- replacement requirements
- compatibility obligations
- historical context
- deprecation state
- provenance

## 5.6 Architectural Decision

Required concepts:

- id
- title
- status
- context
- decision
- alternatives considered
- rationale
- assumptions
- what may change
- what must survive
- revisit conditions
- related entities
- date/version
- provenance

## 5.7 Compatibility Contract

Required concepts:

- id
- contract type
- boundary
- must preserve
- may change
- migration policy
- version
- validation references

Examples:

- API
- ABI
- file format
- save format
- command-line behavior
- protocol
- plugin interface
- database schema
- import/export format

## 5.8 Migration

Required concepts:

- id
- source implementation
- target implementation
- reason
- preserved capabilities
- preserved invariants
- compatibility impact
- assumptions retired
- tests/verification
- rollback notes
- status
- date/version
- provenance

## 5.9 Implementation

Required concepts:

- id
- type
- technology
- version
- satisfies capabilities
- constrained by invariants
- replaceability
- source locations
- runtime requirements

## 5.10 Evidence

Required concepts:

- id
- type
- source
- statement supported
- confidence
- timestamp/version
- immutable reference when possible

---

# 6. Dependency Replacement Classification

Implement the following initial classes exactly and document their semantics.

## LOCKED

The implementation itself is part of the contract.

Replacement requires an explicit architectural decision.

## SEMANTIC

Implementation may change, but externally observable semantics must remain equivalent.

## CAPABILITY

Any implementation is acceptable if declared capabilities, constraints, and invariants remain satisfied.

## TRANSITIONAL

Known temporary dependency.

Should be reconsidered when declared conditions are met.

## LEGACY

Retained solely for historical compatibility.

## OPTIONAL

Supports a nonessential feature and may be removed if that feature is intentionally removed.

These names may evolve later, but v0.1 must implement them consistently across bindings.

---

# 7. Canonical Serialized Representation

Create a versioned, language-neutral serialization format.

Recommended root manifest:

```text
forever/
  manifest.json
  project.intent.json

  capabilities/
  invariants/
  constraints/
  dependencies/
  decisions/
  compatibility/
  migrations/
  implementations/
  evidence/
```

The format must include a schema version.

Example:

```json
{
  "foreverVersion": "0.1",
  "projectId": "example-project",
  "records": {
    "intent": ["project.intent.json"],
    "capabilities": ["capabilities/streaming-transfer.json"]
  }
}
```

The exact representation may differ if a better neutral structure emerges.

Requirements:

- deterministic interpretation,
- explicit versioning,
- no language-specific type information,
- UTF-8,
- stable entity IDs,
- portable relative references,
- clear handling of unknown future fields,
- forward-compatible parsing rules where practical.

---

# 8. Schema Package

Create canonical schemas under:

```text
spec/
  manifest.schema.json
  project-intent.schema.json
  capability.schema.json
  invariant.schema.json
  constraint.schema.json
  dependency-intent.schema.json
  decision.schema.json
  compatibility-contract.schema.json
  migration.schema.json
  implementation.schema.json
  evidence.schema.json
```

Use JSON Schema.

Each schema must include:

- descriptions,
- required fields,
- enums where appropriate,
- version field,
- examples,
- extensibility guidance.

Do not over-constrain optional domain-specific extensions.

Provide a namespaced extension mechanism.

Example:

```json
{
  "extensions": {
    "com.example.performance": {
      "maxLatencyMs": 30
    }
  }
}
```

---

# 9. Canonical Intermediate Representation

Create a language-neutral in-memory model documented independently from any SDK.

Call it something neutral such as:

```text
Forever Model
```

or:

```text
Longevity Graph
```

Do not name the canonical model after TypeScript, Python, or any package.

The model should support:

- entity lookup,
- references,
- graph traversal,
- provenance,
- validation,
- relationship tracing,
- versioned serialization.

Conceptually:

```text
Intent
  ↓
Capabilities
  ↓
Invariants / Constraints
  ↓
Implementations
  ↓
Dependencies
```

But do not force a strict tree.

Use a graph.

---

# 10. Core Query Semantics

Define a transport-independent query contract.

Required conceptual operations:

```text
getProjectIntent()
listCapabilities()
listInvariants()
listConstraints()
listDependencies()
listDecisions()
listCompatibilityContracts()
listMigrations()

getEntity(id)
traceEntity(id)
traceCapability(id)
traceInvariant(id)

explainDependency(id)
findReplaceableDependencies()
findLegacyDependencies()
findTransitionalDependencies()

validateModel()
evaluateReplacement(current, candidate)
verifyMigration(migration)
```

The first implementation may expose these as library functions.

Later they may be mapped to:

- CLI,
- MCP,
- HTTP,
- IDE integration,
- CI.

The semantics should be documented independently from transport.

---

# 11. Replacement Evaluation Model

Implement a structured way to evaluate whether a candidate replacement satisfies the old implementation's role.

At minimum:

```text
current dependency
        ↓
required capabilities
protected invariants
constraints
compatibility contracts
        ↓
candidate replacement
        ↓
pass / fail / unknown per requirement
```

Do not return only a single boolean.

Return evidence.

Example:

```json
{
  "candidate": "new-streamer",
  "result": "partial",
  "checks": [
    {
      "requirement": "capability.streaming",
      "status": "pass"
    },
    {
      "requirement": "invariant.bounded-memory",
      "status": "unknown",
      "reason": "No benchmark evidence supplied"
    }
  ]
}
```

The system must prefer `unknown` over invented certainty.

---

# 12. Verification Model

Define a neutral verification record.

Potential verification types:

- unit test
- integration test
- benchmark
- static analysis
- manual review
- compatibility fixture
- file corpus
- protocol test
- runtime probe
- external conformance suite

Do not assume one testing framework.

A record should describe:

- what is being verified,
- how,
- expected result,
- optional command,
- optional tool,
- environment requirements,
- evidence location.

---

# 13. Provenance Model

Every significant statement should be able to carry provenance.

Support at least:

```text
explicit
inferred
imported
historical
agent-proposed
```

Recommended fields:

- source type
- source reference
- author/agent identifier
- confidence
- created at
- last reviewed at
- review status

Rules:

- explicit requirements outrank inference,
- inferred records must remain visibly inferred,
- confidence must not be silently promoted,
- agent-generated proposals should require explicit acceptance before becoming authoritative.

---

# 14. TypeScript Reference Implementation

Create:

```text
packages/typescript/
```

Responsibilities:

- load Forever Works manifests,
- validate schemas,
- expose typed domain objects,
- build the graph,
- run core queries,
- serialize canonically,
- evaluate replacement records,
- validate migrations.

Do not place canonical semantics only in TypeScript comments.

Anything required to implement another binding must also exist in `spec/` or `docs/`.

Provide both:

- ESM support,
- JavaScript-compatible runtime API.

A plain JavaScript project should be able to use the TypeScript implementation's compiled package.

---

# 15. C Reference Implementation

Create:

```text
bindings/c/
```

The C binding is essential because it tests whether the standard is genuinely language-independent.

Goals:

- parse canonical model files,
- validate required structure,
- expose stable C structs or opaque handles,
- query records by ID,
- traverse core relationships,
- report validation errors,
- serialize model data.

Avoid exotic dependencies.

Prefer portability.

Support at least:

- C11 or later,
- common desktop compilers.

Do not require the C binding to duplicate every convenience API from TypeScript.

It must prove semantic equivalence.

---

# 16. Python Reference Implementation

Create:

```text
bindings/python/
```

Goals:

- canonical model loading,
- schema validation,
- domain objects,
- graph traversal,
- query API,
- replacement evaluation,
- migration validation,
- CLI integration where useful.

Use standard Python packaging.

Avoid designing Python behavior that diverges from the specification.

---

# 17. C++ Follow-On Design

Prepare but do not necessarily fully implement until TypeScript, C, and Python conformance is working.

Expected location:

```text
bindings/cpp/
```

C++ should either:

- wrap the C implementation with safer idiomatic types,
- or implement the same spec independently if there is a strong technical reason.

Document the decision.

The C/C++ relationship itself should demonstrate Forever Works principles.

---

# 18. Conformance Test Suite

This is mandatory.

Create:

```text
conformance/
  fixtures/
  expected/
  tests/
```

The same fixtures must be consumable by every language binding.

Required fixture classes:

- minimal valid project,
- complete project,
- invalid missing ID,
- invalid reference,
- unknown future field,
- dependency replacement example,
- migration preserving invariants,
- migration violating invariant,
- compatibility contract example,
- inferred provenance example,
- circular relationship example,
- old schema version fixture.

Each binding should prove it interprets the same records consistently.

The conformance suite is more important than language-specific ergonomics.

---

# 19. Golden Files

Create canonical golden JSON outputs.

Given the same model, TypeScript, C, and Python should produce semantically equivalent normalized output.

Define normalization rules.

Examples:

- deterministic record ordering,
- deterministic key ordering for canonical output,
- stable ID references,
- normalized paths.

This creates an implementation-independent truth source.

---

# 20. CLI

Create an initial CLI, probably implemented first in TypeScript or Python, but define the command semantics independently.

Required commands:

```text
forever init
forever validate
forever inspect
forever explain <id>
forever trace <id>
forever audit
```

Useful later:

```text
forever evaluate-replacement
forever plan-migration
forever verify-migration
forever normalize
forever export
```

The CLI must operate entirely on canonical project files.

Do not make the CLI's implementation language part of the project format.

---

# 21. `forever init`

Implement a minimal initializer.

It should create:

```text
forever/
  manifest.json
  project.intent.json
  capabilities/
  invariants/
  constraints/
  dependencies/
  decisions/
  compatibility/
  migrations/
  implementations/
  evidence/
```

It should not fabricate architectural facts.

Use clear TODO placeholders where the project author must provide intent.

---

# 22. Audit Command

The initial audit command should inspect the Forever Works model itself.

It should identify:

- broken references,
- missing provenance,
- capabilities with no implementation,
- dependencies with no declared purpose,
- invariants with no verification,
- compatibility contracts with no validation,
- transitional dependencies with no revisit condition,
- migrations with unverified requirements.

Do not yet attempt deep source-code inference unless clearly separated as experimental.

---

# 23. Agent-Facing Output

Commands should support structured JSON output.

Example:

```bash
forever explain dependency.package-x --json
```

This is essential for agent use.

Human-readable output should also exist.

Never require an agent to scrape prose when structured output is available.

---

# 24. Documentation

Create professional documentation including:

```text
docs/
  FOUNDATIONAL_PROPOSAL.md
  STANDARD.md
  DATA_MODEL.md
  FILE_FORMAT.md
  CONFORMANCE.md
  AGENT_PROTOCOL.md
  MIGRATION_MODEL.md
  DEPENDENCY_CLASSIFICATION.md
  PROVENANCE.md
  LANGUAGE_BINDINGS.md
  ROADMAP.md
```

Do not duplicate semantics inconsistently across documents.

The specification should be authoritative.

---

# 25. AGENTS.md

Create a root `AGENTS.md`.

It should tell future coding agents:

- read the foundational proposal first,
- preserve language neutrality,
- do not introduce a language-specific assumption into the canonical spec,
- update conformance fixtures when semantics change,
- never treat inferred intent as authoritative,
- prefer backward-compatible schema evolution,
- keep the standard transport-independent,
- preserve the distinction between requirement and implementation,
- add rationale for new foundational dependencies,
- keep the core model understandable without proprietary tools.

---

# 26. Repository Structure

Populate the repository approximately as follows:

```text
/
├── README.md
├── AGENTS.md
├── LICENSE
├── CONTRIBUTING.md
│
├── spec/
│   ├── schemas/
│   ├── examples/
│   └── VERSIONING.md
│
├── docs/
│   ├── FOUNDATIONAL_PROPOSAL.md
│   ├── STANDARD.md
│   ├── DATA_MODEL.md
│   ├── FILE_FORMAT.md
│   ├── CONFORMANCE.md
│   ├── AGENT_PROTOCOL.md
│   ├── MIGRATION_MODEL.md
│   ├── DEPENDENCY_CLASSIFICATION.md
│   ├── PROVENANCE.md
│   ├── LANGUAGE_BINDINGS.md
│   └── ROADMAP.md
│
├── packages/
│   ├── core/
│   ├── typescript/
│   └── cli/
│
├── bindings/
│   ├── c/
│   ├── python/
│   └── cpp/
│
├── conformance/
│   ├── fixtures/
│   ├── expected/
│   └── README.md
│
├── examples/
│   ├── minimal/
│   ├── typescript/
│   ├── c/
│   └── python/
│
└── scripts/
```

Adjust where technically justified.

Keep the conceptual separation.

---

# 27. Core Package Independence

If a shared core implementation is created, it must not make the canonical specification dependent on it.

The source of truth hierarchy should be:

```text
1. specification
2. schemas / conformance fixtures
3. reference implementations
4. convenience tooling
```

Not:

```text
TypeScript implementation
        ↓
everyone else must copy it
```

---

# 28. Schema Evolution Rules

Document versioning from the beginning.

Requirements:

- explicit schema version,
- unknown-field tolerance where safe,
- major-version signaling for incompatible semantics,
- migrations between known schema versions,
- old fixtures retained for regression testing.

The standard is specifically about longevity.

Its own data model must therefore be designed for longevity.

---

# 29. Self-Hosting Requirement

Forever Works should eventually describe itself.

As soon as the schemas are stable enough, add a `forever/` directory to this repository describing:

- Forever Works project intent,
- its core capabilities,
- its invariants,
- dependency rationale,
- compatibility expectations,
- architectural decisions.

This is an important proof.

The standard should be capable of preserving the reasoning behind its own implementation.

---

# 30. Example Self-Hosted Invariants

Potential initial Forever Works invariants:

```text
invariant.language-neutral-core
The canonical standard must not require a specific programming language.

invariant.plain-readable-format
Core project records must remain readable using open, documented formats.

invariant.agent-independent
No particular AI provider or agent protocol may be required.

invariant.binding-conformance
All reference bindings must interpret canonical fixtures equivalently.

invariant.provenance-preserved
Inferred intent may not become authoritative without explicit acceptance.

invariant.backward-aware
Schema evolution must provide an explicit compatibility story.
```

---

# 31. First Proof Project

Create at least one complete example project.

The example should include:

- project intent,
- capabilities,
- invariants,
- dependencies,
- compatibility contract,
- architectural decision,
- migration.

Suggested scenario:

```text
A file transfer utility originally uses an old Node streaming dependency.

Its enduring requirement is:
- remote streaming
- bounded memory
- resumability

A hypothetical future implementation replaces that dependency with a WebAssembly-based streaming engine.

Forever Works should show why the replacement is acceptable.
```

This directly demonstrates the foundational vision.

---

# 32. Replacement Evaluation Proof

The first proof should allow:

```text
forever evaluate-replacement dependency.old-streamer candidate.wasm-streamer
```

and return:

```text
PASS
  streaming capability

PASS
  resumability

UNKNOWN
  bounded memory
  benchmark evidence missing

PASS
  configuration compatibility

RESULT
  Candidate not yet verified.
```

This demonstrates that the standard preserves reason rather than merely package names.

---

# 33. No False Certainty

Codex must implement three-valued or richer evaluation where appropriate.

At minimum:

- pass
- fail
- unknown

Optional:

- not-applicable
- waived
- pending-review

Never infer pass simply because no failure is known.

---

# 34. Source Analysis: Defer Deep Automation

Do not make automated code understanding the first milestone.

First prove that explicitly authored Forever Works records work.

After the standard is stable, agents can propose records based on:

- source analysis,
- dependency manifests,
- tests,
- benchmarks,
- commit history.

But the project must remain useful even without those features.

---

# 35. C as a Design Test

Treat C as a deliberate stress test.

If the canonical model becomes difficult to represent in C without reproducing TypeScript-specific concepts, revisit the model.

The goal is not to make C elegant.

The goal is to prove the standard is not accidentally tied to dynamic objects, classes, promises, decorators, or package ecosystems.

---

# 36. Future Unknown Languages

Document a binding contract for languages that do not yet exist.

The document should explain:

> To implement a Forever Works binding, a language needs only to support reading the canonical serialized form, representing records and references, validating required semantics, and exposing the defined query behavior.

This is critical.

The standard must not be described as:

> a TypeScript API with ports.

It is:

> a language-neutral specification with reference bindings.

---

# 37. Old and Extinct Languages

The architecture should also support adapters for old or uncommon languages.

A language does not need an official SDK to participate.

Possible integration modes:

1. native binding,
2. FFI to C,
3. CLI subprocess,
4. reading/writing canonical JSON,
5. external agent adapter.

This should be documented explicitly.

A COBOL, Pascal, Fortran, Lisp, or future language project should theoretically be able to adopt Forever Works without changing the standard.

---

# 38. Minimal Portable Interop Layer

Design a lowest-common-denominator integration path.

At minimum, every language should be able to participate by:

```text
read JSON
write JSON
invoke CLI
consume JSON result
```

This guarantees a fallback even when no native binding exists.

Later, faster/native integrations may be added.

---

# 39. API Stability Philosophy

Do not prematurely freeze convenience APIs.

Stabilize in this order:

1. semantic model
2. serialized formats
3. conformance behavior
4. query semantics
5. language APIs

Language APIs can evolve while the durable standard matures.

---

# 40. Initial Milestones

## Milestone 0 — Repository foundation

- root docs,
- AGENTS.md,
- license,
- contribution guide,
- build/test scripts,
- CI,
- folder structure.

## Milestone 1 — Specification

- canonical entities,
- JSON Schemas,
- versioning rules,
- examples.

## Milestone 2 — TypeScript reference

- parser,
- validator,
- graph,
- query API,
- serializer.

## Milestone 3 — CLI

- init,
- validate,
- inspect,
- explain,
- trace,
- audit.

## Milestone 4 — Conformance fixtures

- valid/invalid/golden cases.

## Milestone 5 — C binding

- parse,
- validate,
- query,
- serialize,
- conformance tests.

## Milestone 6 — Python binding

- equivalent semantics,
- conformance tests.

## Milestone 7 — Replacement evaluation

- pass/fail/unknown requirements,
- evidence links.

## Milestone 8 — Migration verification

- before/after preservation checks.

## Milestone 9 — Self-host Forever Works

- repository adopts its own model.

## Milestone 10 — C++ binding

- implement after semantics have survived TS/C/Python.

---

# 41. Acceptance Criteria for the First Major Foundation

The foundation is successful when all of the following are true:

1. A user can initialize a Forever Works model in an arbitrary repository.
2. The model uses canonical language-independent files.
3. TypeScript can load and query the model.
4. C can load and query the same fixtures.
5. Python can load and query the same fixtures.
6. All bindings pass the same conformance cases.
7. The CLI can explain why a dependency exists.
8. The CLI can trace a dependency to capabilities and invariants.
9. A replacement candidate can be evaluated without pretending unknown evidence is known.
10. A migration record can demonstrate which requirements were preserved.
11. The Forever Works repository describes itself using its own format.
12. No canonical concept requires knowledge of TypeScript, npm, Node.js, Python packaging, or a particular AI agent.

---

# 42. Implementation Discipline

Codex should work incrementally.

For each foundational semantic decision:

1. update specification,
2. update schema,
3. update conformance fixtures,
4. update reference implementations,
5. update documentation.

Do not allow one language implementation to drift ahead semantically without reflecting the standard.

---

# 43. Dependency Discipline

Forever Works should have few foundational dependencies.

For every nontrivial dependency introduced into the project itself, record:

- why it is needed,
- whether it is replaceable,
- what capability it provides.

This repository should model the behavior it promotes.

---

# 44. Testing Requirements

Required test categories:

- schema validation,
- cross-reference resolution,
- graph traversal,
- invalid references,
- unknown fields,
- future schema version behavior,
- serialization normalization,
- replacement evaluation,
- migration verification,
- conformance across bindings.

Where possible, share test fixture inputs across languages.

---

# 45. CI Requirements

Set up CI to run:

- schema validation,
- TypeScript tests,
- C build/tests,
- Python tests,
- cross-binding conformance checks.

C++ should be added when that binding begins.

CI should fail if a canonical fixture is interpreted inconsistently.

---

# 46. Documentation Tone

The project should be professional and standards-oriented.

Avoid framing the work as magical immortality.

Be precise.

Forever Works does not promise that software literally lasts forever.

It provides infrastructure for:

- preserving architectural meaning,
- reducing future reverse engineering,
- guiding modernization,
- verifying continuity.

---

# 47. North Star

The north star is:

> A sufficiently capable future agent should be able to inherit a project without its original author and still understand what the project was trying to preserve.

And:

> A future technology should be able to replace an obsolete implementation without erasing the reason the old implementation existed.

---

# 48. Final Instruction to Codex

Populate this repository with the complete first foundation necessary to make that vision demonstrably real.

Do not merely scaffold empty directories.

Implement the smallest coherent end-to-end system that proves the standard:

```text
author intent
      ↓
canonical format
      ↓
validation
      ↓
language-independent graph
      ↓
TypeScript / C / Python interpretation
      ↓
agent-readable query
      ↓
replacement evaluation
      ↓
migration preservation evidence
```

Keep the architecture ready for C++ next.

Keep the standard ready for every language after that.

The first three bindings are demonstrations.

The specification is the product.
