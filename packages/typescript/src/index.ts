import {schemas} from './contracts.js';
import {canonical,compare} from './canonical.js';
export {canonical} from './canonical.js';
import {validateStructure} from './structure.js';
import { readFile } from "node:fs/promises";
import { resolve, dirname, sep } from "node:path";
export type Status="pass"|"fail"|"unknown";
export interface RecordValue { foreverVersion:string; id:string; kind:string; [key:string]:unknown }
export interface Issue {code:string;path:string;message:string;reference?:string}
const refs=new Set(["relatedCapabilities","relatedConstraints","relatedInvariants","relatedImplementations","requiredCapabilities","protectedInvariants","compatibilityObligations","relatedEntities","preservedCapabilities","preservedInvariants","compatibilityImpact","verification","satisfiesCapabilities","constrainedByInvariants","satisfiesConstraints","compatibilityContracts","evidence","sourceImplementation","targetImplementation","currentImplementation","scope","validationReferences"]);
const kinds=new Set(["intent","capability","invariant","constraint","dependency","decision","compatibility","migration","implementation","evidence"]);
function references(r:RecordValue):string[]{const out:string[]=[]; for(const k of refs){const properties=Object.values(schemas as Record<string,any>).find((s:any)=>s.properties?.kind?.const===r.kind)?.properties??{};if(!Object.hasOwn(properties,k))continue;const v=r[k]; if(typeof v==="string")out.push(v); else if(Array.isArray(v)) for(const x of v)if(typeof x==="string")out.push(x)} const verification=r.verification;if(['capability','constraint','invariant'].includes(r.kind)&&Array.isArray(verification))for(const v of verification){if(v&&typeof v==='object'&&Array.isArray(v.evidence))out.push(...v.evidence.filter((x:unknown):x is string=>typeof x==='string'))} const claims=r.claims; if(['implementation','migration'].includes(r.kind)&&Array.isArray(claims))for(const c of claims){if(c&&typeof c==="object"){const x=c as Record<string,unknown>;if(Array.isArray(x.evidence))out.push(...x.evidence.filter((e):e is string=>typeof e==="string"))}}return out}
export class Model {
 readonly entities=new Map<string,RecordValue>();
 constructor(public manifest:Record<string,unknown>,public records:RecordValue[]){for(const r of records)if(r&&typeof r.id==='string')this.entities.set(r.id,r)}
 validate():Issue[]{const errors:Issue[]=validateStructure(this.manifest,this.records);for(const r of this.records)if(r&&typeof r==='object')for(const ref of references(r))if(!this.entities.has(ref))errors.push({code:'broken-reference',path:r.id??'?',reference:ref,message:`unknown reference ${ref}`});return errors.sort((a,b)=>(a.code+a.path+(a.reference??'')).localeCompare(b.code+b.path+(b.reference??'')))}
 getEntity(id:string){return this.entities.get(id)}
 list(kind:string){return this.records.filter(r=>r.kind===kind).sort((a,b)=>compare(a.id,b.id))}
 traceEntity(id:string){if(!this.entities.has(id))throw new Error(`entity not found: ${id}`);const a=new Map([...this.entities.keys()].map(x=>[x,new Set<string>()]));for(const r of this.records)for(const x of references(r))if(a.has(x)){a.get(r.id)!.add(x);a.get(x)!.add(r.id)}const found=new Set<string>(),todo=[id];while(todo.length){const x=todo.pop()!;if(found.has(x))continue;found.add(x);todo.push(...[...a.get(x)!].filter(y=>!found.has(y)))}return [...found].sort().map(x=>this.entities.get(x)!)}
 explainDependency(id:string){const r=this.entities.get(id);if(!r||r.kind!=="dependency")throw new Error(`dependency not found: ${id}`);const out:Record<string,unknown>={};for(const k of ["id","dependencyName","purpose","reasonSelected","replacementClassification","requiredCapabilities","protectedInvariants","relatedConstraints","replacementRequirements","compatibilityObligations","historicalContext","provenance"])if(k in r)out[k]=r[k];return out}
 evaluateReplacement(current:string,candidate:string){const d=this.entities.get(current),c=this.entities.get(candidate);if(!d||d.kind!=="dependency")throw new Error(`dependency not found: ${current}`);if(!c||c.kind!=="implementation")throw new Error(`implementation not found: ${candidate}`);const req:string[]=[];for(const k of ["requiredCapabilities","protectedInvariants","relatedConstraints","replacementRequirements","compatibilityObligations"]){const v=d[k];if(Array.isArray(v))req.push(...v as string[])}return evaluate(candidate,[...new Set(req)],(c.claims??[]) as Claim[])}
 normalized(){return canonical({...this.manifest,records:[...this.records].sort((a,b)=>compare(a.id,b.id))})}
}
type Claim={requirement:string,status:Status,evidence?:string[],reason?:string};
function evaluate(candidate:string,requirements:string[],claims:Claim[]){const by=new Map(claims.map(c=>[c.requirement,c]));const checks=requirements.map(requirement=>by.get(requirement)??{requirement,status:"unknown" as Status,reason:"No candidate evidence supplied"});const states=new Set(checks.map(c=>c.status));return {candidate,result:states.has("fail")?"fail":checks.length>0&&states.size===1&&states.has("pass")?"pass":"partial",checks}}
export {loadModel} from "./node.js";
