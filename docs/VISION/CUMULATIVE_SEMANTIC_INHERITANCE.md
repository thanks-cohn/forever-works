# Cumulative Semantic Inheritance

Status: non-normative proposal, 2026-10-15. This proposal complements Forever Works Standard 0.1 without changing the normative core or claiming implemented features.

## Principle

Preserve the program, preserve its meaning, and preserve what was learned while changing it.

Forever Works should capture transferable engineering experience during migrations, ports, modernizations, reconstructions, and companion-app construction. Future developers and agents should be able to reuse prior reasoning, tested adaptations, failures, human corrections, and remaining limitations rather than rediscovering them.

**Cumulative Semantic Inheritance (CSI)** means every transformation may add reusable, provenance-rich, versioned knowledge to a growing engineering memory. Human edits and their rationale matter just as much as automated changes. Claims and summaries are not independently verified results.

## Proposed terminology

- **Software Translation Atlas:** optional shared or private corpus of directional migration and companion examples, not the separate Atlas product.
- **Semantic Bridge:** explicit mapping of a source capability or contract to a target implementation and its meaningful differences.
- **Transformation Record:** contextual history of a particular port, migration, reconstruction, or extension.
- **Inheritance Package:** frozen, portable, independently readable set of architectural contracts, examples, and evidence, with checksums and declared gaps.
- **Translation Recipe:** reusable procedure drawn from previous transformation attempts, conditional on its original assumptions.
- **Applicability Envelope:** platform, version, API, permissions, hardware, constraints, and data conditions under which a recipe is supported.
- **Semantic Delta:** behavior or meaning intentionally altered, missing, or impossible to preserve on a target.
- **Human Intervention Record:** human edits, rejections, decisions, corrections, reasoning, and approval boundaries with provenance.
- **Failure Memory:** reproducible bug, unsuccessful approach, error, root-cause hypothesis, remedy, and outstanding risk.
- **Verification Evidence:** executed tests and observations with environment, method, results and artifacts; separate from supplied claims.
- **Knowledge Lineage:** traceable links across source requirements, transformed implementations, human input and later reuse.
- **Cumulative Engineering Memory:** selectively retrievable body of knowledge gained from prior work.
- **Directed Translation Case:** a source-to-target example; reverse translation counts separately.
- **Companion Construction:** making an interoperable sibling application rather than a replacement.
- **Source-Independent Inheritance:** an isolated agent works from a frozen documentation package and allowed public references, without secretly receiving implementation source.
- **Knowledge-Conditioned Development:** relevant past bridges, decisions, tests and pitfalls inform a new implementation before rediscovery.

All terms above are proposed conceptual terminology, not current normative record kinds.

## Two forms of transformation

1. **Replacement/port:** reconstruct required capabilities in another framework, language, runtime or platform, verifying invariants and documenting differences.
2. **Companion construction:** create an interoperating application with different platform affordances, stating common data, state ownership, synchronization, security and conflict behavior. It need not offer identical features.

An Android companion for a Chrome extension cannot assume that Android offers an equivalent of the extension's chrome.bookmarks API. A tested bridge might instead use explicit export/import or authorized sync, preserving portable bookmark metadata and annotations while recording the lost native integration.

## Reference examples: one origin of each type

Develop at least one modest real source application in each of four environments: Chrome extension, React web, React Native Android, and desktop (specify actual implementation, e.g. Electron or Tauri). From each origin, demonstrate the other three targets: twelve directed cases. Include both ports and companion designs, and record infeasible mappings honestly. Cover persistence, data round trips, notes/tags, search, lifecycle, UI adaptation, errors, accessibility, permissions and platform-specific constraints.

| Original | Target environments |
| --- | --- |
| Chrome extension | React web; React Native Android; desktop |
| React web | Chrome extension; React Native Android; desktop |
| React Native Android | Chrome extension; React web; desktop |
| Desktop | Chrome extension; React web; React Native Android |

Use shared behavioral specifications rather than sharing hidden implementation source in source-independent tests. Reverse direction is a different case.

## Large-system example: Alpine and an experimental derivative

An agent building an experimental Zig-based Alpine derivative (illustratively, ALPZ) could inherit explicit architectural intent, data contracts, ABI and syscall requirements, tested replacements, failures, manual fixes, and documented limitations. Another agent approaching a Rust-based derivative could reuse suitable knowledge, but must revalidate target-specific assumptions. Alpine Linux is a distribution, not the kernel: userland/package changes, replacing kernel components, and building a new kernel must be distinguished. A large project should expose short agent-oriented indexes linked to precise subsystem-level authoritative contracts, not demand that every record fit in one context window.

## Proposed optional Translation and Inheritance Profile

Keep Forever Works' canonical model small and language-neutral. Put specialized bridge, translation, intervention, failure, and evidence shapes into a versioned optional profile grounded in existing stable IDs and safe extensions. Never introduce a mandatory ontology or silently modify Standard 0.1.

Capture for each example: precise source/target versions and boundaries; source intent, capabilities and invariants; semantic mapping and deltas; applicability envelope; attempted and rejected solutions; recorded human edits and rationale; reproduced bugs and fixes; preservation tests and independent evidence; untested claims and unknowns; data formats and migration compatibility; privacy and permissions; pointers to reproducible artifacts.

## Succinct agent-oriented layered documentation

Produce multiple navigational views derived from one authoritative graph:

1. **Orientation capsule:** objective, platform boundaries, contract version, status, critical risks.
2. **Bridge index:** capability IDs, candidate translations, semantic deltas, applicability and provenance.
3. **Task work packet:** only relevant decisions, human corrections, bugs, tradeoffs, fixtures and evidence.
4. **Deep authoritative records:** exact behavior, schemas, interfaces, errors, state ownership, verification.

A summary must link to stable IDs, version/checksum, evidence, uncertainties and original records; it cannot silently replace or contradict their authority. Invalidate stale summaries. Human changes are valuable contextual evidence, not automatically universal instructions.

Retrieval sequence: understand target task and constraints; discover matching bridges; check applicability; inspect contrary evidence and known failures; obtain a scoped work packet; implement and independently test; append the new lessons with their provenance. Never promote an earlier claimed PASS to a verified result in a new environment.

## Research program and limits

Hypothesis: accumulated verified migration knowledge significantly reduces repeated discovery, time, tokens, human interventions and regressions for subsequent related transformations. Exponential improvement is an aspiration, **not** an established outcome.

Evaluate independent agents under comparable tooling and compute budgets using: conventional docs only; Forever Works contracts; contracts plus prior translation knowledge. Freeze inputs/checksums, prohibit hidden source access or coaching, use held-out projects and version changes, retain failed attempts. Measure functionality, preserved invariants, data loss, regressions, security, human edits, time, compute, and incorrect reuse. Compare across increasingly varied sets, potentially 5, 20 and 100 cases, before claiming compounding advantages.

Imported knowledge is untrusted data, never a grant of execution or privileges. Preserve licensing, privacy, consent, secret redaction, authorship and authority. Independent consumer success and outside adoption need separate proof.

## Order of implementation

First finish the existing foundation-hardening run. Next complete the planned independent two-product-to-third-product reconstruction proof. Then define and validate the optional profile, build a small verified translation example with failure memories and human edits, expand the directional case matrix, add contextual retrieval, and independently measure its benefits. Do not conflate an ambitious proposal with an implemented or certified standard.

> Preserve purpose, required behavior, and the knowledge learned through change. Make the next transformation easier without making it less trustworthy.
