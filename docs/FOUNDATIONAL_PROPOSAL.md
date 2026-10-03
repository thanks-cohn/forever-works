# Forever Works
## Foundational Proposal for Long-Lived, Agent-Maintainable Software

**Status:** Foundational proposal  
**Project:** Forever Works  
**Scope:** Language-, framework-, runtime-, platform-, and vendor-agnostic  
**Primary objective:** Establish a durable standard that allows present and future software agents to understand, maintain, modernize, and migrate software while preserving the project's original intent, essential capabilities, constraints, and design reasoning.

---

# 1. Executive Summary

Software rarely becomes obsolete because its purpose stops mattering.

It becomes obsolete because the environment around it changes.

Libraries disappear. Runtimes deprecate APIs. Operating systems change. Browsers evolve. Build systems are replaced. Security expectations increase. Package managers change. Hardware assumptions shift. Programming languages fall out of common use. Services close. File formats are superseded. Frameworks are abandoned.

A project may still be conceptually valuable while the technical assumptions that once made it work no longer exist.

Today, preserving such a project usually requires a future maintainer to reconstruct its intent from incomplete evidence:

- source code,
- comments,
- commit history,
- old documentation,
- dependency manifests,
- tests,
- issue trackers,
- and institutional memory.

That reconstruction is often difficult even for the original authors. Decades later, it can become nearly impossible.

Forever Works proposes a different model.

A project should carry a structured, machine-readable description of:

- why it exists,
- what outcomes it is meant to produce,
- which capabilities are essential,
- which behaviors are contractual,
- which constraints must remain true,
- which implementation choices are replaceable,
- why dependencies were selected,
- what tradeoffs were intentionally accepted,
- how components relate to project goals,
- and how modernization should be evaluated.

This creates a durable layer above source code.

The implementation may change.

The purpose should not be lost.

The long-term ambition is to make agent-assisted software preservation and modernization a normal property of well-designed software.

---

# 2. Mission Statement

> **Forever Works exists to make software understandable across time.**

Its mission is to establish a portable standard through which a software project can explain its own purpose, architecture, invariants, capabilities, dependencies, tradeoffs, and modernization boundaries to any sufficiently capable future agent.

The goal is not to freeze software in its original form.

The goal is to preserve what matters while allowing everything else to evolve.

Forever Works should make it possible for a future agent to answer questions such as:

- Why does this dependency exist?
- What capability does it provide?
- Is that dependency essential, or merely the current implementation?
- What project goal does this subsystem serve?
- Which performance characteristics must be preserved?
- Which compatibility assumptions may be retired?
- What behavior must remain unchanged?
- What may safely be redesigned?
- If a runtime becomes obsolete, what replacement would preserve the original purpose?
- If a new technology provides a better implementation, does it satisfy the original constraints?
- What would constitute a true modernization rather than an accidental regression?

---

# 3. Vision

The vision is software that can participate in its own long-term preservation.

A project adopting Forever Works should become progressively easier for future agents to understand and modernize.

The desired future experience is:

```text
Agent opens project
        ↓
Reads Forever Works model
        ↓
Understands project purpose
        ↓
Traces capabilities to implementations
        ↓
Identifies obsolete or fragile components
        ↓
Finds modernization candidates
        ↓
Checks candidates against invariants
        ↓
Produces migration plan
        ↓
Implements changes
        ↓
Verifies original intent is still satisfied
```

The future agent should not need to guess why something exists simply because the original implementation is old.

The project itself should explain enough of its reasoning to make safe evolution possible.

---

# 4. Foundational Principle

The project is based on one central distinction:

> **Implementation is temporary. Intent can be durable.**

A dependency is not necessarily architecture.

A framework is not necessarily architecture.

A runtime is not necessarily architecture.

A database engine is not necessarily architecture.

A rendering library is not necessarily architecture.

A particular implementation may have been chosen only because it was the best available mechanism at the time.

Forever Works therefore separates enduring meaning from temporary mechanism.

A project should be able to state:

