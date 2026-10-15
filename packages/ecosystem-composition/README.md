# Ecosystem composition reference validator

Dependency-free plain JavaScript proof for the experimental, opt-in
[composition profile 0.1](../../spec/profiles/ecosystem-composition/v0.1/README.md).
The profile and JSON Schema are language-neutral; this directory is a replaceable
reference implementation, not a new canonical format or published package.

```js
import {loadComposition, validateComposition} from './src/node.js';
const document = await loadComposition('/path/to/model', 'composition.json');
const result = validateComposition(document, {records: validatedCanonicalRecords});
// result.valid checks structure/references. result.verification.status is UNKNOWN.
```

Use `src/core.js` for already parsed, filesystem-independent JSON. Node.js 20.18+
is the current proof runtime; no TypeScript compiler is needed. See the
[adapter reference](../../docs/API/ECOSYSTEM_COMPOSITION_PROFILE_V0_1.md) for exact
helpers, errors, loader limits and CLI exit codes. Public API v0.1 is unchanged.

From the repository root:

```sh
node --test packages/javascript/test/ecosystem-composition.test.js
node scripts/validate_composition.mjs conformance/ecosystem-composition/v0.1 valid/many-to-many-multiedge-cycle.json conformance/fixtures/complete/forever
```
