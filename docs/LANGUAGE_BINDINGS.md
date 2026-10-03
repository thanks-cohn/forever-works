# Language bindings

A binding needs only to read/write canonical JSON, represent records and ID references, validate required semantics, and expose the query contract. Native bindings, C FFI, a CLI subprocess, direct JSON processing, and external adapters are all valid—including for COBOL, Pascal, Fortran, Lisp, or languages not yet created.

## First-class proof targets

JavaScript, TypeScript, C, Python, and C++ are proof targets; none defines the standard.

**JavaScript is a first-class target in its own right.** It is not considered conformant merely because TypeScript compiles to JavaScript. The project requires independent plain-JavaScript consumption, tests, examples, and conformance evidence. A consuming JavaScript project must not need a TypeScript compiler.

**TypeScript** provides a typed proof binding and TypeScript-oriented ergonomics. Its static types are conveniences layered over the canonical language-neutral model, not normative semantics.

**C** provides a low-level portability stress test. **Python** provides an independent high-level dynamic-language proof. **C++** wraps C where appropriate because that minimizes duplicate parsing semantics while providing RAII and idiomatic exceptions.

All bindings are subordinate to the normative specification, schemas, and shared conformance contract.
