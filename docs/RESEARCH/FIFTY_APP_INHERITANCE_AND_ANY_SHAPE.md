# Research Program — Fifty-App Inheritance, SUBSTRATE Mini, and Any-Shape

**Status:** Proposed flagship demonstrations, not completed implementations or normative requirements.  
**Date:** 2026-10-14  
**Parent:** [Forever Works Long-Horizon Vision](../VISION/INHERITABLE_SOFTWARE_ECOSYSTEM.md)  
**Methods:** [Selective Reconstitution Proposal](../PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md)

## One standard, three experiments

Forever Works must be demonstrably more than dense documentation. Three complementary experiments should test its breadth:

| Demonstration | Research question | Deliverable |
| --- | --- | --- |
| **SUBSTRATE Mini** | Can we rescue essential functionality from a genuinely entangled legacy product without inheriting unnecessary coupling or unexplained failure? | Lean, fully mapped canvas/document application; comparative behavioral fixtures; extraction and dependency evidence |
| **Any-Shape** | Can a cold agent receive an inherited semantic contract and reconstruct a working application in a different medium, language or framework while preserving state, interactions and real effects? | Repeatable, source-neutral browser-to-desktop/mobile experiments, verified independently |
| **50-application browser ecosystem** | Does the same standard support dozens of truly different applications and future migrations rather than a carefully hardcoded demonstration? | Cross-app corpus, consistent inheritance packages, repeated cold-agent renewal/reconstruction trials |

Their source applications should remain useful products in their own right. Research frameworks must be optional tools; they cannot become hidden mandatory dependencies of the standard.

## SUBSTRATE: understand what the product truly is

The original SUBSTRATE is understood by its owner as an accumulation of **at least twenty functional areas**, developed at different times and sometimes haphazardly. Although useful functionality works, glitches, crashes, unexpected interactions and undocumented cascading failures can arise from cross-feature coupling. The exact inventory and causes **have not yet been established**; they must be discovered empirically from the live repository and running application.

**Preserve the current product** as the reference and do not recklessly remove code. First build a **Capability Ledger and Dependency Atlas** that answers for each selected capability:

- Intended user outcome and entry point; observable successful workflows and representative failures.
- Source locations, runtime control/data paths, state ownership, event lifecycles and resource cleanup.
- Direct, transitive, intermeshed, hidden and apparently extraneous dependencies, with evidence and uncertainty.
- Relations to other functional areas and sources of interference/cascading failure.
- Security and authorized effects, error handling, performance and acceptance criteria.
- What to **PRESERVE**, **CORRECT** with owner approval or **EXCLUDE** intentionally.
- Isolation strategy, regression tests, provenance and current confidence status.

An **unexplained dependency is an unfinished extraction**. A suspected incidental dependency is not automatically safe to delete. Keep failures diagnosable and reproducible; eliminate accepted cascading failures through sound isolation and explicit contracts, not promises of impossible zero-defect software.

### SUBSTRATE Mini — proposed first bounded slice

Initial *target* scope: a reliable visual **canvas** for **images and videos**, plus **Word/document opening** and **PDF opening/viewing**. Exact supported formats, editing/export behaviors, canvas transforms, persistence and performance targets will be frozen **only after observing** actual SUBSTRATE behavior and obtaining owner acceptance.

Expected modular design (subject to proof, not dogma):

- A minimal **canvas core** owning selection, positioning, transforms, focus, lifecycle and common state.
- Independently bounded **image**, **video**, **document/Word**, and **PDF** adapters with explicit interfaces and cleanup semantics.
- Portable state serialization and diagnostics; deterministic fixtures for open, close, switch, render and reopen.
- No direct hidden mutation of sibling adapter internals, no unrelated Legacy subsystem imported just for incidental initializers, and no undocumented side effects.

A PDF failure should not silently destabilize video playback, canvas state or images. Tests must intentionally exercise switching, repeated open/close, malformed files, concurrent operations, resource exhaustion, and rollback/recovery. Baseline memory, responsiveness, rendering and crash incidence before claiming improvement.

### Progressive capability recovery ladder

1. **Observed:** a baseline, fixtures and a recorded behavior/defect disposition exist.
2. **Mapped:** known code and effect paths/dependencies are documented; unknowns explicitly remain.
3. **Isolated:** the selected capability works behind an explicit boundary, without unverified reliance on unrelated systems.
4. **Verified:** independent functional, regression, failure, performance and cross-feature interference checks pass.
5. **Reconstituted:** capability is maintainable outside Legacy, optionally in another language/platform, with migration/handoff evidence.