```text
What must survive?
What may change?
Why does this exist?
What capability does it provide?
What constraint does it protect?
How can a replacement prove equivalence?
```

---

# 5. The Problem Forever Works Solves

Modern software documentation usually describes one or more of the following:

- how to build the software,
- how to run it,
- how to call its APIs,
- how components are organized,
- how to contribute,
- or what a dependency currently does.

That is useful, but incomplete for long-term preservation.

Consider a project that uses an old Node.js package for streaming large files.

A dependency manifest might preserve:

```text
package-x: ^4.2.1
```

A comment might say:

```text
Used for streaming.
```

That is not enough.

A future agent needs the deeper reason:

```text
Purpose:
Transfer large files without buffering them fully into memory.

Constraint:
The software must remain usable on memory-constrained machines.

Required properties:
- streaming
- backpressure
- bounded memory
- resumability

Replacement policy:
The current package is replaceable.
Any replacement is acceptable if it preserves these properties.
```

If package-x later disappears, the agent does not need to preserve the package.

It needs to preserve the capability and constraint.

That is the difference between preserving an implementation and preserving a project.

---

# 6. Core Model

Forever Works should standardize a small set of durable concepts.

## 6.1 Intent

**Intent** describes why the project or subsystem exists.

Examples:

- allow users to move remote files without downloading them locally,
- run acceptably on low-memory hardware,
- preserve user-created worlds across versions,
- make a document readable without proprietary software,
- support offline operation.

Intent answers:

> Why does this matter?

---

## 6.2 Capability

A **Capability** describes something the project must be able to do.

Examples:

- stream remote data,
- render a 3D world,
- serialize project state,
- authenticate a user,
- export a document,
- resume an interrupted upload.

Capability answers:

> What must the system be capable of?

---

## 6.3 Invariant

An **Invariant** describes a property that must remain true across implementations.

Examples:

- peak memory must remain below a defined threshold,
- files must not be modified during inspection,
- public API identifiers must remain stable,
- a saved project must remain readable by future versions,
- user actions must be undoable,
- the application must function without a specific vendor.

Invariant answers:

> What must remain true?

---

## 6.4 Implementation

An **Implementation** describes how a capability is currently realized.

Examples:

- Node.js package X,
- SQLite,
- WebAssembly module,
- React component,
- C++ subsystem,
- Cloudflare R2,
- browser IndexedDB.

Implementation answers:

> How do we currently accomplish it?

Implementations should generally be considered replaceable unless explicitly declared otherwise.

---

## 6.5 Rationale

**Rationale** explains why an implementation or architectural decision was chosen.

Examples:

- lower memory usage,
- browser portability,
- deterministic execution,
- simpler deployment,
- compatibility with existing data,
- avoidance of vendor lock-in.

Rationale answers:

> Why was this decision reasonable at the time?

---

## 6.6 Constraint

A **Constraint** limits acceptable implementations.

Examples:

- must work offline,
- must support a 4 GB machine,
- must run in a browser sandbox,
- must avoid proprietary formats,
- must keep startup below two seconds.

Constraints may be technical, operational, legal, product-related, or user-experience-related.

---

## 6.7 Dependency Intent

A **Dependency Intent** record explains why an external dependency exists and what would be required to replace it.

This is a critical primitive.

A future agent should be able to distinguish:

```text
"This library is fundamental to the product"
```

from:

```text
"This library was simply the easiest available way to satisfy capability X in 2026."
```

---

## 6.8 Decision

A **Decision** records a meaningful architectural choice.

Forever Works decisions should extend ordinary Architecture Decision Records by explicitly including:

- the context,
- the chosen approach,
- rejected alternatives,
- reasons,
- assumptions,
- what may change,
- what must survive,
- and conditions under which the decision should be revisited.

---

## 6.9 Migration

A **Migration** describes how one implementation is replaced by another while preserving declared intent, capabilities, and invariants.

A migration record should explain:

- what is changing,
- why change is needed,
- what remains unchanged,
- what risks exist,
- how equivalence will be tested,
- and whether any old assumptions can be retired.

---

