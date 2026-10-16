# Additive lossless interchange, decimal-v1

This optional adapter contract does not narrow Standard 0.1 or change existing API
v0.1 operations. Existing `loadModel`, host objects, and `normalize` remain compatible.
New consumers may explicitly select lossless text loading and `decimal-v1` output.
No new wire record kind, arithmetic system or runtime dependency is required.

`parseLossless(textOrBytes)` / Python `parse_lossless` returns an immutable document:
`value` contains ordinary objects/arrays/strings/booleans/null and immutable numeric
tokens (`JsonNumber.token`). All numbers use tokens so type/precision never depends
on magnitude. `source()` returns the exact original UTF-8 text, including number
spelling and whitespace. `canonical()` returns deterministic `decimal-v1` text.
Token JSON serialization/coercion is deliberately rejected; use the supplied writer.

Supported domain: finite mathematical JSON decimals, token length <=4096 ASCII bytes,
significant coefficient <=4000 digits, explicit and adjusted exponent absolute value
<=1,000,000 (bounds close canonical numeric tokens under re-ingestion); JSON strings are Unicode scalars,
duplicate decoded keys are invalid, root depth <=64, document UTF-8 bytes <=1 MiB.
NaN/Infinity are not JSON numbers; `1e400` and `1e-400` are supported finite decimals.
Limits fail explicitly, without exponent expansion or silent rounding. Filesystem
model loading retains the existing 16 MiB/4096-record containment policy.

Canonical decimal-v1: remove coefficient leading/trailing zeros, account for decimal
point and exponent exactly, render all zeros as `0` (including negative zero).
Use plain notation when the nonzero leading digit's decimal exponent is -6 through
20 inclusive, otherwise one leading digit, optional fractional digits, `e`, signed
exponent without redundant zeros or a positive `+`. Equivalent decimal spellings
produce identical bytes. This is exact decimal value canonicalization, not preservation
of original spelling; `source()` preserves spelling. Objects/Unicode/arrays/indent/LF
follow the existing normalized byte contract. No Unicode normalization or signing
claim is introduced. Output space is bounded by coefficient length, not exponent.

`loadModelLossless` / `load_model_lossless` exposes model queries with token values;
`normalized()` uses decimal-v1 and `sourceDocuments()` / `source_documents()` returns
the original inventoried documents. Numeric schema minimum/maximum checks compare
exact decimal values, including confidence just outside 0..1 that binary64 rounds
onto a boundary. The legacy loading path remains explicitly a host-number interface.

Programmatic writers accept JsonNumber tokens and ordinary safe integers; other host
numbers must be explicitly represented as tokens. A number already rounded before
this API receives it cannot be recovered. `document.toHost()` / `to_host()` permits
native values only when their emitted decimal JSON value round-trips exactly;
`allowLoss:true` / `allow_loss=True` explicitly permits finite rounded projections.
Neither projection preserves original spelling; neither reconstructs prior precision.

Compatibility matrix:

| Input / API | Old mode | New lossless mode |
| --- | --- | --- |
| Historical small-number model | unchanged native values/goldens | token values, exact source; same bytes where numeric rendering agrees |
| 9007199254740993 | legacy JS rounding remains documented | exact token/source/canonical value; strict host projection rejects |
| Precise fractional confidence | legacy host precision | exact numeric constraint enforcement |
| Huge/tiny exponent | legacy finite host limit | supported within explicit token/exponent bounds |
| Already-rounded host object | no recovery claim | unsafe host numbers rejected; explicit original token required |
| Source vs canonical | legacy normalized text | separate exact source and versioned decimal-v1 bytes |

JS and TS share the implementation. Python is independently implemented using the
standard Decimal representation without context-rounded arithmetic. C/C++ retain
source-preserving serialization; canonical decimal-v1 is not advertised for native
bindings. Tests must distinguish these implementations and compare actual bytes
against reviewed expectations and an independent structural oracle.

CLI: pass global `--lossless` before an existing command to select this mode, e.g.
`packages/cli/bin/forever --lossless --root conformance/lossless/forever normalize`.
C exposes `fw_load_lossless` and C++ `model(path,true)`; source serialization retains
original number spellings, while exact min/max checks use an independent comparator.

Text/file byte limits apply at ingestion. Pretty printing or normalized multi-record
output may be larger than one input file; this does not relax a later ingestion limit.
Numeric canonicalization never expands a million-place exponent into a million zeros.
