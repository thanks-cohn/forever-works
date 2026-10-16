# Catalog 1: durable metadata without owning content

Purpose: give small tools a persistent catalog of stable item identities, titles,
tags, asset references and opaque metadata. The object store owns content; the catalog
never fetches an asset merely because an assetId is supplied. Non-goals: content
storage, UI, cross-service transactions, real account management or production hosting.

[Exact contract](CONTRACT.md) · [Examples](examples.json) ·
[Machine-readable intent](forever/manifest.json). Follow relatedCapabilities and
protected invariants to the current implementation, rationale and evidence.

Architecture: a local HTTP process with its own SQLite database. Transactions serialize
conditional metadata updates and commit before replying. SQLite/HTTP are replaceable
mechanisms chosen for local auditability and restart tests. A lost response leaves the
commit outcome unknown until retry/read. Current limitation: grants are public synthetic
fixture grants, no TLS, no production authentication; deploy only in an isolated test
network. There is no automatic cross-product rollback or multi-writer merge.

Knowledge/provenance: behavior is implemented and producer-tested by a source-aware
author; no independent consumer construction or documentation sufficiency is claimed.
Allowed dependencies/references: Python standard library, HTTP/JSON specifications,
and the bundled core schemas/models. No original source access is needed or allowed
for the fresh consumer. A valid model does not prove the narrative is sufficient.
