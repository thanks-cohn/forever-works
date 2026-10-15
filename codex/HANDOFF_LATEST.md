# Latest implementation handoff

**Date:** 2026-10-15. **Repository:** `thanks-cohn/forever-works`. **Branch:** `main`.
**Session:** bounded ecosystem composition profile implementation.

## Commits and integration

- `c9bce473cb4d6b330972a9d26f4da9d6a11bf914` — `feat: add optional ecosystem composition profile and conformance proof`; successfully pushed to `origin/main` and confirmed with `git ls-remote`.
- This handoff is committed separately as `docs: record ecosystem composition implementation handoff`; inspect `git log` for its final hash.
- Started from the clean onboarding checkout, created local `main`, and fast-forwarded to remote `07a3f4c`. Before the implementation push, integrated concurrent `1aec043` and `d14a3e9` documentation commits by rebasing the unpublished implementation commit. The README append conflict was resolved by retaining both research documentation and the new profile section. No force push, reset or removal of remote work.

## Implemented, not merely proposed

- Optional profile identity `https://forever.works/profiles/ecosystem-composition`, version `0.1`; self-contained Draft 2020-12 schema at `spec/profiles/ecosystem-composition/v0.1/composition.schema.json`.
- Collective canonical intent references, arbitrary participant roles, qualified ports, provided/required capabilities, directed many-party interactions, multiple edges and communication cycles, nested suites with acyclic containment, explicit state stewardship/writers and alternate active configurations.
- Typed contract categories distinguish semantic, ordering, concurrency, retry, idempotency, consistency, offline/failure/recovery, authority/data access, state and version compatibility. Parameters remain opaque and visibly uninterpreted; no runtime policy interpreter is claimed.
- Bounded, dependency-free plain JavaScript reference validator in `packages/ecosystem-composition/src/core.js`, plus filesystem loader and optional manifest-extension discovery in `src/node.js`.
- Stable issue codes, sorted results, deterministic object-key normalization preserving array order, explicit structural errors versus undetermined warnings, and no mutation/promotion of provenance.
- Checks exact canonical ID/kind references when supplied an independently validated model; absent context remains visibly unresolved. Checks duplicates, ports/directions, topology activation, forbidden nesting cycles, grants crossing endpoint/state scopes, unauthorized writers, obligation applicability and evidence linkage/subjects.
- Every evidence claim binds an obligation, configuration, canonical evidence record, artifact path/digest, accepted-scope snapshot path/digest, claimed environment and all active participant digests. Static validation never authenticates those claims or reads/executes artifacts. Suite and obligation verification always remain `UNKNOWN`, including declared `PASS` or `FAIL` claims.
- Safe relative paths, resolved symlink-escape rejection, strict UTF-8, regular-file checks, 4 MiB loader bound, and core limits of 100,000 JSON values/depth 64. These are reference implementation bounds, not abstract participant limits.
- Standalone `scripts/validate_composition.mjs` emits JSON and preserves exit 0 (structural validity), 1 (validation errors), 2 (operational/argument errors).
- 38 portable shared fixtures, plus normalization/validation goldens, under `conformance/ecosystem-composition/v0.1`. Nine valid files include zero/one participants, four-party fan-in/out, many-to-many replication/shared service, bidirectional multiedges/cycles, two deployment configurations and a different person/instrument/library nested example. Twenty-nine invalid files exercise actual rejection cases.
- Adopter/specification guide, experimental adapter reference under `docs/API/`, dated decision history, README/conformance indexes, and independent schema CI job. The development-only JSON Schema oracle has an explicitly agent-proposed, unreviewed dependency-intent record.

## Compatibility boundaries

Normative `docs/STANDARD.md`, `spec/schemas/*`, canonical record kinds, existing record fixtures, Public API v0.1 reference/implementation, package declarations and lockfile are unchanged. The new self-description dependency record and manifest inventory entry are additive data. Existing JavaScript consumer packaging remains independently tested without TypeScript.

Optional manifest pointer:

```json
{"extensions":{"forever.works.ecosystem-composition":{"profileVersion":"0.1","path":"composition.json"}}}
```

Do not put compositions into `manifest.records`. No pointer means disabled. No profile operations are advertised by Public API v0.1 `describe()`. Permanent contracts do not depend on an agent, adopter, language, OS, transport or UI framework.

## Commands actually run and results

From `/workspace/forever-works`:

```sh
npm ci --ignore-scripts --cache /tmp/forever-works-npm-cache
node --test packages/javascript/test/ecosystem-composition.test.js
npm_config_cache=/tmp/forever-works-npm-cache make test
python3 scripts/check_ecosystem_schema.py
node scripts/validate_composition.mjs conformance/ecosystem-composition/v0.1 valid/four-participant-fan.json conformance/fixtures/complete/forever
git diff --check
```

