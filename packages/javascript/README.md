# Forever Works JavaScript

Dependency-free ESM proof binding authored in plain JavaScript. It does not import the TypeScript binding and does not require `tsc`.

```js
import {loadModel, Model} from "@forever-works/javascript";

const model = await loadModel("forever");
console.log(model.validate());

// The semantic core also accepts already-parsed, host-independent JSON data.
const inMemory = new Model(manifest, records);
```
