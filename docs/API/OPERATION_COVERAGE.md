# Operation and proof coverage

Authority: Standard 0.1 query/evaluation sections and Public API v0.1. Input details:
[core validation and normalization](CORE_INPUT_AND_NORMALIZATION.md).
`make test` retains original fixture, golden, migration and JS packaging coverage;
`make hardening` adds the common adverse corpus and independent structural oracle.

| Operation | Rule / portable evidence | JS | Python | TS | C / C++ |
| --- | --- | --- | --- | --- | --- |
| load, validate | schema structures + exact graph refs; original catalog + hardening cases + self/examples | yes | yes | yes | yes, first error |
| getEntity / lookup | exact ID, full JSON; complete and unknown fields | yes | yes | yes | yes; C++ wraps C |
| lists | sorted IDs; complete fixture | yes | yes | yes | unsupported |
| traceEntity | bidirectional closure, cycles; complete + circular fixture | yes | yes | yes | unsupported |
| explainDependency | standard explanation projection; complete fixture | yes | yes | yes | unsupported |
| audit | stable findings, no inferred pass; model tests | yes | yes | unsupported | unsupported |
| evaluateReplacement | closed-world supplied claims; golden partial + fail/pass tests | yes | yes | yes | unsupported |
| verifyMigration | required referenced evidence + closed-world aggregation; preserving/violating goldens | yes | yes | unsupported | unsupported |
| normalize | scalar ordering + byte golden, subject to numeric gap | yes | yes | yes | unsupported; raw serialization only |
| describe / v0.1 facade | API operations + structured operational errors; public-api tests | yes | unsupported | unsupported | unsupported |

The CLI maps Python operations as documented in Public API v0.1 and is still a partial
adapter. Missing native operations are not claimed as newly removed functionality:
the original C API has load/free/count/lookup/validate/serialize only. `fw_serialize`
is source-preserving model-envelope serialization, not canonical `normalize`.
Native callers must check the header/support table rather than assume v0.1 discovery.

C++ is a wrapper of C, not independent semantic evidence. TS and JS use separate
query/evaluation bodies but share the structural/serialization algorithm. Python's
structural/serialization implementation and the Draft 2020-12 oracle are independent
of that algorithm, while all consume the same published schema constraints. This
is fixture-level evidence, not independent implementations of every operation.

## Additive lossless coverage

JS `parseLossless` / `loadModelLossless`, Python `parse_lossless` /
`load_model_lossless`, and TS equivalents preserve exact original documents and
provide token-aware queries plus decimal-v1 normalized output. C `fw_load_lossless`
and C++ `model(path,true)` preserve raw JSON and check numeric schema bounds with
an independent decimal comparator; native decimal-v1 output remains unsupported.
Legacy modes remain available. JS/TS share token/parser algorithms; Python uses
Decimal tuples and its standard JSON parser; C uses retained raw tokens and its own
bounded comparator. `make hardening` runs reviewed numeric vectors, actual output
bytes, source round trips, exact-constraint oracle cases and domain failures across
these paths. `make sanitizer` covers legacy and lossless native parsing.
