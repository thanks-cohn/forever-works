# Core input, validation and normalization

This reference refines Public API v0.1 implementation obligations. Standard 0.1,
[versioning](../../spec/VERSIONING.md), schemas and retained fixtures remain the
authority. No new record kind, transport, service, capability grant or evidence
executor is introduced. See [the operation map](OPERATION_COVERAGE.md) for scope.

## Structure and graph

Validation checks the manifest and each record against the core schema constraints:
required fields, object/array/string/number types, IDs, enums, provenance confidence,
unique string arrays and extension owner names. Unknown fields remain accepted.
A parsed record with a missing ID remains a record and produces a finding; it must
never disappear. Inventory errors fail loading rather than silently skipping entries.
The structural engines implement only the subset used by the checked-in schemas;
they are not general Draft 2020-12 processors. Schema changes require extending the
engines and comparing against the independent development oracle.

Version syntax is `0.<one or more decimal digits>`. Historical `0.0` and understood
newer `0.x` minor versions are readable under the existing compatibility policy.
A manifest and record with different understood minor versions are not automatically
invalid; incompatible majors and malformed versions are rejected independently.
Discovery's `supportedModelVersions:["0.1"]` names the implemented normative edition;
JavaScript additionally describes its minor-version compatibility policy.

These fields refer to exact IDs, including undotted IDs:

| Kind | Exact entity references |
| --- | --- |
| intent | relatedCapabilities, relatedConstraints |
| capability | relatedInvariants, relatedImplementations; verification[].evidence |
| invariant | scope, relatedCapabilities; verification[].evidence |
| constraint | scope; verification[].evidence |
| dependency | currentImplementation, requiredCapabilities, protectedInvariants, relatedConstraints, compatibilityObligations |
| decision | relatedEntities |
| compatibility | validationReferences |
| implementation | satisfiesCapabilities, constrainedByInvariants, satisfiesConstraints, compatibilityContracts; claims[].evidence |
| migration | sourceImplementation, targetImplementation, preservedCapabilities, preservedInvariants, compatibilityImpact, verification; claims[].evidence |
| evidence | none |

Only fields defined for that kind acquire these semantics. Extension objects and
unknown fields cannot acquire reference or execution authority just by their spelling.
Cycles are valid. Missing reference targets are errors; references do not require a dot.

The shipped examples establish that capability inputs/outputs/requiredProperties,
intent priorities/nonGoals/supportedEnvironments, decision alternatives/assumptions/
mayChange/mustSurvive/revisitConditions, compatibility mustPreserve/mayChange,
implementation sourceLocations/runtimeRequirements and migration assumptionsRetired
are descriptive strings, not automatic entity references. Blanket schema descriptions
calling all string arrays IDs have been corrected. `replacementRequirements` and
`claims[].requirement` are exact requirement labels and can identify requirements
outside the entity inventory (the retained configuration-compatible example does so).
A future typed reference design would require deliberate compatible evolution.

## Filesystem loading policy

The filesystem adapters enforce the following bounded input policy:

- UTF-8 with malformed byte sequences rejected; JSON syntax must be valid. Decoded
  strings must contain Unicode scalars (no unpaired surrogates); non-finite decoded
  host numbers are unsupported in legacy mode; the lossless mode accepts finite
  mathematical decimals within its documented token/exponent limits.
- Duplicate decoded JSON member names rejected, including escaped equivalents.
- Maximum nesting 64 (root at depth zero), 1,048,576 bytes per file,
  16,777,216 bytes including manifest, and 4,096 inventoried records.
- Portable relative `.json` paths, no absolute/drive/UNC paths, backslashes or `..`
  path segments. Missing files, non-files and malformed inventories fail loading.
- Both lexical location and the existing real target must remain under the model
  directory. Within-root symlinks are allowed; outside targets are rejected.
- Duplicate listed paths are rejected (native spelling aliases may instead reach
  duplicate-ID validation). Content is data: no verification command, source URI,
  grant, confidence or PASS assertion is executed or dereferenced.

