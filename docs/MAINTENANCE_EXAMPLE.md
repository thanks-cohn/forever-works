# A concrete maintenance change

The owner requested lossless unknown numeric metadata while retaining small, neutral
core contracts and old consumers. A reproducible legacy input rounded
`9007199254740993` to `9007199254740992`. That is a bug in a preservation workflow,
not accepted intent to discard data.

Trace this change in the self-model:

- `capability.lossless-interchange` states the useful outcome and links the existing
  backward-awareness/readable-format invariants.
- `decision.lossless-interchange` records why an additive interface was chosen over
  narrowing the core, raw text alone or a general arithmetic system.
- `implementation.lossless-adapters` links the actual mechanisms and retains an empty
  claims list rather than treating planned behavior as verified PASS.
- `evidence.lossless-interchange` points to the exact tests and recorded artifact hashes.

These newly authored records remain agent-proposed/unreviewed. The original user
requirement is linked as provenance; the agent's interpretation is not silently
promoted into a new normative model edition. Source-aware test observations and
independent consumer construction remain distinct.

A maintainer changing confidence handling should update the exact contract first,
add positive/negative vectors around the intended boundary, change the corresponding
implementation, and rerun `make test hardening` and the affected native sanitizer
checks. Keep historical fixtures and the legacy host-number mode. Record why the
change is compatible or introduce an explicit new profile version.

Run `python3 scripts/check_maintenance.py` to detect missing or changed bytes in the
small allowlist of artifacts cited by this observation. It deliberately does not fail
on every unrelated source change. A changed hash identifies stale evidence linkage,
not automatically a semantic regression. Do not update hashes merely to make CI pass:
review the contract and rerun the relevant evidence, then record a new observation.
A matching hash establishes identity, not complete semantic freshness.

Future tests, not coverage claims: a browser extension receiving metadata; a CLI
round-trip; an independently deployed stateful service; a native library integration;
and an independently implemented language rewrite. Each needs its own contracts,
platform/authority conditions, held-out cases and executed results.
