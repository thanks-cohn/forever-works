# Foundation hardening results — 2026-10-16

## Verdict

**INCOMPLETE against the full execution brief.** Implementation, regressions, CI
configuration and official documentation are checked in. The executed Linux corpus
passes. Broad numeric preservation/canonicalization remains a demonstrated failure;
Windows and hosted CI results have not been executed in this environment. No complete
conformance, certification, documentation sufficiency or commercial claim is made.

Starting commit: `ecb3369ae1f92b5710e8dd07d277ee2d63083097` (clean `work` branch).
This supersedes the brief's suggested `7460736` baseline. Finishing implementation:
`93fe561cb42b3ca1012018af721b48ee715eb6c9`. This report is a subsequent documentation
commit, so its own hash is obtained with `git log -1 --format=%H -- <this report>`;
embedding its own hash would be self-referential. No history rewrite or release.

Environment: Linux 6.18.44 x86_64; Node 24.19.0, npm 11.9.0, TypeScript 5.9.3,
Python 3.12.14, GCC/G++ 14.2.0. Independent oracle: jsonschema 4.26.0, attrs 26.1.0,
jsonschema-specifications 2025.9.1, referencing 0.37.0, rpds-py 2026.6.3,
typing-extensions 4.16.0. Oracle versions are pinned in
`scripts/requirements-schema.txt`. C parser: vendored cJSON 1.7.19, MIT, with the
explicit parsed-string length patch in `bindings/c/vendor/README.md`. clang-format
19.1.7 was used as a scratch formatting tool, not added as a build/runtime dependency.

## Reproduce

From the repository root, with Node, Python and C/C++ toolchains available:

```sh
npm ci
python3 -m pip install -r scripts/requirements-schema.txt
python3 scripts/reproduce_foundation_baseline.py
make test
make hardening
make sanitizer
python3 scripts/check_ecosystem_schema.py
python3 scripts/check_onboarding.py
python3 scripts/sync_core_contracts.py
git diff --exit-code
node scripts/observe_numeric_gap.mjs
```

The final numeric command intentionally observes a known failure; it is not a passing
conformance test. Expected: input `9007199254740993` becomes `9007199254740992` in JS.
The corresponding Python JSON value and native source-preserving serialization retain
the original integer. There is no hidden oracle/runtime disagreement in this report:
this precision disagreement is explicitly outstanding.

Local commands used `npm_config_cache=/workspace/forever-works/work/npm-cache` because
the default home cache was unwritable. Initial `npm ci` needed the managed environment's
network permission; no credentials or proxy values were printed. The default sandbox
also returned empty stdout from successful child processes; rerunning checks with the
supported execution permission enabled real subprocess output and the checks passed.
The first `make test` attempt was therefore an environment failure, not a clean baseline
PASS. The read-only baseline reproducer independently establishes F1–F4 at the actual
starting commit without changing the checkout or rewriting history.

Final `make test hardening` results:

- Python: 6 existing tests passed.
- Plain JavaScript: 79 tests passed, including the original 76 and 3 hardening tests;
  clean npm-pack consumer proof still runs without TypeScript.
- TypeScript: build plus 2 existing tests passed.
- Native C and C++ smoke tests passed; the common harness supplies adverse coverage.
- Original Python/JS/TS minimal and complete normalization goldens passed unchanged.
- Common hardening harness: 71 cases passed through Python, JS, TS, C and C++.
  These are 42 model cases, 10 historical cases, self-model plus 2 example manifests,
  and 16 loader/resource cases. Structural expectations use the independent Draft
  2020-12 oracle; graph expectations are checked separately by the semantic bindings.
- ASan/UBSan: 137 seeded malformed inputs, no sanitizer failure or false valid result.
- Optional composition profile: 38 independent schema fixtures and profile byte golden
  passed. The profile's static UNKNOWN verification boundary remains intact.
- Schema/algorithm snapshot regeneration left the committed implementation unchanged.

The last optimized common-harness observation was 8.280 seconds and maximum child
RSS 65,808 KiB. This is one local process observation, not a throughput guarantee or
whole-job peak-memory bound. Limits exercised: >1 MiB single file, >16 MiB aggregate,
4,097 otherwise-valid unique records, excessive depth, malformed UTF-8/JSON, duplicate
members and decoded equivalent names, missing files, POSIX traversal/absolute paths,
Windows drive/UNC spellings and actual outside-root symlinks. Windows path spellings
on Linux do not establish Windows filesystem behavior. Concurrent hostile filesystem
mutation is outside the explicitly stable-directory assumption.

## Findings to changes and regressions

