# Optional ecosystem composition proof

**Date:** 2026-10-15. **Status:** implementation decision, agent-proposed and
unreviewed; not a new normative Standard 0.1 decision or approved adopter intent.

The original single-project record graph remains valid. The earlier
[ecosystem proposal](../PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md)
identified requirements that exist between components and within deployment
arrangements, including many-party coordination, state ownership and collective
acceptance. A separate optional profile now provides a first executable schema,
JavaScript reference validator, scoped evidence claims and shared fixtures.

We keep canonical intent/capability/invariant/compatibility references rather than
inventing competing authoritative requirements. Stable participant identity and
interaction meaning are distinct from replaceable deployment bindings. Ports are
qualified by participant; interactions form directed hyperedges and multigraphs;
containment is acyclic even though communication may cycle. One declared state
owner and explicit writers make a bounded set of authority contradictions
machine-checkable without pretending to implement authentication or consent.

A schema-valid composition is not verified interoperability. The static adapter
always returns UNKNOWN for runtime obligations, including evidence that claims
PASS. Digests and verifier names are claims awaiting independent authentication.
Component builds and existing component evidence do not establish suite proof.
Opaque policy parameters and unknown semantics remain visible warnings.

The [versioned profile](../../spec/profiles/ecosystem-composition/v0.1/README.md)
is experimental. No canonical record kind, schema, Standard 0.1 semantics or
Public API v0.1 operation changes. No external adopter or agent toolkit is a
runtime dependency. Python jsonschema is only an independent development oracle;
its rationale is recorded as an unreviewed dependency-intent record. Other
bindings are not claimed to implement the profile.

Next evidence should include a second independent semantic validator and two real
interacting outputs with held-out authority/state/recovery checks. A synthetic
adopter mapping can then test preservation of relationships and provenance;
it must not equate a user generation request with accepted enduring intent.
Only observed, general semantic gaps should justify further profile evolution.
