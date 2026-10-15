# Experimental composition profile reference adapter 0.1

This is a **profile-specific reference interface**, separate from Public API v0.1.
No profile operation is added to that API's `describe().operations`, and there is
no new claim of CLI, C, C++, Python or TypeScript profile support. The portable
[profile contract](../../spec/profiles/ecosystem-composition/v0.1/README.md), schema
and fixtures define meaning independently of this JavaScript mapping.

## Implemented helpers

Import the semantic core from
`packages/ecosystem-composition/src/core.js` or filesystem helpers from `src/node.js`.
These are repository source modules, not a newly published package export.
The current proof target is Node.js 20.18+ with JSON import attributes; no
TypeScript compiler or runtime dependency is needed.

| Helper | Inputs | Result |
| --- | --- | --- |
| `validateComposition` | parsed composition; optional `{records}` array of already validated canonical records | `{valid, issues, verification}`; findings are data, verification always `UNKNOWN` |
| `normalizeComposition` | parsed JSON | Two-space JSON, lexically sorted object keys, preserved array order, trailing newline; input must be finite, acyclic JSON |
| `safeRelativePath` | value | Boolean lexical safe-path check; no filesystem access |
| `loadComposition` | root directory, relative path (default `composition.json`) | Promise of parsed JSON; no validation or side effects |
| `validateCompositionFile` | root, relative path, optional validation options | Promise of the validation result |
| `loadOptionalComposition` | root, canonical manifest, optional validation options | `{enabled, document, validation}`; absent pointer gives `false, null, null` |

`PROFILE` exports the stable profile identity URI. Core validation preserves input
and is deterministic for the same JSON and record context. `issues` sort by JSON
pointer path, code, then message; obligation results sort by ID. Validation errors
have severity `error`, undetermined behavior has severity `warning`. Structural
schema failures stop further reference validation. Error message text is not a
compatibility contract. Unknown versions and unrecognized core fields fail;
owner-qualified extensions are retained and warn. This differs deliberately from
canonical Standard 0.1's unknown-field policy only within the opt-in profile.

Provenance is never upgraded. `records` must first pass the existing model's own
validation; the core checks exact ID/kind resolution but does not reimplement that
validator. Omitting records leaves references visibly unresolved. `valid: true`
does not authenticate authority, check policy behavior, or verify evidence.

## Stable validation issue codes

| Codes | Meaning |
| --- | --- |
| `schema-type`, `schema-required`, `schema-const`, `schema-enum`, `schema-pattern`, `schema-min-length`, `schema-min-items`, `schema-unique-items`, `schema-additional-property` | Structural schema violation |
| `input-limit`, `record-context` | Reference implementation bounds / invalid canonical context |
| `duplicate-id`, `duplicate-port`, `dangling-reference`, `dangling-port`, `port-direction` | Identity, resolution or direction violation |
| `record-not-found`, `record-kind`, `requirement-kind` | Canonical reference does not match its declared purpose |
| `nested-cycle` | Forbidden ecosystem containment cycle |
| `authority-scope`, `state-authority` | Grant escapes endpoint/state scope or contradicts declared state stewardship |
| `binding-scope`, `inactive-endpoint`, `inactive-state-owner` | Invalid active topology |
| `obligation-scope`, `evidence-scope`, `evidence-subjects`, `unsafe-path` | Invalid obligation/evidence linkage, applicability, artifact identity inventory or path |
| `record-unresolved`, `authority-unreviewed`, `unsupported-semantics`, `unsupported-extension`, `unsupported-permission`, `parameters-uninterpreted`, `evidence-unverified`, `obligation-missing` | Warning: unresolved, unsupported, unauthenticated or absent semantics/proof |

Every validation result carries `verification.status: "UNKNOWN"`; each reported
obligation has `{id, status: "UNKNOWN", reason}`. Evidence claim statuses are
preserved independently, including `PASS`, `FAIL`, `UNKNOWN`, `NOT_RUN`; none is
an executed outcome. Evidence includes an artifact digest, an accepted `scopeArtifact` snapshot digest,
claimed environment and participant digests. The adapter does not read evidence
bytes, authenticate the snapshot or run commands.

## Loading and CLI errors

`CompositionLoadError` has a stable `code` and explanatory `message`. Codes are
`unsafe-path`, `invalid-json`, `invalid-encoding`, `input-limit`, `load-failed`,
`invalid-profile-reference`, and `unsupported-profile`. The manifest pointer is
`extensions["forever.works.ecosystem-composition"]` containing exactly
`{profileVersion: "0.1", path: "composition.json"}`. No pointer means disabled;
the adapter does not scan for files or implicitly enable a profile.

```sh
node scripts/validate_composition.mjs ROOT RELATIVE_JSON [CANONICAL_MODEL_ROOT]
```

The standalone script writes one JSON document on stdout. Exit 0 means structural
validation passed, exit 1 means validation errors, exit 2 means operational or
argument failure. CLI-only `invalid-argument` and `invalid-model` codes cover bad
arguments and an invalid canonical context. Operational errors use
`{error: {code, message}}`; validation errors stay in the normal result. This
script does not alter mappings or error behavior of `packages/cli/bin/forever`.

`listEcosystems`, `getEcosystem`, `listParticipants`, `listInteractions`,
`resolveConfiguration`, authenticated verification and a profile `describe()`
wrapper remain deferred. Consumers must not infer support from this document's
candidate names or treat these helpers as Public API v0.1 operations.
