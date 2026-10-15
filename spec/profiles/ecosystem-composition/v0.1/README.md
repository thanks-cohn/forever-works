# Ecosystem composition profile 0.1

**Status:** experimental, optional implemented profile. **Identity:**
`https://forever.works/profiles/ecosystem-composition`, `profileVersion: "0.1"`.
The URI identifies the contract; readers need not fetch it. The self-contained
[Draft 2020-12 schema](composition.schema.json) is the interchange definition.
This profile specification, its schema and shared fixtures govern profile behavior;
reference code is subordinate. It does not change normative Forever Works
Standard 0.1, canonical record kinds, `foreverVersion`, or Public API v0.1.
This implementation is an experiment, not promotion to a normative standard.

## Adoption and authority

Keep the existing canonical manifest and accepted records. Store a separate UTF-8
JSON composition document; optionally point to it with this existing manifest
extension mechanism:

```json
{"extensions":{"forever.works.ecosystem-composition":{"profileVersion":"0.1","path":"composition.json"}}}
```

Do not add composition files to `manifest.records`. Legacy bindings ignore and
preserve the extension; they are not claimed to support profile semantics.
`loadOptionalComposition` only loads when the pointer is present. Explicit
`loadComposition` selects a document directly. Neither follows evidence files,
nested ecosystem references, remote URIs, nor commands. Nested references resolve
within this one document. The extension pointer has exactly `profileVersion` and
`path`; unsupported versions and unknown pointer fields are operational failures.

`intentRefs` refer to existing canonical intent IDs, not new authoritative intent.
`recordRefs`, capability references and requirement references contain exact
`{id, kind}` pairs. Requirements are intent, capability, invariant, constraint or
compatibility records; implementation and evidence are not requirements. Record
references are checked against an optional supplied canonical record array that
must first pass the Standard 0.1 model validator. Without this context, unresolved
records emit warnings and remain undetermined. A supplied missing/wrong-kind
record is an error. The CLI validates the canonical model before using it.

The document's provenance is a declaration, never independently authenticated by
validation. Imported, inferred, historical and agent-proposed descriptions do not
become accepted merely by loading or validating. The examples remain explicitly
agent-proposed and unreviewed. An `explicit`/`accepted` declaration also does not
constitute verifier proof of owner consent.

## Portable representation

Every document has `ecosystems`, `participants`, `contracts`, `interactions`,
`states`, `configurations`, `obligations`, and `evidence` arrays. Except ecosystems
and configurations, they may be empty. Thus an empty ecosystem, one component,
and arbitrary finite many-party arrangements are representable. No participant
role, implementation technology, operating system, language or transport enum
limits the abstract model.

| Entity | Meaning and references |
| --- | --- |
| Ecosystem | Collective canonical `intentRefs`, membership `participantRefs`, collective `obligationRefs`. Several ecosystems may share participants. |
| Participant | Arbitrary `roles`, canonical `recordRefs`, ports, optional `ecosystemRef` identifying a nested suite. |
| Port | Local stable `id`, `direction` (`in`, `out`, `inout`), explicitly provided and required canonical capabilities, contract references. |
| Interaction | Globally distinct ID, nonempty `from` and `to` endpoint arrays; each endpoint is an exact `{participant, port}` pair. Multiple edges, hyperedges and communication cycles are legal. |
| Contract | Typed `kind`, explanatory `statement`, canonical `requirementRefs`, optional opaque `parameters`. It explains a requirement; it is not a competing source of accepted intent. |
| State | One declared authoritative `owner`, explicit `authorizedWriters`, contract references. Shared services can have many writers without multiple contradictory owners. |
| Configuration | Explicit active participants, interactions, obligations and optional participant-keyed replaceable `bindings`. Alternate configurations can activate different subsets. |
| Obligation | Canonical requirements scoped to an ecosystem, participant, interaction or configuration; configuration applicability and evidence references. |
| Evidence claim | Obligation + exact configuration + canonical evidence record + relative artifact path + SHA-256 digest + accepted scope snapshot artifact + environment description + all active participant artifact digests + verifier identity + declared result. |

