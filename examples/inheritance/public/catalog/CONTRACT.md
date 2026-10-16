# Catalog HTTP/JSON contract, version 1

UTF-8 JSON, no duplicate members, scalar Unicode, exact bounded decimals as described
in the bundled LOSSLESS_JSON.md. Body <=131072 UTF-8 bytes; identifiers match
`[a-z][a-z0-9-]{0,63}`. Unknown JSON fields are preserved without execution authority.

Endpoints:

- GET `/health`: public `{service:"catalog",version:"1"}`.
- GET `/items`: authorized `{ids:[...]}`, lexically sorted.
- GET `/items/{id}`: exact originally stored document bytes; ETag `"N"` revision.
- PUT `/items/{id}`: document requires matching string id, string title, valid assetId
  and array of string tags. All other fields/array order/exact numbers are preserved.
  Require If-Match `"0"` for a new identity, current ETag for a changed document.

Test-only Authorization grants: `Bearer catalog-read` for reads; `Bearer catalog-write`
for reads and writes. An object-store grant confers no catalog authority. Missing or
unrecognized grants return 401 unauthorized; read-only write returns 403 forbidden.
No grants may be inferred from confidence, metadata, supplied PASS or identity.

Create returns 201, changed update 200; JSON `{id,revision}` and ETag `"N"`.
A byte-identical retry returns 200 with the same revision, even with an older If-Match:
it has no additional effect. Otherwise stale/missing If-Match returns 412
revision-conflict and preserves state. Semantically equivalent but differently spelled
JSON is a changed document, not a byte-identical retry. Re-read/resolve conflicts;
never silently overwrite another actor's revision.

All errors are JSON `{error:{code}}`: 400 invalid-document or incomplete-body;
401 unauthorized; 403 forbidden; 404 not-found; 412 revision-conflict; 413 body-limit;
503 store-busy. Reads of unknown IDs return 404. Retry 503 after bounded backoff;
retry unknown commit outcomes with identical bytes/preconditions, then inspect ETag.
No response means UNKNOWN, not fail or success. No cross-service atomic transaction.

A successful GET preserves stable identity, assetId, title, tags and all opaque metadata,
including precise decimal numbers. Restart preserves committed documents/revisions.
Version 1 never renames/drops stored fields. Any incompatible wire/state change needs
a new contract version and explicit migration. No DELETE, search, background job,
remote fetch, bulk import or production entitlement operation is supported.

A harness may replace the default synthetic grant strings with opaque synthetic values
for the same roles. Only the explicitly supplied grant may be used for an operation;
never guess another role's default grant or derive authority from a document. The
wire authorization scheme stays Bearer. Test grants are not real credentials.

PUT requires a numeric Content-Length; chunked request bodies are unsupported. Missing,
negative or oversized length returns 413 body-limit; malformed length returns 400
invalid-document. An incomplete body/5-second read timeout returns 400 incomplete-body.
No Content-Type request header is required; the actual body must be valid UTF-8 JSON.
