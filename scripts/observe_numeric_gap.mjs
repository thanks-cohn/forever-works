// Deliberate failure observation, not a passing conformance test.
import {normalize} from '../packages/javascript/src/model.js';
const raw='{"unknown":9007199254740993}';
const parsed=JSON.parse(raw);
console.log(JSON.stringify({input:raw,javascriptOutput:normalize(parsed),lossless:false}));
