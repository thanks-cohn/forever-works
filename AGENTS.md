# Agent guidance

Read `docs/FOUNDATIONAL_PROPOSAL.md` and `docs/STANDARD.md` before changing semantics.

* Preserve language, runtime, framework, transport, agent, and vendor neutrality.
* The authority order is specification, schemas and conformance fixtures, reference bindings, then tooling.
* Update schemas, conformance fixtures, implementations, and documentation together when semantics change.
* Never promote inferred or agent-proposed intent to authoritative intent without explicit acceptance.
* Prefer backward-compatible schema evolution and retain old-version fixtures.
* Keep requirements distinct from implementations and record rationale for foundational dependencies.
* Keep the core model usable through plain UTF-8 JSON and understandable without proprietary tools.

