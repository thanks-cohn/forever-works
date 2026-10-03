# Versioning

`foreverVersion` uses `MAJOR.MINOR`. Readers MUST reject an unsupported major version, MUST accept a newer minor version when all required semantics are understood, and MUST ignore unknown fields while preserving them when round-tripping. A major change may alter meaning or required fields; a minor change may only add optional fields or enum values whose unknown handling is defined. Canonical output retains the input version. Historical fixtures remain part of conformance.