- Profile JavaScript run: **55 tests passed, 0 failed**, including 38 catalog cases, loader safety, provenance, unknown policy/permission semantics, optional discovery, CLI exit statuses and goldens.
- Full `make test`: **6 Python tests; 76 JavaScript tests; 2 TypeScript tests; C binding smoke; C++ wrapper smoke; cross-language golden normalization — all passed**. The 76 JavaScript count includes the profile tests, not an additional 76 profile tests. No skipped/failing tests were reported.
- Independent `jsonschema` 4.26.0 Draft 2020-12 check: **38 fixtures passed their structural expectations**, schema metaschema validated, independent Python normalization matched the shared golden. This is not a second semantic profile validator.
- Representative CLI result: structurally valid, explicit unreviewed-provenance warning, all three obligations and suite `UNKNOWN`; exit 0. Negative CLI exit 1/2 cases are exercised in tests.
- `git diff --check`: passed. Source/test blobs were unchanged by the final README-only rebase conflict resolution.
- Node.js v24.19.0 and Python 3.12.14 were used locally. Node 20.18+ is the documented reference-module target; repository CI uses Node 20, but hosted CI execution was not observed in this session.
- Final full-suite output was captured in `/tmp/forever-works-final-test.log` (ephemeral, not repository evidence or a required future dependency).

Initial npm install/consumer proof failed because its default cache attempted to write outside the writable workspace. Retrying with `/tmp/forever-works-npm-cache` resolved it while preserving lockfile integrity and TLS/checksum verification.

## Pre-existing repository defect, independently confirmed

`packages/cli/bin/forever --root forever validate` returns `valid: false` with four pre-existing broken references:

- `decision.javascript-first-class` → `implementation.reference-bindings`.
- `decision.public-api-v01` → `implementation.reference-bindings`.
- `implementation.javascript-binding` → `capability.binding-conformance`.
- `invariant.javascript-independent-proof` → `capability.binding-conformance`.

Compared `loadModel(...).validate()` for an untouched `git archive 07a3f4c` checkout against the modified self-model: results were exactly equal, with **zero new issues**. The actual existing IDs appear to be `implementation.bindings` and `capability.cross-language-conformance`; investigate and fix separately with focused regression evidence rather than silently changing accepted records in this profile task. The current CLI exits 0 even when this validation JSON is false, so inspect the result, not just its process exit status. Shared compatibility fixtures still pass.

## Explicit limitations and next work

1. No real interacting products or independently authenticated suite evidence were executed. This is static profile/schema conformance, not interoperability certification.
2. One JavaScript semantic proof binding only. The custom schema walker implements the bundled schema vocabulary, not arbitrary JSON Schema. Independent Python checks structure and one normalization golden only. Future schema keyword additions must update the walker or replace it with an independently conforming implementation.
3. Precise retry, concurrency, ordering, consistency, recovery and compatibility policies are referenced/recorded, not executed. Unknown categories, parameters and extensions remain warnings/UNKNOWN.
4. No profile query facade or `describe()` wrapper, no `listEcosystems`/`resolveConfiguration`, and no changes to Public API v0.1 discovery. Add only after shared semantic conformance and concrete adopter needs justify a separately versioned API.
5. State has one logical authority plus explicit writers; distributed physical realization remains replaceable. Joint authority/ownership transfer and configuration-specific stewardship need explicit design/evidence if actual adopters require them.
6. Evidence snapshot/digests/environment/verifier are unauthenticated declarations. Snapshot contents, signatures, oracle independence, artifact bytes and actual interactions are not inspected. Never change static `UNKNOWN` into a fabricated PASS.
7. File safety assumes a trusted, non-concurrently-mutating checkout; the loader is not a sandbox. Number normalization is reference-host JSON serialization, not a signature canonicalization standard.
8. No automatic migrations; only profile 0.1 is supported. Core fields are strict; dotted owner-qualified extensions preserve forward experiments with warnings. Canonical Standard 0.1 unknown-field handling is unchanged.
9. The new jsonschema test dependency's rationale is intentionally unreviewed/agent-proposed. CI job configuration is committed; hosted results are unobserved.

## Environment configuration

Using the onboarding skill, saved a draft `install_script` that runs frozen npm installation from the existing checkout, and additive non-secret `npm_config_cache=/tmp/forever-works-npm-cache`. No services or `start_skill` are required. Draft persistence was confirmed; it does not execute, apply or publish changes. Review/save these changes in environment settings, then publish if reusing this prepared environment. No secrets or network-policy changes were requested. Current tests were run with the explicit cache override; fresh-task restoration/publication was not verified.

Each cloud task already runs in an isolated checkout. Use it directly; do not create a Git worktree unless explicitly requested.

## Copy-ready continuation prompt

Work in `thanks-cohn/forever-works` on `main`. Read `AGENTS.md`, this handoff, the profile contract/schema and `docs/API/ECOSYSTEM_COMPOSITION_PROFILE_V0_1.md`. Pull current remote work without discarding changes. Preserve Standard 0.1, Public API v0.1, legacy fixtures, independent JavaScript packaging and unreviewed provenance. Keep existing static verification UNKNOWN.

First run the listed checks with the writable npm cache. Implement a second independent semantic validator against the same versioned catalog and goldens; extend shared fixtures for demonstrated semantic gaps rather than copying JavaScript assumptions. Then map one synthetic multi-product adopter request into canonical records plus the optional profile, without adding an adopter dependency or treating request intent as accepted intent. Plan and execute two small genuinely interacting outputs with independent tests for allowed effects, state and recovery. Keep runtime evidence authentication a separate explicit contract; do not infer PASS from schemas/builds. Defer API breadth until these proofs justify it. Separately track/fix the four existing self-model references. Update official docs alongside any actual contract change, and commit/push an updated handoff with exact results and remaining unknowns.
