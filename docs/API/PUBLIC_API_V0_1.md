# Forever Works Public API v0.1

**Status:** implemented in JavaScript; other adapters are partial  
**API version:** `0.1`  
**Model versions supported by the JavaScript adapter:** `0.1`

## 1. Contract and authority

This is the transport-neutral semantic interface for interrogating a Forever Works model. It is subordinate to the normative standard, schemas, and conformance fixtures. JavaScript and CLI examples are adapter mappings, not the definition. UTF-8 JSON is the common representation. HTTP and MCP are intentionally deferred and are not canonical.

The API version describes this operation contract. `foreverVersion` describes the model format. They evolve independently: an adapter MUST report both its API version and supported model versions.

## 2. Discovery

`describe()` takes no arguments and returns:

* `foreverApiVersion`: `"0.1"`;
* `supportedModelVersions`: sorted model versions;
* `operations`: sorted supported operation names;
* `implementation`: non-normative name and version;
* `adapter`: non-normative adapter information.

Clients MUST use `operations` rather than infer support from implementation identity. An adapter receiving an unsupported operation MUST return `unsupported-operation`; JavaScript object consumers naturally cannot call absent methods and SHOULD check `describe()` first.

## 3. Operations

All list and trace results are arrays of complete record JSON objects sorted by `id`. Unknown record fields are preserved. Inputs named `id`, `current`, or `candidate` are exact, case-sensitive entity IDs.

| Operation | Arguments | Success result | JavaScript v0.1 |
| --- | --- | --- | --- |
| `describe` | none | discovery object | yes |
| `getProjectIntent` | none | first intent in deterministic ID order | yes |
| `getEntity` | `id` | matching record | yes |
| `listCapabilities` | none | capability records | yes |
| `listInvariants` | none | invariant records | yes |
| `listDependencies` | none | dependency records | yes |
| `listImplementations` | none | implementation records | yes |
| `traceEntity` | `id` | bidirectionally reachable records, including start | yes |
| `explainDependency` | `id` | dependency explanation fields defined by the standard | yes |
| `validateModel` | none | `{valid, errors}`; validation findings are data | yes |
| `audit` | none | `{issues, issueCount}` | yes |
| `evaluateReplacement` | `current`, `candidate` | conservative replacement evaluation | yes |
| `verifyMigration` | `id` | conservative migration verification | yes |
| `normalize` | none | canonical JSON text with trailing newline | yes |

`getProjectIntent` returns the lexically first intent if a model contains more than one. Validation is responsible for reporting structural model problems. Evaluation and verification preserve the standard's closed-world `pass` / `fail` / `partial` aggregation: missing claims or required evidence never pass.

## 4. Errors

Operational failures have a stable lower-case hyphenated `code`, human-readable `message`, and JSON-object `details`. Messages are not a compatibility surface. The JavaScript binding throws `ForeverApiError`, whose `toJSON()` returns:

```json
{"error":{"code":"entity-not-found","message":"entity not found: missing.entity","details":{"id":"missing.entity"}}}
```

Stable v0.1 codes are `entity-not-found`, `project-intent-not-found`, `dependency-not-found`, `implementation-not-found`, `migration-not-found`, and `unsupported-operation`. Entity absence is an operational error, not `null`. Validation findings instead appear in the successful `validateModel` result using the established validation issue codes.

## 5. Adapter obligations

A conforming adapter MUST:

1. implement every operation it advertises with the semantics above;
2. preserve record JSON and unknown fields;
3. obey deterministic ordering and normalization rules;
4. expose stable error codes in its native error mechanism and structured transport form;
5. keep diagnostics separate from a successful JSON result;
6. never treat missing evidence as a pass; and
7. avoid making vendor or adapter identity part of semantic correctness.

Bindings MAY expose additional implementation-specific helpers, but MUST NOT advertise them as v0.1 operations. Future HTTP, MCP, or other transports should map arguments, results, and errors without redefining them.

## 6. JavaScript mapping

```js
import {createForeverApi} from "@forever-works/javascript";

const forever = await createForeverApi("./forever");
console.log(forever.describe());
console.log(forever.getProjectIntent());
console.log(forever.listCapabilities());
```

`createForeverApiFromModel(model)` from `@forever-works/javascript/core` is the host-neutral construction path. Plain JavaScript consumption requires neither TypeScript nor `tsc`.

## 7. CLI and compatibility status

The existing CLI maps `validate`, `audit`, `explain`, `trace`, `evaluate-replacement`, `verify-migration`, and `normalize` to equivalent semantics. `inspect` is a legacy discovery-like command, not `describe`; list operations and stable structured operational errors are not yet exposed. Consequently the CLI is useful as a lowest-common-denominator JSON adapter but is not yet a conforming complete Public API v0.1 adapter.

Within API v0.1, new optional discovery fields and new error codes may be added. Operations, required fields, and meanings will not be removed or incompatibly changed. Consumers MUST ignore unknown object fields. An incompatible contract change requires a new API version; model-version support may change independently and must remain discoverable.

## 8. Published schema version strings

The record schemas' `foreverVersion` pattern matches ordinary version strings such as `0.1` and the retained `0.0` fixture (`^0\.[0-9]+$`). A prior overescaped pattern rejected the documented `0.1` values during independent JSON Schema validation even though the JavaScript model validator accepted them. Correcting the pattern aligns schemas with the existing model contract; it does not change Public API versioning, authority, or the supported-major-version rule. `packages/javascript/test/schema-version.test.js` retains the regression separately from reference-library conformance.

## 9. Hardened input and evidence boundary

See [core input and normalization](CORE_INPUT_AND_NORMALIZATION.md) for exact reference
fields, bounded filesystem loading, validation issues, output-byte rules and the
unresolved numeric-domain limitation. The [operation coverage map](OPERATION_COVERAGE.md)
is the authoritative implementation-status inventory for the other bindings.

A replacement `pass` is aggregation of supplied declarations under Standard 0.1,
including claims with optional evidence. It is not an observed execution result.
Neither replacement nor migration verification executes commands, fetches evidence
URIs or converts confidence into authority. No stronger evidence policy is added to
API v0.1 by this hardening change.

## 10. Optional lossless interchange

`loadModelLossless`, `parseLossless`, `JsonNumber` and `canonicalLossless` are additive
adapter helpers, not new v0.1 discovery operations or a new model edition. See
[LOSSLESS_JSON.md](LOSSLESS_JSON.md) for the exact supported decimal domain, source
preservation, token-aware model queries, schema checks and decimal-v1 byte format.
Existing consumers retain their host-number values and historical normalization.
Applications must use the lossless writer for token-bearing values; ordinary JSON
serialization is deliberately rejected rather than silently emitting token objects.
Parser/profile errors use `invalid-number`, `resource-limit`, `invalid-unicode`,
`duplicate-member` or `invalid-json`; projections use `unsafe-host-number`,
`lossy-number-projection`, `unsupported-host-number` and explicit-writer/coercion errors.
Filesystem loaders retain their existing structured failure stage/path mechanisms.

CLI mapping: global `--lossless` selects token-aware loading and decimal-v1 JSON for
existing commands; `normalize` remains its existing command name. Without the flag,
loading/output are unchanged. This optional mode does not make the CLI a complete
Public API v0.1 adapter. Parse/projection/resource failures remain operational failures.
