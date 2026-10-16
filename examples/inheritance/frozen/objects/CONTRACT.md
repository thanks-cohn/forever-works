# Objects HTTP/JSON contract, version 1

UTF-8 JSON with exact bounded decimals (bundled LOSSLESS_JSON.md), scalar Unicode and
no duplicate members. Body <=131072 bytes, decoded content <=65536 bytes. Identifiers
match `[a-z][a-z0-9-]{0,63}`. Unknown fields are preserved and inert.

- GET `/health`: public `{service:"objects",version:"1"}`.
- GET `/objects`: authorized `{ids:[...]}`, lexically sorted.
- GET `/objects/{id}`: exact stored JSON bytes, ETag `"1"`, X-Content-SHA256 of decoded
  bytes. Stable identity includes both content and metadata document, not location.
- PUT `/objects/{id}`: JSON requires matching string id and strict standard Base64
  string contentBase64 (no whitespace/URL alphabet). Optional metadata/unknown fields
  are preserved in original bytes. No If-Match is required.

Test-only grants: Authorization `Bearer objects-read` for reads and `Bearer objects-write`
for reads/writes. Catalog grants confer no access. Missing/unknown grant: 401 unauthorized;
read-only write: 403 forbidden. Metadata, confidence or PASS assertions confer none.

Create returns 201 `{id,revision:1}`, ETag `"1"` and X-Content-SHA256. Byte-identical
retry returns 200 with unchanged revision/digest. Any different document for an existing
identity returns 409 identity-conflict, without modifying content or metadata, even if
new JSON decodes to the same bytes. Use a distinct identity for intentional replacement.
A lost response is UNKNOWN; retry identical bytes/read by identity, never invent success.

Errors `{error:{code}}`: 400 invalid-document or incomplete-body; 401 unauthorized;
403 forbidden; 404 not-found; 409 identity-conflict; 413 body-limit or content-limit;
503 store-busy. Unknown reads: 404. Retry 503 after bounded backoff. Restart preserves
committed state. No DELETE, fetch-by-URI, publication, transaction coordinator, upload
resumption or production entitlements. A partially completed catalog+store workflow
may leave an unreferenced object; consumers must disclose/recover according to their own
published workflow rather than silently delete or assume atomic rollback.

Version 1 never reinterprets identifiers or drops stored fields. Incompatible formats,
state ownership or error changes require a new contract and explicit migration path.

A harness may replace the default synthetic grant strings with opaque synthetic values
for the same roles. Only the explicitly supplied grant may be used for an operation;
never guess another role's default grant or derive authority from a document. The
wire authorization scheme stays Bearer. Test grants are not real credentials.

PUT requires a numeric Content-Length; chunked request bodies are unsupported. Missing,
negative or oversized length returns 413 body-limit; malformed length returns 400
invalid-document. An incomplete body/5-second read timeout returns 400 incomplete-body.
No Content-Type request header is required; the actual body must be valid UTF-8 JSON.
Base64 must be canonical RFC 4648 standard encoding, including padding and unused bits.