# 7. Preserve the Upper Graph, Replace the Leaves

A useful mental model for Forever Works is a graph.

```text
PROJECT INTENT
     │
     ▼
CAPABILITY
     │
     ▼
INVARIANT / CONSTRAINT
     │
     ▼
ABSTRACTION
     │
     ▼
CURRENT IMPLEMENTATION
     │
     ▼
DEPENDENCY / LIBRARY / RUNTIME
```

The upper parts of this graph often represent the enduring project.

The lower parts often represent the technology available at a particular moment in history.

The guiding principle is:

> **Preserve the upper graph. Replace the leaves when necessary.**

If an obsolete package disappears, the project should not lose its purpose.

The dependency node changes.

The capability and invariant remain.

---

# 8. Example

Consider a file-transfer project.

A naive record might say:

```text
Dependency: package-x
```

A Forever Works record should be closer to:

```yaml
dependency: package-x
classification: capability

purpose:
  Stream large remote files to a destination.

reason_selected:
  Supported streaming and backpressure with low implementation complexity.

required_capabilities:
  - streaming
  - backpressure
  - resumable transfers

protected_invariants:
  - bounded-memory-transfer
  - no-required-local-download

replaceable: true

replacement_requirements:
  - preserve streaming
  - preserve bounded memory
  - preserve current retry semantics
  - support target platforms

historical_context:
  Chosen because it was a stable implementation available at the time.
```

A future agent can now evaluate alternatives correctly.

---

# 9. Dependency Classification

Forever Works should define a small replacement classification system.

Suggested classes:

## LOCKED

The implementation itself is part of the contract.

Replacement requires an explicit architectural decision.

Example:

- cryptographic format required by an external standard,
- mandated interoperability protocol,
- binary compatibility boundary.

## SEMANTIC

The implementation may change, but externally visible behavior must remain equivalent.

Example:

- parser,
- serialization library,
- UI state engine.

## CAPABILITY

Any implementation is acceptable if declared capabilities and invariants are preserved.

Example:

- file streaming library,
- HTTP client,
- image-processing backend.

## TRANSITIONAL

The dependency is known to be temporary.

It should be actively reconsidered when a declared condition becomes true.

## LEGACY

The dependency exists solely to maintain compatibility with historical data, APIs, or environments.

## OPTIONAL

The dependency supports a nonessential feature and may disappear if that feature is intentionally removed.

This classification gives future agents an immediate estimate of how much freedom they have.

---

# 10. Project-Level Intent Model

Every adopting project should be able to define a top-level intent document.

Conceptually:

```json
{
  "project": "example-project",
  "purpose": [
    "Allow remote files to be moved without requiring local download"
  ],
  "priorities": [
    "portability",
    "bounded memory",
    "long-term maintainability"
  ],
  "nonGoals": [
    "permanent dependence on a specific cloud vendor"
  ],
  "supportedEnvironments": [
    "modern browser",
    "low-memory desktop"
  ]
}
```

The exact schema may evolve, but the concept should remain stable.

---

# 11. Invariants as Executable Knowledge

Whenever possible, invariants should be testable.

Example:

```yaml
id: bounded-memory-transfer

statement:
  Large file transfers must not require loading the full file into memory.

verification:
  type: benchmark
  threshold:
    peak_memory_mb: 256

scope:
  - remote-transfer
  - upload

change_policy:
  implementation may change
  invariant may not
```

This creates an important bridge between documentation and verification.

An invariant is stronger when an agent can test it.

---

# 12. Agent Interface

Forever Works should eventually expose a stable agent-facing query surface.

Conceptual operations:

```text
getProjectIntent()
listCapabilities()
listInvariants()
listConstraints()

explainComponent(component)
explainDependency(dependency)

traceCapability(capability)
traceInvariant(invariant)
traceDecision(decision)

findReplaceableDependencies()
findLegacyDependencies()
findUnverifiedAssumptions()

evaluateReplacement(current, candidate)
createMigrationPlan(target)
verifyMigration(plan)
verifyIntentPreservation()
```

