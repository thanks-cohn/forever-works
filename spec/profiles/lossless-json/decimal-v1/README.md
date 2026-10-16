# Optional lossless JSON interchange: decimal-v1

An additive adapter profile, authorized by the lossless-core execution brief; no
new normative model edition, record kind, arithmetic operation or mandatory SDK.
The exact contract is [official API/LOSSLESS_JSON.md](../../../../docs/API/LOSSLESS_JSON.md).
Wire documents remain ordinary UTF-8 JSON. Numeric token objects are an adapter's
in-memory representation, never a replacement JSON schema number type.

This profile preserves both original token spelling (`source`) and exact mathematical
decimal value (`canonical`), in separate operations. Its explicit size, precision,
exponent and nesting bounds are resource policies, not a silent restriction on the
legacy API or all Standard 0.1 documents. Preserve 0.1 fixtures and modes. No consumer
must adopt this profile merely to read ordinary existing models.

Proof: conformance/lossless and scripts/check_lossless.py, original conformance suite,
plain-JS packed consumer and native sanitizers. Wrappers/generated algorithms are
labeled in the official coverage map. Supplied PASS claims never become executed proof.
