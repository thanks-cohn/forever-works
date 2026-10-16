# Foundation readiness audit — 2026-10-15

## Verdict and scope

Audited source: `9a66a82b87cd18cbba8e360518524724fa46e427`.
Read-only implementation review and local runtime probes; no production code changed.
This is an agent assessment, not certification, a security audit or an exhaustive review.

Forever Works is a real early foundation with worthwhile architectural principles and executable tooling. It is suitable for controlled adoption experiments. It is not yet ready to be represented as a hardened general-purpose interoperability standard or a proven documentation-only ecosystem/product generator.

The owner's ambition is a foundational, widely adopted future standard. The most useful next work is to make current promises true for adversarial and independently authored inputs, then demonstrate source-independent inheritance on real interactions. Further vision documents cannot substitute for those proofs.

## What exists and is valuable

- Language-neutral Standard 0.1, UTF-8 JSON records and Draft 2020-12 schemas.
- Intent, capability, invariant, constraint, compatibility, rationale, implementation and evidence separated conceptually.
- An implemented JavaScript Public API v0.1, independent plain-JavaScript consumption/package proof and Python/TypeScript bindings.
- A C portability prototype and C++ RAII wrapper, though their semantics are much narrower than a conforming binding.
- Shared fixtures, normalization/evaluation goldens, migration/replacement examples and continuous integration.
- An optional ecosystem composition profile with bounded loading, explicit authority/state/configuration modeling and substantially broader negative tests.
- The composition profile deliberately leaves runtime verification UNKNOWN, even for metadata claiming PASS. That is an important sound design boundary.

## Executed baseline checks

After installing the pinned-lockfile Node development dependencies, `make test` completed successfully locally:

- Python: 6 tests.
- JavaScript: 76 tests including nested conformance cases and the optional profile.
- TypeScript: 2 tests.
- C and C++: one existing smoke executable each.
- Cross-language runner: existing Python/TypeScript/JavaScript normalization goldens for minimal and complete fixtures passed.

An earlier attempt stopped because TypeScript was not yet installed; the completed rerun supersedes that environment blockage.
Latest CI for the audited commit: workflow 38833158152 passed its test, javascript and ecosystem-schema jobs.
Independent local Draft 2020-12 checks also ran: all 38 composition fixtures and the independent profile-normalization golden passed. All 16 file-transfer example records passed structural schema validation. The 21-record self-model had one structural error (see F1). CI's schema job covers the optional profile, not all canonical self-model records or the extra probes.

## Reproduced findings

### F1 — core validation accepts schema-invalid records (high priority)

Files: `packages/javascript/src/model.js`, `bindings/python/foreverworks/model.py`, `packages/typescript/src/index.ts`.

JavaScript accepted each of these without a validation finding:
- ID `INVALID ID!`.
- Record version `99.0` under a `0.1` manifest.
- Numeric `name` and null `statement`.
- Provenance source `made-up` and confidence `99`.
- A dangling relationship reference `missing`, which contains no dot even though undotted IDs are permitted by the ID grammar.

A combined record containing those defects also returned an empty error array in Python and TypeScript. The schemas constrain these values, but the model validators are handwritten partial checks and do not enforce the same contract. Passing structural validation therefore has inconsistent meanings depending on the entry point. This matters for adopters relying on the advertised validateModel API.

An independent Draft 2020-12 validator reported six structural errors in the combined runtime-accepted capability record. It also found the repository's own `forever/invariants/javascript-independent-proof.json` uses verification type `conformance-suite`, while the schema permits `external-conformance-suite` but not `conformance-suite`. The current test suite remains green despite that actual self-model/schema discrepancy.

The reference extractor uses a dot heuristic and a handpicked field list. Clarify the schema/spec classification of every relationship and requirement field, then enforce it consistently without mistaking free prose or source paths for entity references.

### F2 — canonical ordering differs across implementations (high priority)

