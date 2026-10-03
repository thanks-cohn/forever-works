# Forever Works

**A language-neutral longevity standard for software in the agentic era.**

Forever Works lets a project carry durable, machine-readable intent, capabilities, invariants, constraints, implementation rationale, replacement requirements, and migration evidence. It preserves purpose rather than obsolete machinery.

## End-to-end proof

The canonical product is [`docs/STANDARD.md`](docs/STANDARD.md), the JSON Schemas in `spec/schemas`, and shared conformance behavior. TypeScript, C, Python, and the C++ wrapper are proof bindings—not the definition.

```sh
npm install
make test
packages/cli/bin/forever --root examples/file-transfer/forever validate
packages/cli/bin/forever --root examples/file-transfer/forever explain dependency.old-streamer --json
packages/cli/bin/forever --root examples/file-transfer/forever evaluate-replacement dependency.old-streamer implementation.wasm-streamer
packages/cli/bin/forever --root examples/file-transfer/forever verify-migration migration.old-to-wasm
```

The replacement proof passes streaming, resumability, portability, and configuration compatibility while reporting bounded memory as **unknown** until benchmark evidence exists. The migration remains partial for the same reason. This is intentional: absent evidence is never success.

## Layout

* `spec/` — canonical schemas, examples, and evolution policy.
* `docs/` — normative standard and focused explanatory documents.
* `packages/typescript/` and `packages/cli/` — ESM/JavaScript runtime and portable CLI adapter.
* `bindings/` — C11, dependency-free Python, and C++ bindings.
* `conformance/` — shared valid, invalid, evolution, cycle, replacement, and migration fixtures plus goldens.
* `examples/file-transfer/` — complete intent-to-migration proof.
* `forever/` — the project describing itself.

Read the [foundational proposal](docs/FOUNDATIONAL_PROPOSAL.md), [standard](docs/STANDARD.md), and [conformance contract](docs/CONFORMANCE.md) before changing semantics.
