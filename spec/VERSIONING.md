# Versioning

`foreverVersion` uses `MAJOR.MINOR`. Readers MUST reject an unsupported major version, MUST accept a newer minor version when all required semantics are understood, and MUST ignore unknown fields while preserving them when round-tripping. A major change may alter meaning or required fields; a minor change may only add optional fields or enum values whose unknown handling is defined. Canonical output retains the input version. Historical fixtures remain part of conformance.

Clarifications repair contradictory descriptions against the existing standard and
retained examples; they must include regression evidence. Tightening a previously
valid semantic domain, changing canonical bytes incompatibly, removing fields or
operations, or changing authority requires a versioned contract and migration note.
Do not silently rewrite historical fixtures to bless an implementation change.

Optional profiles remain opt-in and cannot add mandatory core ontology or dependencies.
Deprecation must name the replacement, retained compatibility fixtures and supported
transition period before removal in an incompatible edition. Stronger conformance
claims require operation-level fixtures and independent semantic implementation
results; wrappers, shared algorithms and structural schema oracles must be labeled.
Any new governance/acceptance body is a proposal until explicitly adopted. The numeric
domain question recorded in docs/API/CORE_INPUT_AND_NORMALIZATION.md remains unresolved.
