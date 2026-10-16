// @ts-nocheck
import {Model} from './index.js';
import {canonicalLossless} from './lossless-json.js';
import {compare} from './canonical.js';
export * from './lossless-json.js';
export function createLosslessModel(manifest,records,documents){return new (class LosslessModel extends Model {
  constructor(manifest,records,documents){super(manifest,records);this.documents=Object.freeze(documents);}
  normalized(){return canonicalLossless({...this.manifest,records:[...this.records].sort((a,b)=>compare(a.id,b.id))});}
  sourceDocuments(){return this.documents;}
})(manifest,records,documents);}
