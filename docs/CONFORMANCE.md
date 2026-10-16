# Conformance

A conforming binding loads the shared fixtures, rejects structural and reference errors, tolerates unknown fields, rejects unsupported major versions, produces canonical normalization, implements lookup/list/trace, and implements conservative replacement and migration checks. `conformance/fixtures/cases.json` is the machine-readable case catalog and `conformance/expected` contains golden results. Bindings may expose different APIs but MUST produce semantically identical JSON results. Cycles terminate through a visited set.

JavaScript, TypeScript, C, Python, and C++ are distinct proof targets. JavaScript runs its shared-fixture and golden comparisons directly from `.js` source without `tsc`; TypeScript compilation or conformance is not JavaScript evidence. C and C++ intentionally expose a smaller parsing/query surface, while JavaScript and Python cover replacement and migration; TypeScript covers replacement but not migration. See the [operation map](API/OPERATION_COVERAGE.md).

The experimental optional ecosystem profile has a separate versioned catalog at
`conformance/ecosystem-composition/v0.1/cases.json`. Its JavaScript semantic tests
run within `make test-javascript`; independent Draft 2020-12 structural validation
runs with `python3 scripts/check_ecosystem_schema.py` after installing
`scripts/requirements-schema.txt`. `schemaValid` describes structure only; `valid`
also includes profile reference checks. These results do not claim a second
semantic binding or runtime interoperability. See the
[profile contract](../spec/profiles/ecosystem-composition/v0.1/README.md).

`make hardening` runs `conformance/hardening/cases.json`, original cases, self-model,
all shipped example manifests, strict loader boundaries and independently reviewed
normalization bytes through JS, TS, Python, C and the C++ wrapper. Install the pinned
`scripts/requirements-schema.txt` first. The `jsonschema` Draft 2020-12 oracle checks
structure separately from graph semantics. `make sanitizer` runs deterministic native
malformed inputs under ASan/UBSan on supported Linux toolchains. CI adds Linux/Windows
hardening and a Linux sanitizer job; a workflow definition is not an executed result.

Canonical byte agreement has the numeric-domain limitation documented in
[the core contract](API/CORE_INPUT_AND_NORMALIZATION.md). No complete conformance badge,
source-independent construction success or runtime evidence acceptance is claimed.