Profile IDs follow the canonical ID grammar and are unique across all top-level
entity arrays in the document. Port IDs are unique within their participant;
qualified endpoint references disambiguate repeated local IDs. Profile IDs and
canonical record references are separate typed namespaces. References never use
array offsets. Configuration bindings and participant `implementationBindings`
are opaque replaceable descriptions, excluded from permission and verification
reasoning. They do not define a participant's enduring identity.

Containment via ecosystem membership and `ecosystemRef` must be acyclic. Ordinary
interaction cycles are legal. A participant may belong to multiple ecosystems;
nesting does not inherit privileges. Configurations are explicit flat activation
sets: selecting a nested-suite participant does not silently activate its members.

Contracts distinguish `semantic`, `ordering`, `concurrency`, `retry`, `idempotency`,
`consistency`, `offline`, `failure`, `recovery`, `authority`, `data-access`, `state`,
and `version-compatibility`. Interactions recognize `command`, `event`, `query`,
`stream`, `replication`, `shared-state`, and `coordination`. These are descriptive
categories, not implemented runtime protocols or automatic behavioral checks.
Unknown categories remain round-trippable but produce `unsupported-semantics`
warnings. Nonempty policy parameters produce `parameters-uninterpreted`; this
version has no interpreter for ordering, timeout, reconciliation or retry policies.
Precise acceptance meaning remains in the referenced canonical requirements.

Every interaction declares `authority.inheritPrivileges: false` and an explicit
list of grants. Empty grants convey no permission. Grant recipients must be
endpoints; referenced states must be in the interaction's state scope. A `write`
grant must name the state's owner or a declared authorized writer. Both `read`
and `write` grants must explicitly name at least one state. Known
permission labels are `read`, `write`, `invoke`, `subscribe`; unknown permissions
are warnings, never newly granted authority. A declaration is not authentication,
consent, a sandbox or enforcement of the running products.

An active interaction requires every endpoint and referenced state owner to be
active in that configuration. Bindings cannot target inactive participants.
Obligations with nonempty `configurationRefs` apply only to those configurations;
an empty list allows applicability wherever their scope is active. The
configuration's `obligationRefs` selects its declared acceptance inventory. Listed
obligations must have active scopes and compatible applicability. Collective
obligations must be listed by their own ecosystem. Missing collective/interaction
obligations and omitted applicable configuration obligations are warnings, never
evidence of completeness.

## Verification and deterministic results

`validateComposition` returns `{valid, issues, verification}`. `valid` means the
implemented structural and reference checks passed, including known authority
contradictions. Warnings do not make structural validation fail. `issues` contain
stable `code`, JSON-pointer `path`, severity (`error`/`warning`), and explanatory
`message`. Sort by path, then code, then message. Consumers should key on codes,
not message wording. Structural failures stop semantic traversal.

**`verification.status` and every obligation status are always `UNKNOWN` in this
reference implementation.** Even a declared `PASS`, a well-formed digest, an
existing component test record, or all participant builds passing cannot verify a
suite. Claims marked `FAIL`, `UNKNOWN` or `NOT_RUN` are also unauthenticated claims,
not executed outcomes. They remain preserved in the document. Missing evidence
is unknown; a dangling evidence ID is a reference error. Evidence must be linked
back by its obligation, selected by the configuration, and bind all active
participant artifacts (or identity/role attestations for non-software actors).
`scopeArtifact` is a second safe relative path/digest pair for an immutable accepted
snapshot of canonical requirements, the composition contract and selected
configuration; `environment` records the claimed execution context without an OS
or runtime enum. These are still unauthenticated declarations. Independent
verification must compare that snapshot to the selected live contract, rather
than trusting an obligation ID that might later refer to changed meaning.
A component's proof cannot be silently relabeled as
suite-level success.