Stop at **Verified** when the aim is stabilizing the original. Reconstitute into Mini when independent recovery is justified. Keep Legacy functioning and compare it against extracted slices. Newly discovered defects in the original do not become invariants automatically.

### Beyond Mini: the integrated product and product family

Successful isolation may reveal independent reusable libraries, several separately distributable applications, a lightweight Mini, and eventually a full **SUBSTRATE Complete** assembled from verified capabilities. The count and commercial demand of possible apps are hypotheses, not predetermined outcomes. Shared engines should be reused rather than duplicated. Integrated suites require additional cross-capability tests; standalone tests cannot prove interactions safe. Review licensing and third-party dependencies before commercial redistribution.

Most importantly, **the capability graph may reveal the actual conceptual architecture and aims of SUBSTRATE**, apart from the order in which it was developed. Product discovery is a benefit of the research, but preservation of meaning and reliability are the first obligations.

## Any-Shape: the first cross-medium showcase

Any-Shape is proposed as the **first deliberate showcase of the power of Forever Works** to support reconstructing an application's semantic identity in a different shape or medium. A browser app may become a conventional mobile or native desktop program; appearance may adapt while **a press here must produce the same intended and authorized effect there**.

The pipeline should:

1. Inherit a source app **cold** and discover its capabilities through the portable Forever Works package, runtime evidence and fixtures.
2. Build a target-specific application through explicit platform adapters, using conventional tools and project structure.
3. Preserve authorized HTTP/filesystem effects, data formats, persistence, control semantics, error cases, accessibility and quality of interaction.
4. Verify using independent matched scenarios and real effect receivers—not merely screenshots, code compilation or subjective visual resemblance.
5. Record the migration, discovered gaps, regressions, modifications, limitations and useful lessons in a new inheritance package.

Avoid hand-coded recipes for the flagship source application. Source-neutral standards and reusable capabilities must generalize to unfamiliar apps. Future targets might include modern browsers, Windows/Linux desktop implementations, Android/iOS and technologies not yet invented. No universal target support is claimed at this stage.

## The fifty-app research corpus

Grow from a few deeply verified reference applications to a broad ecosystem of ~50, each with a conforming model, accepted capability descriptions, fixtures, observable effects, expected UX and performance, real source evidence and versioned continuity history.

Use diverse domains: forms, files, media, documents, graphics, interactive canvases, cloud-connected tasks, offline workflows, stateful tools and others. A corpus of fifty nearly identical forms would not prove generality. Record not only success rates but failures, ambiguities, maintenance costs, intervention count and parity gaps. Re-run inheritance tests after runtime/framework upgrades.

**Cold-agent experiment:** A reconstruction agent must not receive undocumented coaching or prewritten target implementation from the same extraction agent. Assess the resulting system independently. Record unknowns and needsHumanVerification explicitly. Compare to ordinary modernization/refactoring approaches, not just internal benchmarks.

## The research-to-standard feedback loop

Every unexpected legacy dependency, broken transfer, hidden effect or interface mismatch is potentially a **gap in the inheritance standard**, not only a bug in a demonstration. File an evidence-grounded proposal; review against multiple adopter cases; update schemas, conformance fixtures, APIs and documentation together *if* approved; preserve backward compatibility where possible.

Do not bloat the standard with every application-specific feature. Its core must remain lean, readable, language-neutral and comprehensible to developers independent of its founders. SDKs and adapter packages can be rich without making the normative data model needlessly enormous.

## Near-term milestones (proposed)

1. Inventory current SUBSTRATE capabilities and freeze one narrow, actually functioning extraction scope.
2. Capture reproducible selected behavior, crash cases, dependency and effect paths; publish a first Capability Extraction Package.
3. Extract the canvas/media/doc/PDF Mini incrementally after narrower pilot verification, recording missing capabilities honestly.
4. Run independent cold-agent reconstruction through Any-Shape on genuinely unfamiliar applications and at least one dissimilar target environment.
5. Expand the app corpus as evidence quality allows; audit which knowledge future agents actually needed and what was missing.
6. Feed validated lessons into reviewed Forever Works standard evolution, without binding the core to SUBSTRATE or Any-Shape.

## Ultimate acceptance question

**When our authors are gone and our frameworks obsolete, can an agent unfamiliar with any of our fifty applications inherit one of them, understand what it exists to do, repair or remake it in a current language and platform, and independently demonstrate that its meaning, state and real effects survived?**

That—not module count, export count, raw code generation speed or polished demos—is the long-term research measure.
