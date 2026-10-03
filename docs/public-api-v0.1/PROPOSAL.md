# Forever Works Public API v0.1 and Early-Adopter Readiness

**Status:** Implementation proposal  
**Initiative:** Public API v0.1  
**Primary goal:** Turn the existing Forever Works foundation into a stable, publicly consumable platform without weakening the language-neutral standard.

## 1. Why this is the next step

Forever Works already has a working semantic foundation:

- a normative standard,
- canonical JSON schemas,
- conformance fixtures and golden outputs,
- JavaScript, TypeScript, Python, C, and C++ proof implementations,
- a CLI,
- replacement and migration evaluation,
- self-hosted Forever Works records,
- and a transport-independent agent query concept.

The next major risk is not lack of features. It is fragmentation.

If each language binding, CLI, future MCP server, HTTP adapter, or agent integration grows its own method names, output shapes, errors, and semantics, Forever Works will gradually become a family of similar tools instead of one durable standard.

The next phase should therefore formalize a **Forever Works Public API v0.1**: one stable semantic interface that can be exposed through many transports and languages without changing what Forever Works means.

The governing principle is:

> **Standardize semantics before transports.**

HTTP is not the API. MCP is not the API. JavaScript is not the API. The CLI is not the API.

They are adapters to the same semantic contract.

## 2. Relationship to the long-term vision

This initiative directly supports the project's autonomous-inheritance design goal:

> **A sufficiently capable agent should be able to inherit the repository cold, understand it, repair it, modernize it, verify the repair, and leave it in a better documented state without needing the original developers.**

A cold agent should not need private knowledge of a particular Forever Works implementation. It should be able to discover the API version, discover supported capabilities, ask stable questions, receive predictable structured results, and reason from those results.

The public API becomes the durable interrogation surface between a repository and the intelligence maintaining it.

## 3. API philosophy

The Forever Works Public API should be:

- transport-neutral,
- language-neutral,
- versioned,
- discoverable,
- deterministic where the standard requires determinism,
- conservative about missing evidence,
- compatible with plain JSON,
- friendly to both humans and agents,
- small enough to preserve,
- and subordinate to the normative standard.

The API must not expose implementation details merely because a current binding makes them convenient.

A public operation belongs in the API only when it corresponds to a durable Forever Works concept.

## 3.1 Official API documentation home

The permanent public documentation for the Forever Works API should live under:

`docs/API/`

This directory is the official human- and agent-readable API documentation surface. Planning notes, implementation requests, and handoffs may live elsewhere, but a released or changed public API must be reflected in `docs/API/`.

The initial structure should include:

- `docs/API/README.md` — API index, current version, compatibility/status guidance, and links.
- `docs/API/PUBLIC_API_V0_1.md` — Public API v0.1 contract and reference.

Any future change to public API semantics, operations, errors, versioning, or adapter obligations should update the relevant official API documentation in the same change.

## 4. Proposed Public API v0.1 surface

The first API should remain intentionally compact.

### Discovery

- `describe()`
- `getProjectIntent()`

`describe()` should allow an unfamiliar client to determine at least:

- Forever Works API version,
- supported model version or versions,
- implemented API capabilities,
- implementation/binding identity where useful,
- optional adapter profile information.

An agent should be able to interrogate capabilities rather than rely on assumptions.

### Core model queries

- `getEntity(id)`
- `listCapabilities()`
- `listInvariants()`
- `listDependencies()`
- `listImplementations()`
- `traceEntity(id)`
- `explainDependency(id)`

Additional list operations may be exposed through a generic `list(kind)` internally, but the stable public API should favor durable domain concepts rather than convenience leakage.

### Validation and health

- `validateModel()`
- `audit()`

Validation answers whether the model violates the standard.

Audit answers where important architectural knowledge, provenance, evidence, implementation linkage, or verification is weak or incomplete.

These must remain distinct concepts.

### Modernization and verification

