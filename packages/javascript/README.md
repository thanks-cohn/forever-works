# Forever Works JavaScript

Dependency-free ESM proof binding authored in plain JavaScript. It does not import the TypeScript binding and does not require `tsc`.

The recommended Public API v0.1 façade is:

```js
import {createForeverApi} from "@forever-works/javascript";

const forever = await createForeverApi("./forever");
console.log(forever.describe());
console.log(forever.listDependencies());
```

For host-neutral use, import `createForeverApiFromModel` from
`@forever-works/javascript/core` and supply an already constructed `Model`.
The repository's `docs/API/PUBLIC_API_V0_1.md` is the authoritative contract.

The lower-level proof API remains available:

```js
import {loadModel, Model} from "@forever-works/javascript";

const model = await loadModel("forever");
console.log(model.validate());

// The semantic core also accepts already-parsed, host-independent JSON data.
const inMemory = new Model(manifest, records);
```
