# File format

A `forever/manifest.json` inventories relative JSON record paths by plural record category. Paths MUST remain within the model directory, use `/`, and be unique. Each file contains one JSON object encoded as UTF-8. The manifest version governs the model; records repeat it so detached records remain intelligible. Unknown fields are tolerated and retained. See `spec/schemas`, `spec/VERSIONING.md`, and canonical normalization in `docs/CONFORMANCE.md`.