JavaScript's `normalize({Z:1,a:2,A:3,z:4})` orders keys `a,A,z,Z` in this environment because it uses localeCompare. Python orders `A,Z,a,z`. The existing goldens do not exercise this case.

Unknown fields are allowed, so this is not restricted to invalid record IDs. Locale-sensitive ordering is not portable canonical ordering. Specify and test the exact portable ordering/number domain, including integer-like keys, non-ASCII keys, array significance and precision boundaries, with independent goldens.

### F3 — C validation is not equivalent even on existing negative fixtures (high priority)

Files: `bindings/c/src/forever.c`, `bindings/c/tests/test.c`; C++ wraps this same implementation.

A small harness using fw_load, fw_validate and fw_record_count produced:
- `invalid-missing-id`: valid=1, records=0 (bad record silently dropped).
- `invalid-reference`: valid=1, records=1 (broken reference accepted).

The loader scans for string fragments rather than parsing the documented JSON structure. Its smaller query surface is acknowledged, but that does not justify accepting malformed input or silently omitting records. The present C/C++ tests are smoke checks, not cross-binding conformance evidence. Replace the parser/loader safely and explicitly state partial support until it meets the common contract.

### F4 — JavaScript model loader follows a symlink outside its root (high priority)

File: `packages/javascript/src/node.js`.

A temporary model with linked.json symlinked to a harmless generated sibling JSON file loaded the external record and returned no validation errors. The loader checks a lexically resolved path prefix, not the actual resolved target. Python resolves targets and the newer composition loader has separate symlink handling.

The format requires paths to stay within the model directory. Define the trusted-checkout versus security-boundary assumptions and enforce real containment, including missing files, malformed manifest inventories and resource bounds. Do not imply complete hostile-filesystem protection without race-safe design and tests.

### F5 — replacement PASS is declaration aggregation, not independently verified proof

A valid dependency requiring one capability plus an implementation with `claims:[{requirement:"capability.good",status:"pass"}]` produced replacement result `pass` without evidence.

The current core specification allows claims with optional evidence and says a supplied claim controls its check. Thus this finding is a trust/contract limitation, not automatically a violation of that sentence. API and user-facing wording must make that scope clear. A core aggregate PASS cannot be promoted to verified software behavior. Define stronger evidence acceptance as an explicitly versioned policy if needed; do not silently rewrite semantics or treat filenames as verified evidence.

The ecosystem profile's always-UNKNOWN static result demonstrates a clearer distinction between declaration and execution. Preserve that distinction.

## Gaps relative to the documentation-only ambition

- No executed source-restricted two-product-to-third-product experiment was established by this review. Synthetic topology fixtures are useful structural examples, not working product interoperability.
- The composition profile has a JavaScript semantic implementation and independent structural schema checks, but no second semantic binding or authenticated runtime evaluator.
- A validated model can still lack wire formats, state machines, pseudocode, migration details and acceptance fixtures needed to build a compatible app without source access. Model conformance is not documentation sufficiency.
- CLI completeness and cross-binding API coverage remain explicitly partial.
- Independent adopter tests, a portable inheritance-package export/validation workflow and repeatable held-out reconstruction evidence are still needed before strong foundational claims.

## Recommended work sequence

Run [the bounded core hardening request](../../codex/CORE_HARDENING_AND_SOURCE_INDEPENDENT_PROOF_REQUEST.md) first. Fix current validation/normalization/loader discrepancies against existing semantics and add meaningful cross-binding tests. Record exact scope and avoid claiming all bindings conform when only a subset does.

Then construct two small real participants with complete portable contract packages. Run a separate cold construction exercise to build a third participant from those packages alone and independently test real effects. Document gaps rather than coach around them invisibly. Extend this to Atlas/Redown only once their actual shared contracts are stable enough.

Readiness ladder: experimental foundation → hardened interoperable core → verified inheritance package → independently demonstrated ecosystem generation → broader external adoption. No stage guarantees becoming the de facto standard, but each supplies evidence the next stage needs.
