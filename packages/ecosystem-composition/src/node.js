import {open, realpath} from 'node:fs/promises';
import {resolve, sep} from 'node:path';
import {safeRelativePath, validateComposition} from './core.js';
export {validateComposition, normalizeComposition, PROFILE} from './core.js';

export class CompositionLoadError extends Error {
  constructor(code, message) { super(message); this.name='CompositionLoadError'; this.code=code; }
}
/** Reads only the explicitly selected profile. Never follows evidence or nested refs.
 * Both lexical traversal and symlink escapes are rejected before reading the file. */
export async function loadComposition(root, relative='composition.json') {
  if(!safeRelativePath(relative)) throw new CompositionLoadError('unsafe-path','Unsafe composition path');
  try {
    const base=await realpath(root);
    const path=await realpath(resolve(base,relative));
    if(!path.startsWith(base+sep)) throw new CompositionLoadError('unsafe-path','Composition escapes root');
    const file=await open(path,'r');
    try {
      const info=await file.stat();
      if(!info.isFile()) throw new CompositionLoadError('load-failed','Expected a regular JSON file');
      if(info.size>4*1024*1024) throw new CompositionLoadError('input-limit','Profile exceeds 4 MiB reference-loader limit');
      const bytes=await file.readFile();
      if(bytes.length>4*1024*1024) throw new CompositionLoadError('input-limit','Profile exceeds 4 MiB reference-loader limit');
      let text;
      try { text=new TextDecoder('utf-8',{fatal:true}).decode(bytes); }
      catch { throw new CompositionLoadError('invalid-encoding','Profile must be valid UTF-8'); }
      return JSON.parse(text);
    } finally { await file.close(); }
  } catch(error) {
    if(error instanceof CompositionLoadError) throw error;
    throw new CompositionLoadError(error instanceof SyntaxError?'invalid-json':'load-failed',error.message);
  }
}
export async function validateCompositionFile(root, relative, options) {
  return validateComposition(await loadComposition(root,relative),options);
}

/** Standard 0.1 manifests remain opt-in through an owner-qualified extension.
 * This helper does not alter or extend Public API v0.1 discovery. */
export async function loadOptionalComposition(root, manifest, options) {
  const pointer=manifest.extensions?.['forever.works.ecosystem-composition'];
  if(pointer===undefined) return {enabled:false,document:null,validation:null};
  if(!pointer || typeof pointer!=='object' || Array.isArray(pointer) ||
     Object.keys(pointer).some(k=>!['profileVersion','path'].includes(k)) || typeof pointer.path!=='string') {
    throw new CompositionLoadError('invalid-profile-reference','Expected profileVersion and a relative path');
  }
  if(pointer.profileVersion!=='0.1') throw new CompositionLoadError('unsupported-profile','Unsupported composition profile version');
  const document=await loadComposition(root,pointer.path);
  return {enabled:true,document,validation:validateComposition(document,options)};
}