Duplicate-member rejection resolves JSON's ambiguous interoperable behavior; the
resource limits are adapter input limits, not new model-schema fields. All retained
valid fixtures fit. Applications needing larger models need a separately documented
adapter policy and resource evidence. These checks assume a stable directory and
ordinary regular files. They do not defend against concurrent hostile replacement
between real-target inspection and opening; no race-safe security boundary is claimed.
Windows CI is configured; only the executed platform results in the report are proven.

## Normalized bytes

A normalized model replaces the manifest's path inventory with complete records sorted
by ID, retaining other manifest fields. Key ordering is ascending Unicode scalar value,
recursively, independent of locale and host object enumeration. Record IDs are ASCII;
key ordering also applies to supplementary characters and integer-looking keys.
Objects and arrays use two spaces, LF, UTF-8 without BOM and one trailing newline.
Strings use JSON escapes for quotation, backslash and controls; other Unicode scalars
are emitted directly. Lone surrogates cannot be emitted as UTF-8 scalar text. Ordinary
array order is significant; only normalized record order is sorted. A normalized
in-memory JavaScript object alone does not prove these output bytes.

The reviewed golden covers mixed case, punctuation, nested objects, integer-like keys,
BMP/supplementary Unicode, escaped strings, significant arrays, negative zero (output
`0`), integral floats (`1`), decimal/exponent boundaries and `2^53-1`. JS and TS use the
same serializer algorithm; Python supplies a separate implementation. C/C++ serialize
preserved source documents and do not advertise canonical normalization.

**Numeric modes:** the legacy host-number API retains its existing binary64 behavior
in JS/TS. For portable preservation, select the additive
[lossless interchange contract](LOSSLESS_JSON.md): exact original text, immutable
numeric tokens, exact schema comparisons and separately versioned decimal-v1 output.
This closes the advertised lossless path within explicit input/resource bounds,
without narrowing Standard 0.1 or claiming to recover precision lost before ingestion.
Native bindings expose an additive lossless loader with source-preserving output;
canonical decimal-v1 is implemented in JS/TS and independently in Python.

RFC 8785/JCS was assessed as an alternative: its compact bytes, UTF-16 ordering and
ECMAScript number contract differ from the existing two-space/newline contract and
scalar-order clarification. Switching to JCS would need a distinct version/profile
and retained old fixtures. No signing, hashing-security or universal canonicalization
guarantee follows from the current golden's SHA-256 agreement.

## Failure stages and evidence

Structural/semantic findings remain `{code,path,message}` with optional `reference`.
Existing `missing-required`, `invalid-record`, `invalid-kind`, `invalid-classification`,
`unsupported-version`, `duplicate-id` and `broken-reference` remain; structural
checks also use `invalid-type`, `invalid-value`, `duplicate-value`, `unknown-field`.
The path identifies the affected manifest/record field. Fix that field against its
schema; a broken reference needs an inventoried target or corrected reference.
Messages are explanatory, not stable identifiers, and do not include document content.

Loading fails before a Model is returned. Adapter errors identify malformed input,
manifest/path/byte/count/depth failure; native `fw_error.code` includes `io`,
`path-escape`, `resource-limit`, `invalid-json`, `invalid-utf8`, `invalid-type`,
`missing-required`, `unknown-field`, `duplicate-path`, `allocation`. Native errors use
a bounded message and first-error representation. JavaScript wraps loader failures in `ForeverApiError` with `details.stage:"load"`
and `details.path`; Python `ModelError` carries `code`, `stage` and `path`. TypeScript attaches the same `code`/`details` shape to its native Error. Native C/C++
retain the compatible first-error `fw_error`/exception mechanism rather than adding
fields to the C ABI.
Operational Public API errors retain their existing separate mechanism.

Replacement PASS aggregates supplied claims, with optional supplied evidence. It does
not execute or independently verify the candidate. Migration evidence references are
required as specified, but artifact existence/metadata likewise does not establish
executed behavior. Evidence confidence never confers authority or permission.