Independent acceptance must verify canonical intent acceptance, actual artifact
bytes and digests, participant versions, exact configuration and environment,
interaction effects, authority enforcement, state and recovery behavior, and the
verifier's independence/identity. This validator does **not** do those operations.
It never runs evidence commands or reads artifact paths. No callback can turn its
static result into `PASS`. A future authenticated evaluator needs a separately
versioned contract and held-out runtime evidence.

Normalization sorts object keys lexically by Unicode scalar value, preserves all
array ordering and opaque data, indents two spaces, and appends one newline.
Arrays are significant, including declaration order; callers must not use this
normalizer to reorder accepted intent. It is deterministic serialization, not an
artifact signature or authentication protocol. JSON number serialization follows
the reference host's JSON representation; interoperable signatures require a
separately specified canonicalization scheme.

Safe reference paths use `/`-separated relative components; no empty, `.` or `..`
segments, backslash, colon, percent escapes, query/fragment marker or ASCII control
characters are allowed. The filesystem adapter also rejects resolved symlink
escapes. It assumes a trusted, non-concurrently-mutating checkout; it is not a
filesystem security boundary. The reference loader bounds files to 4 MiB and
requires valid UTF-8; core traversal bounds inputs to 100,000 values and nesting
depth 64. These are reported implementation limits, not an abstract participant
count or platform constraint.

## Run the proof

From the repository root, using plain JavaScript and no TypeScript compiler:

```sh
node --test packages/javascript/test/ecosystem-composition.test.js
node scripts/validate_composition.mjs conformance/ecosystem-composition/v0.1 valid/four-participant-fan.json conformance/fixtures/complete/forever
```

CLI exit codes are 0 (structurally valid, possibly warnings/unknown), 1 (validation
errors), and 2 (load, input, canonical-model or argument failure). Results/errors
are one JSON document on stdout. See the [experimental adapter contract](../../../../docs/API/ECOSYSTEM_COMPOSITION_PROFILE_V0_1.md).

Independent schema proof, separate from the reference validator:

```sh
python3 -m pip install -r scripts/requirements-schema.txt
python3 scripts/check_ecosystem_schema.py
```

This development-only oracle is replaceable by any conforming Draft 2020-12
implementation. It validates the schema and each catalog entry's `schemaValid`
expectation, not reference integrity or runtime behavior. The JavaScript suite
checks full `valid`, error codes and conservative verification. Python, C, C++ and
TypeScript bindings retain their existing model support; this is one JavaScript
profile proof binding, not cross-language profile semantic conformance.

## Examples and evolution

[Shared fixtures](../../../../conformance/ecosystem-composition/v0.1/cases.json)
include zero/one components, a four-party collector/helper/client/shared-service
fan-in/out, multiedges, cycles, many-to-many replication, a structurally different
person/instrument/library nested ecosystem, and alternate deployments.
`implementationBindings.exampleForm` illustrates browser-extension, helper,
mobile-client and shared-service forms without putting them in an abstract enum.
The examples reuse existing canonical remote-transfer fixture records; they are
synthetic structural examples, not real independently working product suites.

Only profile 0.1 is implemented. Unknown versions fail explicitly; this does not
change Standard 0.1's model minor-version rules. Core profile objects are strict:
unknown fields fail, so typos cannot become implied authority. Forward research
belongs in owner-qualified `extensions` keys using the canonical dotted-key
namespace grammar. Extensions are preserved, warn as unsupported, and cannot
confer authority, supported behavior or proof. No migrations have been invented or
executed. Future versions must publish explicit transformations, retain these
fixtures, preserve provenance and obtain review for changed obligations.

No new Public API v0.1 operations are advertised. Profile query discovery and a
second independent semantic binding are deferred until the contract is exercised
against actual interacting systems.
