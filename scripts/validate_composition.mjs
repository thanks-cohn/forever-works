#!/usr/bin/env node
import {loadComposition, validateComposition, normalizeComposition} from '../packages/ecosystem-composition/src/node.js';
import {loadModel} from '../packages/javascript/src/index.js';
try {
  const [root,file,modelRoot,...extra]=process.argv.slice(2);
  if(!root || !file || extra.length) throw Object.assign(new Error('Usage: node scripts/validate_composition.mjs ROOT RELATIVE_JSON [CANONICAL_MODEL_ROOT]'),{code:'invalid-argument'});
  let records;
  if(modelRoot) {
    const model=await loadModel(modelRoot);
    if(model.validate().length) throw Object.assign(new Error('Canonical model must validate before resolving composition references'),{code:'invalid-model'});
    records=model.records;
  }
  const result=validateComposition(await loadComposition(root,file),{records});
  process.stdout.write(normalizeComposition(result));
  process.exitCode=result.valid?0:1;
} catch(error) {
  process.stdout.write(normalizeComposition({error:{code:error.code ?? 'load-failed',message:error.message}}));
  process.exitCode=2;
}
