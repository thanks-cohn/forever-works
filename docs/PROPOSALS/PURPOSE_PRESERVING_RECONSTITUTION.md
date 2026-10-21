# Purpose-Preserving Reconstitution

**Status:** Foundational design doctrine and research proposal; non-normative for Standard 0.1 and Public API v0.1.  
**Scope:** Legacy understanding, simplification, replacement, cold-agent inheritance, architectural discontinuity, and evidence-backed reconstruction.

## Core principle

> The original implementation is evidence of an intended system, not the definitive expression of its purpose. Architecture, dependencies, interfaces, languages, and historical decisions may be discarded or replaced, provided the successor demonstrably preserves the accepted purposes, obligations, and relevant constraints of the original.

**Purpose should survive; mechanisms must remain negotiable.** No line of code, architectural layer, dependency, platform, or interface is authoritative merely because it existed before. Preserve *semantic continuity despite implementation discontinuity*.

This is stronger than code migration or faithful architectural translation. An agent inheriting tangled, badly designed, or obsolete software should recover *what it exists to accomplish*, *why it was built that way*, *which outcomes people actually depend on*, and *what may safely be discarded*. A smaller, wholly different implementation may be preferable to perpetuating historical complexity, **but only if independent evidence supports equivalence within the accepted scope**. Do not assume fewer lines imply better software.

## Why purpose extraction matters

A legacy system can contain hundreds of thousands of lines, circular dependencies, workarounds for disappeared platform limitations, accidental coupling, duplicated behavior, and expedient decisions mistaken for timeless requirements. Rather than canonizing these accidents, describe the system in a compact, linked, machine-queryable network of:

- **Purpose / intent:** human need, beneficiary, desired outcome, and why the system exists.
- **Capabilities:** what the system enables in externally meaningful terms.
- **Invariants, constraints, compatibility and authority:** what must remain true, for whom and under which conditions, including privacy, security, accessibility, data sovereignty, legal obligations, and interoperability.
- **Decisions and rationale:** what was chosen; why; alternatives rejected; assumptions at the time; what would invalidate those assumptions.
- **Mechanisms:** code, architecture, APIs, dependencies, database, framework, UI, deployment model—historical realizations that may be replaced.
- **Provenance and evidence:** how we know a claim, whose interpretation it is, and what remains uncertain.
- **Replacement and migration obligations:** externally observable criteria for a legitimate successor and the tests that must demonstrate satisfaction.

An agent should be able to answer, for each entangled component: "What purpose does it serve? Why did they do this? Because of X and Y? Are X and Y still true? If not, can I replace the whole mechanism?" A system's existing complexity is a subject of investigation, not a design specification to be copied.

## Reconstitution protocol for unfamiliar or convoluted software

1. **Establish the evidence boundary.** Inventory source, runtime observations, tests, documentation, issues, historical decisions, user workflows and data formats. Identify missing evidence and inaccessible services.
2. **Extract purpose and lived behavior separately.** Infer possible intents from code and documents, inspect actual behavior and usage when authorized, and distinguish what stakeholders *want* from what the system *happens to do*. Do not silently promote inference to requirement.
3. **Untangle the causal history.** For each decision record the original question, selected mechanism, historical limitations, tradeoffs, workarounds, consequences, alternatives and whether the original rationale still holds.
4. **Classify what survives.** Separate accepted purposes and externally necessary capabilities from invariants, compatibility promises, safety/privacy duties, transitional data-migration obligations, replaceable mechanisms, incidental quirks, defects and unresolved ambiguities.
5. **Reconcile contradictions explicitly.** Purposes can conflict: convenience versus privacy; speed versus correctness; simplicity versus accessibility; interface redesign versus learned user workflows. Record priority, scope, decision authority and unresolved conflict. **Never let a simplification silently weaken privacy or other critical constraints.**
6. **Model a successor without architectural allegiance.** Consider new languages, storage, deployment, interfaces, platforms or completely different interaction paradigms. Permit removal of accidental complexity and obsolete workarounds; retain essential observable outcomes and authorized user value.
7. **Prove rather than assert.** Define acceptance examples, migration checks, data round-trip tests, accessibility and security checks, performance envelopes when material, negative cases, and independently run verification. Unknown evidence remains UNKNOWN, not PASS.
8. **Record what changed and why.** Explain eliminated mechanisms, altered user-visible behavior, new tradeoffs, outstanding uncertainties and new evidence. Leave better provenance for the next inheritor.

### The undocumented-behavior trap

The original implementation may embody valuable behavior that **nobody formally specified**: recovery semantics, obscure edge cases, interaction timing, data compatibility, user expectations, security defenses or accessibility affordances. Investigate source and observed behavior before removing anything; compare it with documented intent and real user needs. Classify it as essential, historical/obsolete, accidental, harmful, or uncertain—with evidence. When unclear, flag the uncertainty and seek authorized human judgment rather than blindly simplifying.

Not every old behavior must survive: bugs, obsolete interfaces and incidental constraints can be intentionally retired. But their removal is an explicit scoped decision, never a silent artifact of rewriting.

### The limits of 'preserve purpose'

