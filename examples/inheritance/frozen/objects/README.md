# Objects 1: durable immutable content identities

Purpose: independently persist small binary assets and their opaque metadata under
stable identities. Catalogs may refer to an object ID but cannot write/read this store
without a separate grant. Non-goals: mutable asset replacement, UI, public publication,
real account management or cross-service transactions.

[Exact contract](CONTRACT.md) · [Examples](examples.json) ·
[Machine-readable intent](forever/manifest.json).

Architecture: a separate local HTTP process and SQLite database, with write-once identity
and SHA-256 observations. Shared reference runtime code is an implementation convenience,
not independent semantic proof of the two products. Processes and state are independent;
restart, grants and failures are exercised separately. SQLite and Base64/JSON were chosen
for a small auditable example; the mechanisms can change if exact public behavior holds.

Limitations: public synthetic fixture grants, no TLS/production authentication, small
payloads, no garbage collection or atomic catalog+object commit. Run only in an isolated
test network. An upload may commit before a response is lost; retry/read by identity.

Provenance: source-aware producer tests only, no cold construction success. Allowed
references/dependencies: Python standard library, HTTP/JSON/Base64 specifications and
bundled core schemas/models. Do not inspect original implementation source in a fresh
consumer trial. Package/model validation is integrity/structure evidence, not sufficiency.