| Finding | Reproduced starting behavior | Implementation / regression | Result |
| --- | --- | --- | --- |
| F1 structure and references | Five malformed JS probes each returned `[]`; audit also identified invalid self-model enum | Schema-subset validators in JS/TS and independently written Python/C; IDs, versions, fields/types/enums, provenance, uniqueness, exact undotted references, nested verification evidence; hardening catalog + oracle + all shipped models | PASS for corpus; numeric precision separately FAIL |
| F1 self-model | `conformance-suite` was invalid in invariant verification; stricter graph checks also found five stale target IDs | `external-conformance-suite`; correct links to existing bindings/conformance/evidence IDs; self-model independently structurally and semantically checked | PASS |
| F2 ordering | `a,A,z,Z` rather than Python's `A,Z,a,z` | Explicit scalar comparison and recursive byte emission, not property-sort + JSON.stringify; separately implemented Python serializer; reviewed mixed-case/punctuation/numeric-key/Unicode/number golden | PASS for golden and original fixtures; unrestricted numeric agreement FAIL |
| F3 native parser | missing-ID fixture: valid=true,count=0; dangling-reference fixture: valid=true,count=1 | Real bounded parser + lexical/UTF-8 preflight; preserve invalid records for validation; schema subset + graph checks; 42-case common corpus, native source round trips, 137 sanitizer inputs | PASS for applicable scope |
| F4 loader escape | outside-root symlink loaded with valid=true,count=1 | Real-target containment in JS/TS/Python/C; portable paths, strict inventories, duplicate members, resource bounds; real symlink and adverse loader tests | PASS on Linux under stable-directory assumption; Windows NOT_RUN |
| F5 trust boundary | supplied PASS claim can produce aggregate pass without executed evidence | Evaluation semantics retained; official API, input contract and newcomer path distinguish supplied claims from executed behavior | PASS as documented limitation, not verified replacement execution |

The F1 JS regressions were first run before fixing validation and failed on invalid ID;
a later read-only baseline probe reproduced every listed audit defect. F2–F4 baseline
observations are reproducible from the starting commit even though the final shared
native/loader harness was completed after the parser changes. No historical fixture
or original normalization golden was regenerated to make a failure disappear.

## Coverage, independence and authority

The authoritative operation-by-operation map is
[API/OPERATION_COVERAGE.md](../API/OPERATION_COVERAGE.md). The exact reference fields,
loader policy, diagnostics and serialization contract are in
[API/CORE_INPUT_AND_NORMALIZATION.md](../API/CORE_INPUT_AND_NORMALIZATION.md).

JS supplies all published API v0.1 operations and structured operational errors.
Python has model queries, audit, replacement and migration, but not the full discovery
facade. TS has loading, validation, lookup/list/trace, explanation, replacement and
normalization; audit and migration are unsupported. C has load/free/count/lookup/
validate/raw serialize only; C++ wraps that implementation. Missing operations are
reported, not advertised and then skipped by tests. The CLI remains a partial adapter.

JS/TS structural and serializer algorithms are shared; the TypeScript copies are
explicitly generated. They are separate consumption targets, not independent semantic
implementations of those algorithms. Python and native validation bodies are separate;
C++ is not independent of C. The independent Draft oracle establishes structural
agreement on the corpus, not graph semantics, executed verification or arbitrary inputs.
The finite corpus does not prove complete JSON Schema implementation; future schemas
must extend the subset engines and adverse cases together.

Scalar-order golden SHA-256 from the actual Python/JS/TS output bytes:
`f71cfadcda6f14d2e4479606c3eab8ada7ed7e8a066d41b44c37d87309555437`.
Native serialization is source-preserving, not advertised canonical normalization.
Native positive round trips include unknown fields, embedded NUL strings/member names,
significant arrays, and an unknown manifest integer beyond binary64's safe integer
range. Large-number preservation is not established in JS/TS.

## Compatibility decisions and unresolved questions

No core concept or mandatory SDK/service was added. C's vendored parser is a replaceable
binding detail, described by an agent-proposed, unreviewed dependency-intent record.
Required evidence remains separate from supplied claims; inferred/proposed provenance
is preserved without promotion. Version 0.x minor compatibility and old fixtures remain.
The normalization fixes retain two spaces/LF/trailing newline and existing golden bytes.
Unknown manifest fields now survive the normalized-envelope projection as well.

The schema descriptions incorrectly labeled many prose arrays/source paths as entity
IDs. The retained examples already used descriptive strings in these fields. They are
clarified as prose; actual relationship fields are kind-specific exact IDs. Replacement
requirement labels can be outside the inventory, as the retained configuration example
requires. This prevents both dotted-prose heuristics and accidental interpretation of
unknown reference-looking fields. A future typed reference vocabulary would need its
own reviewed evolution; no new ontology is made mandatory here.

**Outstanding numeric decision:** a full JSON-number contract was absent. Rejecting
all previously accepted large numbers under the same edition would narrow valid input;
continuing to round them is not lossless. A lossless number representation/API or an
explicitly versioned restricted domain needs acceptance, implementation, compatibility
fixtures and independent bytes. JCS was assessed but its compact layout, UTF-16 key
ordering and number contract cannot silently replace this format. The report does not
call a restricted test golden universal canonicalization or a signing guarantee.