- `evaluateReplacement(dependencyId, candidateImplementationId)`
- `verifyMigration(migrationId)`

These operations are strategically important and should have strong conformance coverage.

The existing conservative rule remains fundamental:

> **Missing evidence is unknown, never success.**

### Canonicalization

- `normalize()`

Normalization should produce canonical output according to the Forever Works standard and should not vary by adapter.

## 5. Stable result and error semantics

The API specification should define:

- success shape,
- not-found behavior,
- validation-error behavior,
- malformed-input behavior,
- unsupported-version behavior,
- unsupported-operation behavior,
- deterministic ordering where required,
- stable machine-readable error codes,
- and how human-readable diagnostic messages accompany those codes.

The API should avoid requiring clients to parse prose.

Where reasonable, API results should remain plain JSON values that can survive transport through a CLI subprocess, FFI boundary, HTTP response, MCP call, or future mechanism.

## 6. JavaScript as the strongest first façade

JavaScript is now a first-class proof target and is a good place to establish the public façade.

The JavaScript package should expose a stable high-level entry point such as:

```js
import { createForeverApi } from "@forever-works/javascript";

const forever = await createForeverApi("./forever");

const description = await forever.describe();
const health = await forever.audit();
const dependency = await forever.explainDependency("dependency.old-streamer");

const result = await forever.evaluateReplacement(
  "dependency.old-streamer",
  "implementation.wasm-streamer"
);
```

The exact final names should be chosen carefully during implementation, but the key architectural rule is that the façade must sit **above** the current internal `Model` shape.

The public API should not accidentally become a permanent promise about internal classes.

## 7. TypeScript parity

TypeScript should implement the same semantic contract without becoming authoritative.

The current TypeScript implementation trails the newer JavaScript implementation in some areas. This initiative should close important parity gaps where practical, especially around:

- auditing,
- migration verification,
- classification validation,
- public API discovery,
- stable errors,
- and output parity.

JavaScript and TypeScript remain independent proof targets.

## 8. CLI as the lowest-common-denominator adapter

The CLI should become an explicit adapter to the same API contract.

For example:

```text
forever validate
        ↓
validateModel()

forever audit
        ↓
audit()

forever explain dependency.foo
        ↓
explainDependency("dependency.foo")

forever evaluate-replacement dependency.foo implementation.bar
        ↓
evaluateReplacement("dependency.foo", "implementation.bar")
```

Structured CLI output should match the public API's semantic shapes closely enough that a language with no native binding can still consume Forever Works reliably through subprocess + JSON.

This is one of the project's most important longevity properties.

## 9. API conformance

The API should receive its own conformance layer.

A fixture should be able to express:

```text
Given model X
Call operation Y with arguments Z
Expect semantic result R
```

The same fixtures should be consumable by:

- JavaScript,
- TypeScript,
- CLI/JSON,
- Python where practical,
- and future bindings/adapters.

The purpose is not to force identical internal APIs in every language. The purpose is to prove identical Forever Works semantics.

Conformance should include:

- discovery,
- entity lookup,
- listing/order,
- trace,
- dependency explanation,
- validation,
- audit,
- replacement evaluation,
- migration verification,
- normalization,
- not-found behavior,
- malformed input,
- unsupported version,
- and stable error codes.

## 10. Do not build REST or MCP yet

This run should not spend its limited implementation window on an HTTP service or MCP server.

Those should become thin adapters after the semantic API is stable.

The intended architecture is:

```text
                   Forever Works
                  Public API v0.1
                        │
       ┌────────────────┼────────────────┐
       │                │                │
  JavaScript          CLI/JSON       TypeScript
       │                │                │
       └────────────────┼────────────────┘
                        │
                  conformance
                        │
        ┌───────────────┼───────────────┐
        │               │               │
       MCP             HTTP          future adapter
```

Standardizing a network transport too early would create unnecessary coupling.

## 11. Five-minute newcomer experience

