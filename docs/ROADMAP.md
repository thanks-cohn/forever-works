# Roadmap

The v0.1 foundation includes schemas, shared conformance data, TypeScript/C/Python bindings, CLI, replacement and migration proofs, self-description, and a C++ wrapper.

The next priority is to make **plain JavaScript an explicit first-class proof target** with an independently usable package/runtime surface, dedicated tests, a plain-JavaScript example, independent conformance against shared fixtures and goldens, packaging/consumer smoke tests, a CI lane, and self-hosted architectural records. JavaScript conformance must not be inferred from TypeScript compilation or tests.

After that foundation is proven, expand schema vocabulary only from demonstrated needs, add independent validators, harden resource limits/security, and standardize protocol adapters without making them canonical.