Duplicate-member rejection and size/depth/count limits are explicit adapter policies.
All retained valid cases fit; unbounded/ambiguous JSON loading was not a portable
promise. Generic operational error messages are not compatibility surfaces; issue codes
and existing public error representations are preserved, with additive loader details.
No C ABI fields were added to `fw_error`. Loader error paths are bounded/contextual;
C's first-error diagnostic remains less detailed than JS/Python/TS findings.

## Acceptance table

| Completion gate | Status | Evidence / limit |
| --- | --- | --- |
| Read instructions, current baseline, contract map | PASS | Actual starting hash, read-only reproducer, official operation/reference maps |
| Previously valid historical cases remain valid | PASS | Original `make test`, 10 historical cases through all five targets; unchanged goldens |
| F1 structural/semantic regressions + oracle + self/examples | PASS | 42 adverse/positive model cases, independent Draft oracle and three shipped manifests |
| No silent record loss | PASS | Count assertions on loaded invalid records; native missing-ID case now retained and invalid |
| Preserve all valid unknown numeric data through every target | FAIL | `observe_numeric_gap.mjs`; JS/TS binary64 rounding |
| No unreported schema/runtime disagreement | PASS for executed corpus | Structural and graph expectations separated; numeric disagreement expressly recorded |
| Documented cross-language normalized bytes | PASS for tested subset | Python/JS/TS original and reviewed new golden, exact digest; TS shares JS algorithm |
| Complete numeric domain / universal canonical byte agreement | BLOCKED | Requires explicit compatibility/domain decision and lossless implementation |
| Native parser / applicable validation / honest unsupported operations | PASS for corpus | Common fixtures, source round trips, native probes, support map |
| Loader containment and stated resource limits | PASS on Linux | 16 loader/resource cases, stable-directory assumption; no hostile race claim |
| Stable actionable errors and compatible representations | PASS for implemented scope | Official input/error reference; JS/TS additive details, Python ModelError attrs, native first error |
| Deterministic malformed inputs / parser memory checks | PASS | 137 ASan/UBSan inputs |
| CI configuration and reproducible dependency versions | PASS configuration only | Linux/Windows hardening matrix, Linux sanitizer, existing JS/schema jobs, pinned oracle versions |
| Hosted CI runs, Node 20 run, actual Windows filesystem proof | NOT_RUN | Local toolchain is Linux/Node 24; workflow definition is not a run |
| Official API/docs/support/evolution/newcomer path | PASS | Official refs plus `check_onboarding.py`; no new required ontology |
| Clean consumers | PASS | JS npm-pack test without tsc; installed Python wheel tested from /tmp |
| Stronger independent conformance claim | NOT_RUN | No independent implementation of every operation; shared algorithms/wrappers labeled |
| Source-independent third-product construction | NOT_RUN by design | Outside this run; authoring agent has read source |
| Full hardening mission complete | FAIL | Numeric mandatory gate outstanding; platform/hosted proof unavailable |

Clean Python proof used:

```sh
python3 -m pip wheel --no-cache-dir --no-build-isolation --no-deps --wheel-dir work/wheels bindings/python
python3 -m pip install --no-cache-dir --no-deps --target work/python-consumer-final work/wheels/foreverworks-0.1.0-py3-none-any.whl
```

From `/tmp`, set `PYTHONPATH` to that installed target and validate the minimal and
file-transfer models, trace the dependency to project intent, explain its classification,
and confirm replacement is partial. This passed without reading the Python source tree.
The wheel contains `contracts.json`; its observed SHA-256 was
`a91aa00960b529230595111dfff93cedaa1f8ad6dc7e4b88c3e8415af512fc7f` (not a reproducible-build claim).

## Exact continuation and next independent experiment

1. Resolve the numeric interface/domain incompatibility above explicitly. Add held-out
   precision, exponent and non-finite-range fixtures before implementation; keep 0.1
   examples and outputs, and test lossless unknown values and independently emitted bytes.
2. Execute the checked-in workflow on a disposable branch/PR. Inspect Linux, Windows
   symlink/real-target/UTF-8 behavior, Node 20 and sanitizer results. Fix failures rather
   than treating matrix configuration or Linux Windows-spelling tests as Windows proof.
3. Rerun the commands above, record the new finishing hash and measurements, and only
   then replace the failed/blocked/not-run mandatory gate statuses with actual evidence.

After hardening, conduct a **separate** experiment with two independently running small
products. Freeze checksummed documentation-only export packages containing purpose,
rationale, exact current wire formats, state ownership, errors, compatibility, recovery
and test examples. Do not disguise implementation code as documentation. Give a fresh
agent only those packages, declared public platform references, the broad objective and
explicitly allowed service/test access. Let that agent select the useful third product.

Keep original repositories and this source-aware conversation inaccessible. Record all
allowed access, package checksums, tool versions, interventions, missing knowledge and
failures. Independently operate both originals; use published contracts and held-out
interaction, data-preservation, authority and recovery cases to test real effects.
Do not invisibly coach missing facts. If separation or operating originals cannot be
established, mark the trial NOT_RUN. Successful core hardening alone proves neither
that documentation is sufficient nor that an Atlas/Redown companion has commercial demand.
