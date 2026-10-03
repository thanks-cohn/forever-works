# Language bindings

A binding needs only to read/write canonical JSON, represent records and ID references, validate required semantics, and expose the query contract. Native bindings, C FFI, a CLI subprocess, direct JSON processing, and external adapters are all valid—including for COBOL, Pascal, Fortran, Lisp, or languages not yet created. TypeScript, C, Python, and C++ prove portability; none defines the standard. C++ wraps C because this minimizes duplicate parsing semantics while providing RAII and idiomatic exceptions.
