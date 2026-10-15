# Forever Works

**A language-neutral longevity standard for software in the agentic era.**

Forever Works lets a project carry durable, machine-readable intent, capabilities, invariants, constraints, implementation rationale, replacement requirements, and migration evidence. It preserves purpose rather than obsolete machinery.

## Five-minute start

Create a deliberately draft model, then validate and audit it before replacing the TODO values with accepted project intent:

```sh
packages/cli/bin/forever init
packages/cli/bin/forever --root forever validate
packages/cli/bin/forever --root forever audit
```

For an existing complete example:

```sh
packages/cli/bin/forever --root examples/file-transfer/forever explain dependency.old-streamer --json
```

The initializer labels placeholders as unreviewed drafts; generated text is not accepted architectural truth. See the [official Public API v0.1 reference](docs/API/PUBLIC_API_V0_1.md) for stable operations and adapter status.

### JavaScript

```js
import {createForeverApi} from "@forever-works/javascript";

const forever = await createForeverApi("./forever");
console.log(forever.describe());
console.log(forever.getProjectIntent());
```

This package is dependency-free plain ESM and does not require a TypeScript compiler.

## End-to-end proof

The canonical product is [`docs/STANDARD.md`](docs/STANDARD.md), the JSON Schemas in `spec/schemas`, and shared conformance behavior. JavaScript, TypeScript, C, Python, and the C++ wrapper are separate proof bindings—not the definition. The dependency-free JavaScript package is authored and tested as plain ESM; its evidence does not depend on compiling TypeScript.

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
* `packages/javascript/` — independently authored, dependency-free plain JavaScript proof binding.
* `packages/typescript/` and `packages/cli/` — typed binding and portable CLI adapter.
* `bindings/` — C11, dependency-free Python, and C++ bindings.
* `conformance/` — shared valid, invalid, evolution, cycle, replacement, and migration fixtures plus goldens.
* `examples/file-transfer/` and `examples/javascript/` — complete intent-to-migration proofs.
* `forever/` — the project describing itself.

Read the [foundational proposal](docs/FOUNDATIONAL_PROPOSAL.md), [standard](docs/STANDARD.md), and [conformance contract](docs/CONFORMANCE.md) before changing semantics.

## Research proposal: Selective Reconstitution

[Selective Reconstitution — Capability Recovery from Entangled Software](docs/PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md) proposes extracting owner-selected working capabilities from legacy programs, documenting both their framework-neutral semantics and real intermeshed dependency mechanisms, and rebuilding only the selected behavior with independent cold-agent acceptance evidence. This is a **non-normative research proposal**, not an implemented command or a change to Standard 0.1.

## Long-horizon mission and flagship research

**Forever Works aims to be an independent software-continuity standard.** The owner's long-term vision is an ecosystem of approximately **50 inheritable browser applications**, so unfamiliar future agents can upgrade, renew, reform, recover and reconstruct them for new languages, browsers, desktop environments and mediums, with independent verification of behavior, state and real effects. This is a research ambition, not a claim of present universal support.

- [Long-Horizon Vision — The Inheritable Software Ecosystem](docs/VISION/INHERITABLE_SOFTWARE_ECOSYSTEM.md): the enduring standard, inheritance packages and cold-agent acceptance.
- [50-App Inheritance, SUBSTRATE Mini and Any-Shape Research Program](docs/RESEARCH/FIFTY_APP_INHERITANCE_AND_ANY_SHAPE.md): concrete, linked flagship experiments.
- [Selective Reconstitution — Capability Recovery from Entangled Software](docs/PROPOSALS/SELECTIVE_RECONSTITUTION_CAPABILITY_EXTRACTION.md): research on documenting, disentangling and rebuilding selected legacy capabilities.

## Research proposal: composable software ecosystems

[Composable Software Ecosystems](docs/PROPOSALS/COMPOSABLE_SOFTWARE_ECOSYSTEM_CONTRACT.md) proposes an agent-, runtime-, and language-neutral contract for arbitrary multi-participant suites, interaction graphs, changing deployments, cross-product authority and end-to-end evidence. This is **non-normative**; current Standard 0.1 and Public API v0.1 are unchanged.

## Research: contractual fixity and implementation fluidity

[Linux ABI inheritance and cross-language reconstitution](docs/PROPOSALS/CONTRACTUAL_FIXITY_IMPLEMENTATION_FLUIDITY_LINUX_ABI.md) records the general principle of preserving scoped external invariants while permitting internal mechanisms, languages and architectures to evolve. It includes evidence boundaries from the experimental Zig Morphic/Alpz project, a compatibility-envelope proposal, cold-agent reconstruction protocol, and caveats. This is non-normative research, not a declaration of complete Linux ABI compatibility.

## Optional ecosystem composition profile

The experimental [ecosystem composition profile 0.1](spec/profiles/ecosystem-composition/v0.1/README.md)
now has a standalone JSON Schema, dependency-free JavaScript loader/validator,
and shared valid/invalid fixtures for arbitrary participant graphs, nested suites,
authority/state declarations and alternate configurations. Canonical Standard 0.1
and Public API v0.1 remain unchanged. Static validation always reports runtime
verification as **UNKNOWN**, even when evidence metadata claims PASS.

```sh
node scripts/validate_composition.mjs conformance/ecosystem-composition/v0.1 valid/four-participant-fan.json conformance/fixtures/complete/forever
```
