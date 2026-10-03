# Language bindings

A binding needs only to read/write canonical JSON, represent records and ID references, validate required semantics, and expose the query contract. Native bindings, C FFI, a CLI subprocess, direct JSON processing, and external adapters are all valid—including for COBOL, Pascal, Fortran, Lisp, or languages not yet created.

## First-class proof targets

JavaScript, TypeScript, C, Python, and C++ are proof targets; none defines the standard.

**JavaScript is a first-class target in its own right.** It is not considered conformant merely because TypeScript compiles to JavaScript. The project requires independent plain-JavaScript consumption, tests, examples, and conformance evidence. A consuming JavaScript project must not need a TypeScript compiler.

### JavaScript proof binding

`packages/javascript` is dependency-free ESM authored as `.js`. Its `Model` class is the host-neutral semantic core for already-parsed JSON; the Node adapter adds safe filesystem loading through `loadModel`. Public operations cover validation, entity lookup and sorted lists, cycle-safe bidirectional tracing, dependency explanation and classification queries, audits, deterministic normalization, replacement evaluation, and migration verification. Unknown JSON fields remain on records and survive normalization.

`make test-javascript` runs direct unit and shared conformance tests plus a clean temporary consumer that installs an `npm pack` artifact. None of these steps invokes the TypeScript compiler. `examples/javascript` demonstrates the intent-to-migration chain using only JavaScript.

**TypeScript** provides a typed proof binding and TypeScript-oriented ergonomics. Its static types are conveniences layered over the canonical language-neutral model, not normative semantics.

**C** provides a low-level portability stress test. **Python** provides an independent high-level dynamic-language proof. **C++** wraps C where appropriate because that minimizes duplicate parsing semantics while providing RAII and idiomatic exceptions.

All bindings are subordinate to the normative specification, schemas, and shared conformance contract.
