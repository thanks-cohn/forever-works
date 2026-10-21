# Agent guidance

Read `docs/FOUNDATIONAL_PROPOSAL.md` and `docs/STANDARD.md` before changing semantics.

* Preserve language, runtime, framework, transport, agent, and vendor neutrality.
* The authority order is specification, schemas and conformance fixtures, reference bindings, then tooling.
* Update schemas, conformance fixtures, implementations, and documentation together when semantics change.
* Never promote inferred or agent-proposed intent to authoritative intent without explicit acceptance.
* Prefer backward-compatible schema evolution and retain old-version fixtures.
* Keep requirements distinct from implementations and record rationale for foundational dependencies.
* Keep the core model usable through plain UTF-8 JSON and understandable without proprietary tools.
* **JavaScript is a first-class proof target, separate from TypeScript.** A successful TypeScript build or TypeScript conformance run does not establish JavaScript conformance.
* Plain JavaScript consumption must not require a TypeScript compiler. Maintain dedicated JavaScript tests, examples, packaging/consumer proof, and conformance evidence as the JavaScript target is implemented and evolved.

* When public API semantics, operations, errors, versioning, CLI mappings, or adapter obligations change, update the official documentation under `docs/API/` in the same coherent change. Planning and handoff documents do not replace the official API reference.

* Follow the owner-adopted [Simple Design and Traceable Removal premise](docs/PROPOSALS/SIMPLE_DESIGN_AND_TRACEABLE_REMOVAL.md). Investigate and remove obsolete machinery and unnecessary compensation in the affected scope; document former locations, roles, known effects, suspected influences, and removal evidence. Verify the resulting production artifact where applicable, including residual state and generated outputs. Unknowns remain explicit; do not claim an unaudited release is free of remnants. This maintenance policy adds no Standard 0.1 schema or API requirements.
