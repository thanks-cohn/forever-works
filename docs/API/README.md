# Forever Works API

This directory is the **official public API documentation home** for Forever Works.

Forever Works defines a transport-neutral semantic API. JavaScript, TypeScript, CLI/JSON, future MCP or HTTP adapters, and other bindings are implementations or transports of that contract; none of them defines the API by itself.

## Current API

The current API initiative is **Public API v0.1**.

During the Public API v0.1 implementation run, the authoritative reference will be created and maintained at:

- [PUBLIC_API_V0_1.md](PUBLIC_API_V0_1.md)

Until that reference is created, the design work lives in:

- [Public API v0.1 proposal](../public-api-v0.1/PROPOSAL.md)
- [Codex implementation request](../public-api-v0.1/CODEX_REQUEST.md)

## Documentation maintenance rule

Any change to public API semantics, operation names, inputs, outputs, errors, versioning, capability discovery, CLI mappings, or adapter obligations must update the relevant documentation in this directory in the same coherent change.

**Change the API, change `docs/API/`.**

Official API documentation must describe what is actually implemented and must distinguish stable behavior from experimental, deferred, or future work.
