import {readFile,realpath,stat} from 'node:fs/promises';
import {dirname,resolve,sep,win32,isAbsolute} from 'node:path';
import {Model,ForeverApiError,createForeverApiFromModel} from './model.js';
import {parseInput} from './json-input.js';
import {validateStructure} from './structure.js';

/** Bounded filesystem adapter. Requires a directory stable against concurrent mutation. */
async function loadModelImpl(input) {
  const root=await realpath(resolve(input.endsWith('manifest.json')?dirname(input):input));
  let total=0;
  async function read(path) {
    const target=await realpath(path);
    if(!target.startsWith(root+sep))throw new Error('path-escape: real target outside model root');
    const info=await stat(target);
    if(!info.isFile())throw new Error('invalid-path: expected regular file');
    if(info.size>1048576||(total+=info.size)>16777216)throw new Error('resource-limit: model byte limit');
    return parseInput(await readFile(target));
  }
  const manifest=await read(resolve(root,'manifest.json'));
  const manifestErrors=validateStructure(manifest,[]).filter(e=>e.path.startsWith('manifest'));
  if(manifestErrors.length)throw new Error(`invalid-manifest: ${manifestErrors[0].path}; listed path may escape (escapes model root)`);
  const records=[],seen=new Set();
  for(const paths of Object.values(manifest.records))for(const relative of paths) {
    if(isAbsolute(relative)||win32.isAbsolute(relative)||relative.includes('\\')||relative.split('/').includes('..'))throw new Error('path-escape: expected portable relative path');
    const path=resolve(root,relative);
    if(!path.startsWith(root+sep))throw new Error('path-escape: lexical target outside model root');
    if(seen.has(path))throw new Error('duplicate-path');seen.add(path);
    if(seen.size>4096)throw new Error('resource-limit: record count exceeds 4096');
    records.push(await read(path));
  }
  return new Model(manifest,records);
}
/** Loading failures carry stable codes without including source JSON in messages. */
export async function loadModel(input) {
  try { return await loadModelImpl(input); }
  catch(error) {
    if(error instanceof ForeverApiError)throw error;
    const match=/^([a-z]+(?:-[a-z]+)*)(?::|$)/.exec(error.message??'');
    const code=error.code==='ERR_ENCODING_INVALID_ENCODED_DATA'?'invalid-utf8':error instanceof SyntaxError?'invalid-json':match?.[1]??'io';
    throw new ForeverApiError(code,`Unable to load model: ${code}`,{stage:'load',path:error.path??String(input)});
  }
}
export async function createForeverApi(input) {
  return createForeverApiFromModel(await loadModel(input),{name:'node-filesystem'});
}