This interface should remain transport-independent.

It may later be exposed through:

- CLI,
- JSON-RPC,
- MCP,
- HTTP,
- local agent protocol,
- IDE integrations,
- CI systems,
- or future agent standards.

The durable standard is the model, not a particular transport.

---

# 13. Modernization Workflow

A future modernization cycle could look like this:

```text
1. Agent detects obsolete dependency.

2. Agent asks Forever Works:
   Why is this dependency present?

3. Forever Works returns:
   capability
   rationale
   protected invariants
   compatibility requirements
   replacement policy

4. Agent identifies candidate replacements.

5. Candidate is evaluated against:
   capabilities
   invariants
   constraints
   project priorities

6. Agent generates migration plan.

7. Migration is implemented.

8. Tests and verification run.

9. Forever Works records:
   old implementation
   new implementation
   reason for migration
   preserved invariants
   retired assumptions
```

This turns modernization into a traceable preservation process rather than a sequence of guesses.

---

# 14. Language Independence

Forever Works must not depend on one programming language.

The standard should be usable by projects written in:

- JavaScript,
- TypeScript,
- Python,
- C,
- C++,
- Rust,
- Go,
- Java,
- WebAssembly,
- or future languages.

The durable representation should therefore use neutral formats.

Likely foundational formats:

- JSON,
- JSON Schema,
- YAML where human editing is useful,
- Markdown for narrative rationale.

Language-specific libraries should be optional conveniences.

The project model should remain intelligible even if its original implementation language becomes uncommon.

---

# 15. Framework and Runtime Independence

The standard must not assume that today's platforms remain dominant.

Forever Works should avoid embedding durable meaning in:

- npm,
- Node.js,
- React,
- browser APIs,
- GitHub,
- Docker,
- Cloudflare,
- any specific compiler,
- any specific model provider.

Adapters may integrate with those technologies.

The standard itself should outlive them.

---

# 16. Repository Convention

An adopting project might contain:

```text
forever/
├── project.intent.json
├── capabilities/
├── invariants/
├── constraints/
├── dependencies/
├── decisions/
├── migrations/
└── compatibility/
```

Example:

```text
forever/
├── project.intent.json
│
├── capabilities/
│   ├── streaming-transfer.json
│   └── offline-mode.json
│
├── invariants/
│   ├── bounded-memory.json
│   └── stable-save-format.json
│
├── dependencies/
│   └── package-x.json
│
├── decisions/
│   └── 0001-use-wasm-core.md
│
└── migrations/
    └── 2032-package-x-to-wasm.md
```

The exact layout should remain configurable, but the conceptual entities should be standardized.

---

# 17. CLI Vision

A future CLI could expose:

```bash
forever init
forever inspect
forever explain <dependency-or-component>
forever trace <capability>
forever verify
forever audit
forever plan-modernization
```

Possible interactions:

```text
$ forever explain package-x

Purpose:
  Stream remote files.

Protected invariants:
  bounded-memory-transfer
  resumable-transfer

Replacement classification:
  CAPABILITY

Replaceable:
  yes

Current risk:
  package no longer maintained
```

This makes architectural memory directly accessible.

---

# 18. Automatic Discovery

The long-term system should help generate and maintain the model.

An agent may inspect:

- source code,
- package manifests,
- imports,
- build files,
- runtime configuration,
- tests,
- comments,
- commit history,
- issue history,
- benchmarks.

It can propose records such as:

```text
I believe package-x exists to provide streaming transfer.
I found tests suggesting memory usage is important.
Should this be recorded as a protected invariant?
```

Human confirmation should be encouraged for architectural intent.

The system should distinguish:

- explicitly authored truth,
- inferred knowledge,
- historical evidence,
- agent hypotheses.

Forever Works should never silently convert uncertain inference into permanent architectural fact.

---

# 19. Provenance and Confidence

Every important record should be able to carry provenance.

Example:

```json
{
  "statement": "Transfers must use bounded memory.",
  "status": "explicit",
  "source": "project-author",
  "confidence": 1.0
}
```

