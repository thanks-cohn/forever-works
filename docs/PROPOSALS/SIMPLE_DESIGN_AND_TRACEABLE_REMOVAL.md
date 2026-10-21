# Simple Design and Traceable Removal

**Status:** Owner-adopted engineering premise and repository maintenance policy. This supplements Purpose-Preserving Reconstitution; it does not change Standard 0.1 schemas, Public API v0.1, or their conformance contract. It does not claim full XP adoption or ISO certification.

## Premise

Forever Works adopts the Simple Design principles associated with Extreme Programming (XP): preserve correct behavior, express intent clearly, avoid unnecessary duplication, and retain only elements needed to fulfill current requirements and obligations. Clarity, accessibility, compatibility, recovery, and performance can justify structure; minimum line count is not the objective.

Forever Works goes further by requiring traceable removal: investigate obsolete artifacts and decisions, remove their unnecessary implementation and residual effects, and preserve an evidence-backed account of where they were, what they did, and how their absence was verified. Historical understanding must survive without keeping obsolete machinery active.

This is an adopted premise, not a claim that every existing repository or release has already been audited or found free of remnants.

## Layers of necessity

For each affected area, trace purpose and accepted obligations through observable behavior, implementation, supporting machinery, and historical decisions. Ask what each layer provides, what depends on it, whether its rationale still holds, and what simplification preserves its obligations. Inspect code that still executes as well as unreachable or unused code.

Investigate superseded implementations, duplicate handlers, conflicting CSS overrides, abandoned flags, unused assets and dependencies, obsolete configuration, compatibility paths, generated outputs, and workarounds whose triggering conditions have disappeared. Resolve the underlying conflict rather than continually adding compensating patches.

Do not mistake unfamiliar behavior for obsolete behavior. Extract undocumented but valuable obligations before removal. Preserve required behavior or transfer it to a verified successor. Necessary migration or compatibility code remains current machinery with a stated purpose and retirement condition.

## Removal and historical artifact records

For each meaningful retired mechanism or group of related remnants, maintain a concise, linked record alongside project documentation. Documentation artifacts include this record and its verification evidence; they are separate from shipped application artifacts.

Record:

- Stable record identifier, date, author or agent, affected capability, and related decisions or migrations.
- Historical locations: paths, symbols, selectors, settings, dependencies, and immutable source revision references where available.
- Original role and rationale, with provenance; distinguish documented facts, observed behavior, and hypotheses.
- Why the mechanism became obsolete and the accepted scope of retirement.
- Known effects and suspected influence: coupling, execution order, layout, persistence, performance, or workarounds introduced elsewhere. A suspected influence is not an established cause.
- Removal or replacement revision and current locations of any preserved obligations.
- Residual investigation: imports, handlers, styles, settings, dependencies, assets, generated bundles, deployment outputs, caches, service workers, stored data, and external state as applicable.
- Verification methods, environments, artifact identity or digest where available, results, evidence links, and limits.
- Unresolved questions, follow-up ownership, and the conditions that would reopen the investigation.

Preserve historical code through source history or a durable archive reference. Do not leave disabled copies, commented-out implementations, or unused backup files in the active application merely to explain the past. Keep records searchable and proportionate; group related removals rather than documenting every deleted line.

## Completion and production verification

1. Identify the remnant and trace both direct dependencies and compensating mechanisms.
2. Record the prior locations, effects, rationale, and uncertainty before evidence is lost.
3. Remove the obsolete mechanism and unnecessary compensation; preserve accepted obligations.
4. Inspect source, build inputs, dependencies, and generated artifacts for remaining references or effects.
5. Build the resulting production artifact when applicable and verify required behavior against that artifact, including affected states, viewport sizes, persistence, and upgrade paths.
6. Record the exact checked revision/artifact, evidence, and outstanding uncertainty. A source-only search cannot establish absence from a deployed release.
7. Update the record when later debugging discovers another residual effect or overturns a prior causal explanation.

Documentation is not a substitute for removal. A known obsolete remnant in the affected scope prevents a completion claim. An unresolved possible remnant remains UNKNOWN and prevents an unqualified claim that the scope is free of remnants; continue investigation or explicitly report the incomplete work.

A checked release may be described as free of the identified remnants **within the recorded scope and evidence boundary**. Never turn a bounded search or passing test suite into proof that no unknown historical influence exists anywhere. Existing released versions are not retroactively verified by checking a new build.

## Reusable record outline

- ID / status / owner:
- Capability and related decisions:
- Before revision and historical locations:
- Original role and rationale / provenance:
- Reason and authority for retirement:
- Observed effects:
- Suspected influences and evidence:
- Preserved obligations and successor:
- Removal revision:
- Residual checks, including state and generated outputs:
- Checked production revision/artifact and environment:
- Verification evidence and result:
- Unknowns, follow-up, and reopening conditions:

This is a human-readable documentation convention. It introduces no new canonical record kind, automatic remnant detector, or machine-validated conformance profile. Link existing decision, migration, implementation, and evidence records where available without inventing unsupported API behavior.

## Debugging value

When a later bug appears, a future agent can locate former mechanisms, inspect their historical interactions, identify compensation that may have survived, and rerun relevant checks. The record is a causal investigation aid, not proof that the removed mechanism caused the new bug. Record corrections without erasing the earlier evidence trail.

## Foundations

- [Kent Beck's Simple Design rules, described by Martin Fowler](https://martinfowler.com/bliki/BeckDesignRules.html).
- [Remove Dead Code](https://refactoring.com/catalog/removeDeadCode.html).
- [Purpose-Preserving Reconstitution](PURPOSE_PRESERVING_RECONSTITUTION.md).

**Maxim:** Remove obsolete machinery. Preserve its explanatory history. Verify the current artifact.
