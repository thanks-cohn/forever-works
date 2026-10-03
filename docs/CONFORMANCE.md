# Conformance

A conforming binding loads the shared fixtures, rejects structural and reference errors, tolerates unknown fields, rejects unsupported major versions, produces canonical normalization, implements lookup/list/trace, and implements conservative replacement and migration checks. `conformance/fixtures/cases.json` is the machine-readable case catalog and `conformance/expected` contains golden results. Bindings may expose different APIs but MUST produce semantically identical JSON results. Cycles terminate through a visited set.
