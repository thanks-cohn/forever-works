# Roadmap

The v0.1 foundation includes schemas, shared conformance data, TypeScript/C/Python bindings, CLI, replacement and migration proofs, self-description, and a C++ wrapper.

Plain JavaScript now has an independently authored package/runtime surface, dedicated tests, a plain-JavaScript example, independent conformance against shared fixtures and goldens, a packaging/consumer smoke test, a CI lane, and a self-hosted architectural decision. JavaScript conformance is not inferred from TypeScript compilation or tests.

After that foundation is proven, expand schema vocabulary only from demonstrated needs, add independent validators, harden resource limits/security, and standardize protocol adapters without making them canonical.