A person who has never spoken to the project authors should be able to understand and exercise Forever Works quickly.

The README should lead toward a concise path such as:

```sh
forever init
forever validate
forever audit
forever explain dependency.example
```

The first experience should answer:

- What is Forever Works?
- Why would I use it?
- What files does it add?
- What does it know?
- What does it refuse to assume?
- How do I inspect a dependency?
- How do I evaluate a replacement?
- How do I verify a migration?
- How do I integrate it with an agent?

A newcomer should not need to read the full foundational proposal before seeing value.

## 12. Harden `forever init`

The current initializer is a foundation, not the eventual discovery system.

For this phase, it should be:

- predictable,
- safe,
- explicit about draft/TODO content,
- careful never to fabricate accepted architectural facts,
- clear about what files were created,
- and immediately usable with `validate` and `audit`.

Intelligent repository discovery can come later.

The path should remain:

```text
forever init
    ↓
safe starter model
    ↓
future: repository discovery
    ↓
draft/inferred knowledge
    ↓
explicit review
```

## 13. Public-release consistency audit

Before encouraging outside use, eliminate avoidable ambiguity.

Audit and correct where appropriate:

- root license versus package license metadata,
- package names,
- package versions,
- Node/runtime requirements,
- exports,
- README installation commands,
- CLI naming,
- API terminology,
- standard/model/API version terminology,
- schema links,
- examples,
- command exit behavior,
- structured error output,
- and claims about what is currently implemented.

In particular, the current repository root license and the JavaScript package's declared license must be made consistent.

Do not silently choose a new project license without preserving the repository's existing licensing intent. Align package metadata with the repository license unless the repository explicitly establishes otherwise.

## 14. Self-hosting

Forever Works should record the Public API decision in its own `forever/` model.

Future agents should be able to discover that:

- the public API is semantic and transport-neutral,
- specification and conformance remain authoritative,
- adapters must not redefine semantics,
- capability discovery is important for cold inheritance,
- CLI/JSON is a lowest-common-denominator adapter,
- and REST/MCP are intentionally non-canonical transports.

## 15. What this initiative should not do

Do not:

- introduce a giant ontology,
- add speculative record kinds without demonstrated need,
- make JavaScript authoritative,
- make TypeScript authoritative,
- make the CLI authoritative,
- make HTTP authoritative,
- make MCP authoritative,
- redesign the canonical model gratuitously,
- weaken pass/fail/unknown semantics,
- weaken provenance rules,
- remove existing cross-language proof work,
- or claim public maturity beyond what tests support.

## 16. Desired state after this initiative

The desired shape is:

```text
                 FOREVER WORKS 0.1

              normative specification
                       │
              public semantic API
                       │
       ┌───────────────┼───────────────┐
       │               │               │
 JavaScript API      CLI/JSON       TypeScript
       │               │               │
       └───────────────┼───────────────┘
                       │
                 API conformance
                       │
       Python / C / C++ portability proofs
                       │
                self-hosted model
                       │
              newcomer documentation
```

At this point, Forever Works should be honestly describable as:

> **Early, but usable.**

## 17. Acceptance philosophy

The run should optimize for a small coherent public contract rather than a large incomplete one.

A good v0.1 API is one whose semantics can plausibly survive future implementation rewrites.

Every proposed operation should pass this test:

> Would this operation still make sense if today's JavaScript, CLI implementation, package layout, and agent ecosystem disappeared?

If yes, it is a candidate for the durable API.

If no, it probably belongs in an adapter or implementation-specific layer.

## 18. North star

The Public API should make Forever Works legible to an unfamiliar future intelligence.

The repository should not need to know which agent will inherit it.

The agent should need only:

1. the Forever Works standard,
2. the repository,
3. and an implementation or adapter that conforms to the public semantic API.

That is a direct step toward a self-renewing software ecosystem in which implementation decay is expected, architectural meaning is preserved, and sufficiently capable agents can continuously repair what time breaks.