An inferred record might instead say:

```json
{
  "statement": "This dependency may exist primarily for retry behavior.",
  "status": "inferred",
  "evidence": [
    "tests/transfer-retry.test.ts",
    "commit abc123"
  ],
  "confidence": 0.72
}
```

This prevents future agents from confusing conjecture with intent.

---

# 20. Compatibility Contracts

Long-lived software often survives because its boundaries remain understandable.

Forever Works should allow projects to record compatibility contracts such as:

- save-file formats,
- network protocols,
- ABI boundaries,
- public APIs,
- command-line behavior,
- data schemas,
- plugin interfaces,
- file extensions,
- import/export behavior.

Example:

```yaml
id: project-save-format-v1

type: data-format

must_preserve:
  - existing files remain readable

may_change:
  - internal parser
  - storage implementation

migration_policy:
  automatic upgrades allowed
  destructive conversion forbidden
```

---

# 21. Modernization Is Not Automatically Improvement

A newer technology is not inherently better for a given project.

A replacement may be newer while violating the original project goals.

Examples:

- lower developer effort but much higher memory usage,
- newer framework but larger runtime footprint,
- faster implementation but loss of offline capability,
- modern cloud service but stronger vendor lock-in,
- cleaner API but broken compatibility.

Forever Works therefore evaluates modernization against project intent.

The relevant question is not:

> Is this newer?

It is:

> Does this better satisfy the project's enduring goals while preserving required behavior and constraints?

---

# 22. Project Identity Across Rewrites

A sufficiently old project may eventually be rewritten almost completely.

Forever Works should help answer:

> Is this still the same project?

A project can preserve continuity even when its implementation changes dramatically if its enduring intent, capabilities, user-facing contracts, data compatibility, and protected invariants remain traceable.

This makes the Forever Works model a form of architectural identity.

---

# 23. Relationship to Testing

Tests answer:

> Does the implementation currently behave as expected?

Forever Works answers:

> Why is that behavior important, and what is allowed to change?

The two should reinforce one another.

A Forever Works invariant may reference a test.

A migration may require specific test suites.

An agent may generate new tests when an invariant lacks verification.

The long-term goal is for important architectural knowledge to become executable wherever practical.

---

# 24. Relationship to Documentation

Forever Works does not replace ordinary documentation.

README files, API docs, architecture guides, comments, tutorials, and user manuals remain valuable.

Forever Works adds another layer:

> durable machine-readable architectural intent.

Narrative documentation explains.

Forever Works traces.

The two should link to one another.

---

# 25. Relationship to Version Control

Version control preserves what changed.

Forever Works should preserve why important changes happened and what those changes were required to preserve.

A migration record could reference:

- previous commit,
- new commit,
- retired dependency,
- introduced dependency,
- preserved invariants,
- updated assumptions.

This creates a semantic history above the commit graph.

---

# 26. Relationship to ICU and Perceptual Tooling

Forever Works and an interface-observation standard such as ICU solve different but complementary problems.

A perceptual interface utility answers:

> What is the user seeing now?

Forever Works answers:

> Why is the project built this way, and what must survive change?

Together, future agents could understand both:

```text
present behavior
+
historical intent
```

That creates a much stronger basis for autonomous maintenance.

---

# 27. Security and Safety

A modernization agent should not receive unlimited authority merely because it understands the architecture.

Forever Works should separate:

- understanding,
- planning,
- verification,
- mutation.

The standard should support policies such as:

- read-only inspection,
- proposal-only modernization,
- migration requiring approval,
- protected components,
- immutable compatibility contracts,
- required verification before merge.

Architectural understanding should increase safety, not bypass governance.

---

# 28. Design Principles

The standard should follow these principles.

## Portable

A project should remain understandable outside the tooling that created the records.

## Plain

Core files should use durable, inspectable formats.

## Minimal

Projects should be able to adopt Forever Works gradually.

## Extensible

Specialized domains should be able to add custom capability and invariant types.

## Explicit

The standard should distinguish facts, requirements, assumptions, and inference.

