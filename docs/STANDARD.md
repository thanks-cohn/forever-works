# Forever Works Standard 0.1

This document is normative. The keywords MUST, MUST NOT, SHOULD, and MAY express requirements.

## Authority and scope

Forever Works preserves architectural meaning independently of implementations. Authority descends from this standard to schemas and conformance fixtures, then bindings and convenience tools. UTF-8 JSON is the canonical interchange. No language, runtime, framework, transport, vendor, or agent is required.

## Model

A model is a manifest plus records. Every record has `foreverVersion`, globally unique stable `id`, `kind`, and optional provenance/extensions. Kinds are `intent`, `capability`, `invariant`, `constraint`, `dependency`, `decision`, `compatibility`, `migration`, `implementation`, and `evidence`. References are exact IDs and form a directed graph; cycles are valid. Missing targets are errors. Unknown fields are accepted and preserved. IDs match `^[a-z][a-z0-9]*(?:[._-][a-z0-9]+)*$`.

Requirements (intent, capabilities, invariants, constraints, compatibility) are distinct from replaceable mechanisms (implementations and dependencies). Dependency classifications are exactly LOCKED, SEMANTIC, CAPABILITY, TRANSITIONAL, LEGACY, and OPTIONAL.

## Provenance

Sources are `explicit`, `inferred`, `imported`, `historical`, or `agent-proposed`. Inferred and agent-proposed statements never become authoritative merely through serialization or tool processing. Confidence is 0 through 1.

## Validation and normalization

Validation checks manifest structure, supported major version, required kind fields, unique IDs, listed paths, and all ID references. Safe extensions live below `extensions` using owner-qualified keys. Normalized JSON recursively sorts object keys, orders records by ID, uses UTF-8, two-space indentation, and one trailing newline. Array order is significant except the manifest's record path lists and normalized model record list, which sort lexically.

## Query contract

Lookup returns one record or not-found. Lists sort by ID. Trace returns the starting entity and every entity reachable in either direction, once, sorted by ID. Explanation returns the dependency purpose, selection rationale, classification, capabilities, invariants, compatibility obligations, and provenance. Audit emits stable issue codes and never infers a pass.

## Evaluation and migration

Candidate implementations declare `claims`, each containing a requirement ID, status (`pass`, `fail`, or `unknown`), optional evidence IDs, and reason. Evaluation enumerates every capability, invariant, constraint, replacement requirement, and compatibility obligation required by the dependency. A supplied claim controls its check; an absent claim is `unknown`. Overall result is `fail` if any check fails, `pass` only if every check passes, otherwise `partial`.

Migration verification applies the same closed-world rule to every declared preserved capability/invariant and compatibility impact. It additionally requires referenced verification evidence. Its result uses the same aggregation. This conservative three-valued behavior is normative.