Purpose is not necessarily singular, self-evident, or objectively recoverable from code. Different stakeholders may value different outcomes. Prioritize accepted, sourced intent over an agent's attractive reinterpretation; record provenance, confidence and conflicts. The agent must not unilaterally redefine the project's goals. New purpose is a separately authorized product decision. Preservation does not promise identical execution traces, perfect recovery of lost history, or universal compatibility.

## Relation to neighboring approaches

The following are **differences in primary emphasis**, not claims that the others cannot represent purpose or migration:

| Approach | Strong existing contribution | Distinction pursued by Forever Works |
| --- | --- | --- |
| **arc42** | Architecture views, constraints, rationale and decisions | Make mechanism-independent purpose, replacement obligations and evidence the inheritance interface; original architecture is optional historical evidence, not the target design. |
| **StrictDoc** | Structured requirements, traceability, and implementation/test links | Broaden the target from tracking requirements to reconstructing essential system value across total mechanism replacement; borrow its traceability discipline rather than reinventing it. Significant overlap warrants direct comparison. |
| **OpenSpec** | Spec-driven development and AI-assisted changes | Carry intent across abandoned implementations, agent generations, new modalities and independent cold reconstruction; not only manage a change in a current codebase. |
| **Software Heritage** | Long-lived source/history preservation | Capture the meaning and acceptance obligations needed to *reinterpret* archived source and recreate capabilities after original technologies disappear. Source archives and Forever Works are complementary. |

These approaches are open or openly licensed, not proprietary barriers. Interoperability should be preferred where it reduces redundant work: architecture-decision imports, requirement/test links, spec integration, and persistent source/archive identifiers. Avoid claiming novelty for requirements traceability, documenting why, or preserving history in isolation. The proposed distinction is the **combination and priority** of purpose extraction, dispensable implementation, explicit replacement obligations, provenance, and closed-world verification.

## Example: an overengineered image manager

A legacy application might use 80,000 lines, PHP services, a bespoke thumbnail database, layered caches and browser-specific shims. Its user-centered purpose may instead be: **let people collect, organize, annotate, retrieve, enjoy, and export their images without losing ownership, relationships or privacy**.

The relevant successor might be a compact native desktop tool, an offline mobile app, or a future interaction medium with no PHP, original DB, or browser shims. Preserve verified import/export formats where migration requires them; preserve annotations, relationships, privacy and recoverability as accepted obligations; document which original quirks are deliberately discontinued. The successor must pass independent migration and acceptance checks before it can claim continuity.

For Atlas-like software, a browser right-click shelf may be a historical means of immediate contextual access—not necessarily the enduring requirement to preserve that particular gesture. But discoverability, minimal effort and usability must still be tested; never replace an interface merely by asserting that a new one is prettier.

## Agent-oriented compression without semantic loss

A concise purpose model is useful only if it retains traceable links back to decisions, observed behavior, tests, unresolved questions, and sources. Compress *navigation and rediscovery effort*, not responsibility. A short summary that discards edge cases, contradictory requirements, or evidence is not an adequate inheritance package. Provide progressive disclosure: a small agent entrypoint, stable IDs, queryable records, and deeper evidence on demand. The goal is to avoid repeatedly reverse-engineering the same reasons while remaining auditable by humans.

## Test this claim instead of assuming superiority

Run a **Cold Reconstruction Challenge** with independent agents and comparable documentation/evidence-preparation budgets. Compare source + README, source + arc42, source + StrictDoc, source + OpenSpec, and source + Forever Works on unfamiliar legacy applications, including an obsolete dependency and at least one undocumented but consequential behavior. Keep original behavior probes and evaluator independent from the rebuilding agent.

Measure capability and invariant retention, fidelity of recovered purpose, data migration correctness, regression/security/accessibility results, unresolved uncertainty, human interventions, agent tokens/time, maintenance complexity, and documented rationale for removed mechanisms. A smaller successor is a benefit only when acceptance obligations pass. Publish failure modes, negative results, and limitations; strong ambitions are not demonstrated performance.

## Relationship to the existing standard

Standard 0.1 already distinguishes intent/capability/invariant/constraint from implementation/dependency, retains provenance, and uses conservative PASS/FAIL/UNKNOWN replacement evaluation. This doctrine **interprets and extends their intended use**, but is not an additional normative schema requirement or a claim that fully automated purpose extraction/reconstitution is already implemented. Future evolution should be proposed with versioned schemas, conformance fixtures, interoperable tooling and independent benchmarks rather than silently altering Standard 0.1.

**Design maxim:** Preserve what the software was *for*. Understand why it became what it *is*. Prove that the successor still delivers what matters.

## Adopted maintenance premise

[Simple Design and Traceable Removal](SIMPLE_DESIGN_AND_TRACEABLE_REMOVAL.md) applies this doctrine to ongoing engineering: remove obsolete implementations and unnecessary compensation, preserve a linked account of former locations and effects, and verify the resulting production artifact. It explicitly records suspected residual influence and uncertainty to support later debugging. It is a repository maintenance policy, without changing Standard 0.1 or Public API v0.1.
