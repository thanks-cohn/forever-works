# Read a model in five minutes

You need ordinary UTF-8 JSON, a local checkout and Python 3.9+ for the CLI. No account,
agent or hosted service is needed. Run these commands from the checkout root:

```sh
cat conformance/fixtures/minimal/forever/project.intent.json
packages/cli/bin/forever --root conformance/fixtures/minimal/forever validate
packages/cli/bin/forever --root examples/file-transfer/forever validate
packages/cli/bin/forever --root examples/file-transfer/forever trace dependency.old-streamer
packages/cli/bin/forever --root examples/file-transfer/forever --json explain dependency.old-streamer
packages/cli/bin/forever --root examples/file-transfer/forever evaluate-replacement dependency.old-streamer implementation.wasm-streamer
```

Read the dependency's purpose and reasonSelected, then follow requiredCapabilities,
protectedInvariants and compatibilityObligations. Intent → requirements → current
implementation → evidence explains both why the component exists and what a change
must preserve. The replacement result's bounded-memory check is `unknown`: a claim
or evidence filename cannot substitute for running the benchmark on the actual target.
You must supply project-specific requirements, accepted rationale, target environment
and independently observed evidence; the model cannot discover these facts for you.

For a new project, `packages/cli/bin/forever init <directory>` writes unreviewed TODOs.
Start with one useful intent and the dependency you need to understand. Review them
before treating them as authoritative. Incremental adoption needs no whole-world model.
Plain JS users can use the package example in the README without compiling TypeScript.

Continue to [Public API v0.1](API/PUBLIC_API_V0_1.md), the
[exact reference and loader contract](API/CORE_INPUT_AND_NORMALIZATION.md),
[portable fixture examples](../conformance/fixtures) and
[conformance support](CONFORMANCE.md). Reading an evidence record never executes its
command or follows its URI.

## Exact numeric metadata

Plain JavaScript, no TypeScript compiler:

```js
import {parseLossless} from "@forever-works/javascript/lossless";
const document = parseLossless('{"revision":9007199254740993}');
console.log(document.source());       // original token and whitespace
console.log(document.canonical());    // exact decimal-v1 JSON
```

Use `loadModelLossless` from the main package for file models. Token values require
`canonicalLossless`; ordinary `JSON.stringify` deliberately rejects them. Existing
`loadModel` keeps host-number ergonomics and its documented precision limits.

The existing CLI has the same opt-in mode:

```sh
packages/cli/bin/forever --lossless --root conformance/lossless/forever validate
packages/cli/bin/forever --lossless --root conformance/lossless/forever normalize
```

The fixture includes large integers, precise decimals and tiny/huge finite exponents.
The lossless mode emits plain UTF-8 JSON, never SDK-specific token objects.