## Testable

Important invariants should be machine-verifiable whenever feasible.

## Agent-Friendly

The model should support direct structured queries.

## Human-Readable

A human maintainer should be able to inspect and edit the model without proprietary tooling.

## Vendor-Neutral

No company, model, cloud, framework, or runtime should be required for the standard to remain useful.

## Long-Lived

Durable meaning must not depend on transient implementation details.

---

# 29. Adoption Philosophy

Adoption should be progressive.

A project should not need to fully model its architecture before gaining value.

A minimal adoption might define only:

```text
project intent
three important invariants
critical dependencies
one architectural decision
```

Over time the model becomes richer.

Eventually agents may help maintain it automatically.

The standard should reward partial adoption rather than require perfection.

---

# 30. Initial Implementation Roadmap

## Phase 1 — Specification

Define JSON schemas for:

- project intent,
- capability,
- invariant,
- constraint,
- dependency intent,
- architectural decision,
- migration,
- compatibility contract.

## Phase 2 — Core library

Create a language-neutral core implementation capable of:

- loading records,
- validating schemas,
- linking entities,
- tracing relationships,
- generating a project graph.

## Phase 3 — CLI

Implement:

```text
init
inspect
validate
explain
trace
audit
```

## Phase 4 — Agent protocol

Expose structured operations for agent use.

## Phase 5 — Project analysis

Add optional discovery tools capable of proposing:

- undocumented dependencies,
- implicit invariants,
- stale assumptions,
- obsolete components.

## Phase 6 — Modernization planning

Allow agents to evaluate replacement candidates against:

- capability requirements,
- invariants,
- constraints,
- compatibility contracts.

## Phase 7 — Migration verification

Create standardized before/after evidence showing that modernization preserved declared intent.

---

# 31. Example Future Scenario

Imagine a project written in 2026.

It depends on:

- Node.js,
- several npm packages,
- a browser API,
- a cloud storage provider.

In 2041, several of these technologies are obsolete.

A future agent opens the project.

Instead of seeing merely:

```text
broken package.json
deprecated APIs
old JavaScript
failing build
```

it sees:

```text
Project purpose:
  remote file movement without local download

Critical capabilities:
  streaming
  resumability
  remote storage abstraction

Invariants:
  bounded memory
  low-end hardware support
  no mandatory proprietary client

Current implementation:
  obsolete Node runtime
  abandoned streaming package

Replacement policy:
  both are replaceable

Compatibility contract:
  existing configuration format must remain readable
```

The agent can now construct a new implementation using technologies available in 2041 while preserving the identity of the project.

That is the central promise of Forever Works.

---

# 32. What Forever Works Is Not

Forever Works is not:

- a promise that software can literally run forever,
- a specific AI model,
- a package manager,
- a programming language,
- a framework,
- an automatic rewrite engine,
- a replacement for source control,
- a replacement for tests,
- a replacement for documentation.

It is infrastructure for preserving architectural meaning across technological change.

---

# 33. Long-Term Standardization Goal

The long-term aspiration is that software projects routinely ship with machine-readable architectural intent.

In the same way modern projects commonly include:

- dependency manifests,
- tests,
- API definitions,
- type information,
- CI configuration,

future projects could also include a durable preservation layer describing:

- intent,
- capabilities,
- invariants,
- dependency rationale,
- migration boundaries.

A future maintainer or agent should not need to reverse-engineer the soul of a project from obsolete implementation details.

The project should be able to explain itself.

---

# 34. Foundational Statements

The project can be summarized by several principles:

> **Preserve purpose, not obsolete machinery.**

> **Separate what must survive from what happens to implement it today.**

> **A dependency should explain why it exists before a future agent decides how to replace it.**

> **Modernization is successful only when it preserves the project's enduring intent.**

And the central statement:

> **Software intended to live for a long time should carry enough structured meaning that future systems can understand not only how it works, but why it works that way.**

---

# 35. Mission in One Sentence

> **Forever Works gives future agents the architectural memory required to keep software alive without losing what made it worth preserving.**
