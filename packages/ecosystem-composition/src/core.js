import schema from '../../../spec/profiles/ecosystem-composition/v0.1/composition.schema.json' with {type: 'json'};

export const PROFILE = 'https://forever.works/profiles/ecosystem-composition';
const compare = (a, b) => {
  const left = Array.from(a, c => c.codePointAt(0)), right = Array.from(b, c => c.codePointAt(0));
  for (let i=0; i<Math.min(left.length,right.length); i++) if(left[i]!==right[i]) return left[i]-right[i];
  return left.length-right.length;
};
const serialize = (value, depth=0) => {
  if (!value || typeof value !== 'object') return JSON.stringify(value);
  const array=Array.isArray(value), entries=array?value.map((v,i)=>[i,v]):Object.keys(value).sort(compare).map(k=>[k,value[k]]);
  if(!entries.length) return array?'[]':'{}';
  const indent='  '.repeat(depth+1);
  return (array?'[':'{')+'\n'+entries.map(([k,v])=>indent+(array?'':JSON.stringify(k)+': ')+serialize(v,depth+1)).join(',\n')+'\n'+'  '.repeat(depth)+(array?']':'}');
};
/** Object keys sort by Unicode code point; array order remains significant. */
export const normalizeComposition = value => serialize(value) + '\n';
export const safeRelativePath = value => typeof value === 'string' && value.length > 0 && !/[\\:%?#\x00-\x1f]/.test(value) && value.split('/').every(p => p && p !== '.' && p !== '..');

// Deliberately limited to the vocabulary used by the bundled schema. Not a general
// JSON Schema implementation; the independent Draft 2020-12 test checks the schema.
function structure(value, rule, path, issue) {
  if (rule.$ref) return structure(value, schema.$defs[rule.$ref.split('/').at(-1)], path, issue);
  const type = Array.isArray(value) ? 'array' : value === null ? 'null' : typeof value;
  if (rule.type && type !== rule.type) { issue('schema-type', path, `Expected ${rule.type}`); return; }
  if ('const' in rule && value !== rule.const) issue('schema-const', path, 'Unsupported constant or version');
  if (rule.enum && !rule.enum.includes(value)) issue('schema-enum', path, 'Unsupported value');
  if (type === 'string') {
    if (rule.minLength && [...value].length < rule.minLength) issue('schema-min-length', path, 'Empty text');
    if (rule.pattern && !new RegExp(rule.pattern).test(value)) issue('schema-pattern', path, 'Invalid identifier or digest');
  }
  if (type === 'array') {
    if (value.length < (rule.minItems ?? 0)) issue('schema-min-items', path, 'Missing required items');
    const seen = new Set();
    value.forEach((v, i) => {
      const key = normalizeComposition(v);
      if (rule.uniqueItems && seen.has(key)) issue('schema-unique-items', `${path}/${i}`, 'Duplicate item');
      seen.add(key);
      if (rule.items) structure(v, rule.items, `${path}/${i}`, issue);
    });
  }
  if (type === 'object') {
    for (const key of rule.required ?? []) if (!Object.hasOwn(value, key)) issue('schema-required', `${path}/${key}`, 'Missing field');
    for (const [key, v] of Object.entries(value)) {
      const escaped = key.replaceAll('~', '~0').replaceAll('/', '~1');
      if (rule.propertyNames) structure(key, rule.propertyNames, `${path}/${escaped}`, issue);
      if (Object.hasOwn(rule.properties ?? {}, key)) structure(v, rule.properties[key], `${path}/${escaped}`, issue);
      else if (rule.additionalProperties === false) issue('schema-additional-property', `${path}/${escaped}`, 'Unexpected field; use namespaced extensions');
      else if (typeof rule.additionalProperties === 'object') structure(v, rule.additionalProperties, `${path}/${escaped}`, issue);
    }
  }
}

const CONTRACT_KINDS = new Set(['semantic','ordering','concurrency','retry','idempotency','consistency','offline','failure','recovery','authority','data-access','state','version-compatibility']);
const INTERACTIONS = new Set(['command','event','query','stream','replication','shared-state','coordination']);
const TABLES = ['ecosystems','participants','contracts','interactions','states','configurations','obligations','evidence'];

// Resource limits are implementation bounds, not limits on the abstract profile.
// Iterative traversal rejects cycles and non-JSON input before recursive schema work.
function boundedJson(value) {
  const stack=[{value,depth:0}], ancestors=new Set();
  let count=0;
  while(stack.length) {
    const entry=stack.pop(), v=entry.value;
    if(entry.exit) { ancestors.delete(v); continue; }
    if(++count>100000 || entry.depth>64) return 'Input exceeds 100000 values or nesting depth 64';
    if(v === null || typeof v === 'string' || typeof v === 'boolean') continue;
    if(typeof v === 'number' && Number.isFinite(v)) continue;
    if(typeof v !== 'object') return 'Input must contain only JSON values';
    if(!Array.isArray(v) && ![Object.prototype,null].includes(Object.getPrototypeOf(v))) return 'Input must use plain JSON objects';
    if(Array.isArray(v) && Object.keys(v).length!==v.length) return 'Input must use dense JSON arrays';
    if(ancestors.has(v)) return 'Input contains a cyclic object';
    ancestors.add(v); stack.push({value:v,exit:true});
    for(const item of Object.values(v)) stack.push({value:item,depth:entry.depth+1});
  }
}

/** Bounded structural/reference validation. records is an optional array of canonical
 * Standard 0.1 records, already validated by its own model validator. Evidence claims
 * are NEVER executed, trusted, or promoted to PASS by this static validator. */
export function validateComposition(document, {records} = {}) {
  const issues = [];
  const issue = (code, path, message, severity = 'error') => issues.push({code, path, message, severity});
  const finish = (obligations = []) => ({
    valid: !issues.some(i => i.severity === 'error'),
    issues: issues.sort((a,b) => compare(a.path,b.path) || compare(a.code,b.code) || compare(a.message,b.message)),
    verification: {status:'UNKNOWN', obligations}
  });
  const bound=boundedJson(document);
  if(bound) { issue('input-limit','',bound); return finish(); }
  structure(document, schema, '', issue);
  if (issues.length) return finish();
  const tables = Object.fromEntries(TABLES.map(k => [k, new Map()]));
  const global = new Set();
  for (const key of TABLES) for (const [n, entity] of document[key].entries()) {
    if (global.has(entity.id)) issue('duplicate-id', `/${key}/${n}/id`, entity.id);
    global.add(entity.id);
    tables[key].set(entity.id, entity);
  }
  const ref = (table, id, path) => {
    if (!tables[table].has(id)) issue('dangling-reference', path, `${table}: ${id}`);
    return tables[table].get(id);
  };
  const refs = (table, ids, path) => ids.forEach((id,i) => ref(table,id,`${path}/${i}`));
  if(records !== undefined && (!Array.isArray(records) || records.some(r=>!r || typeof r.id!=='string' || typeof r.kind!=='string'))) {
    issue('record-context','', 'Expected an array of independently validated canonical records');
    return finish();
  }
  const recordMap = records === undefined ? undefined : new Map(records.map(r => [r.id,r]));
  if(recordMap && recordMap.size!==records.length) issue('record-context','','Canonical record IDs must be unique');
  const recordRef = (r,path,kind) => {
    if (kind && r.kind !== kind) issue('record-kind',path,`Expected ${kind}`);
    if (!recordMap) issue('record-unresolved',path,`Canonical record not loaded: ${r.id}`,'warning');
    else if (!recordMap.has(r.id)) issue('record-not-found',path,r.id);
    else if (recordMap.get(r.id).kind !== r.kind) issue('record-kind',path,r.id);
  };
  const requirementRef = (r,path) => {
    recordRef(r,path);
    if (!['intent','capability','invariant','constraint','compatibility'].includes(r.kind)) issue('requirement-kind',path,r.kind);
  };
  // Opaque extensions are preserved but never interpreted as permissions or proof.
  const walkExtensions = (v,path='') => {
    if (!v || typeof v !== 'object') return;
    for (const [k,item] of Object.entries(v)) {
      if (k === 'extensions') { if (Object.keys(item).length) issue('unsupported-extension',`${path}/extensions`,'Extension semantics are undetermined','warning'); }
      else if(!['parameters','implementationBindings','bindings'].includes(k)) walkExtensions(item,`${path}/${k}`);
    }
  };
  walkExtensions(document);
  if (document.provenance.sourceType !== 'explicit' || document.provenance.reviewStatus !== 'accepted') issue('authority-unreviewed','/provenance','Validation does not approve intent','warning');
  document.ecosystems.forEach((e,i) => {
    const p=`/ecosystems/${i}`;
    e.intentRefs.forEach((r,n) => recordRef(r,`${p}/intentRefs/${n}`,'intent'));
    refs('participants',e.participantRefs,`${p}/participantRefs`);
    refs('obligations',e.obligationRefs,`${p}/obligationRefs`);
    for(const oid of e.obligationRefs) {
      const o=tables.obligations.get(oid);
      if(o && (o.scope.kind!=='ecosystem' || o.scope.ref!==e.id)) issue('obligation-scope',`${p}/obligationRefs`,'Collective obligation belongs to another scope');
    }
  });
  document.participants.forEach((p,i) => {
    const path=`/participants/${i}`;
    p.recordRefs.forEach((r,n)=>recordRef(r,`${path}/recordRefs/${n}`));
    if (p.ecosystemRef) ref('ecosystems',p.ecosystemRef,`${path}/ecosystemRef`);
    const ports=new Set();
    p.ports.forEach((port,j) => {
      const pp=`${path}/ports/${j}`;
      if(ports.has(port.id)) issue('duplicate-port',pp,port.id);
      ports.add(port.id);
      for(const field of ['providedCapabilities','requiredCapabilities']) port[field].forEach((r,n)=>recordRef(r,`${pp}/${field}/${n}`,'capability'));
      refs('contracts',port.contractRefs,`${pp}/contractRefs`);
    });
  });
  // Containment cycles are forbidden; communication cycles remain legal.
  const done=new Set(), active=new Set();
  for(const start of tables.ecosystems.keys()) {
    const stack=[{id:start,exit:false}];
    while(stack.length) {
      const {id,exit}=stack.pop();
      if(exit) {active.delete(id);done.add(id);continue;}
      if(active.has(id)) { issue('nested-cycle','/ecosystems',id);continue; }
      if(done.has(id)) continue;
      active.add(id);stack.push({id,exit:true});
      for(const pid of tables.ecosystems.get(id)?.participantRefs ?? []) {
        const nested=tables.participants.get(pid)?.ecosystemRef;
        if(nested && tables.ecosystems.has(nested)) stack.push({id:nested,exit:false});
      }
    }
  }
  document.contracts.forEach((c,i) => {
    if(!CONTRACT_KINDS.has(c.kind)) issue('unsupported-semantics',`/contracts/${i}/kind`,c.kind,'warning');
    if(Object.keys(c.parameters ?? {}).length) issue('parameters-uninterpreted',`/contracts/${i}/parameters`,'Policy parameters are declarations, not executed constraints','warning');
    c.requirementRefs.forEach((r,n)=>requirementRef(r,`/contracts/${i}/requirementRefs/${n}`));
  });
  document.states.forEach((s,i) => {
    ref('participants',s.owner,`/states/${i}/owner`);
    refs('participants',s.authorizedWriters,`/states/${i}/authorizedWriters`);
    refs('contracts',s.contractRefs,`/states/${i}/contractRefs`);
  });
  document.interactions.forEach((edge,i) => {
    const path=`/interactions/${i}`;
    if(!INTERACTIONS.has(edge.semantics)) issue('unsupported-semantics',`${path}/semantics`,edge.semantics,'warning');
    const members=new Set();
    for(const direction of ['from','to']) edge[direction].forEach((endpoint,j) => {
      const p=`${path}/${direction}/${j}`;
      members.add(endpoint.participant);
      const participant=ref('participants',endpoint.participant,`${p}/participant`);
      const port=participant?.ports.find(port=>port.id===endpoint.port);
      if(participant && !port) issue('dangling-port',`${p}/port`,endpoint.port);
      if(port && port.direction !== 'inout' && port.direction !== (direction==='from'?'out':'in')) issue('port-direction',p,endpoint.port);
    });
    refs('contracts',edge.contractRefs,`${path}/contractRefs`);
    refs('states',edge.stateRefs,`${path}/stateRefs`);
    edge.authority.grants.forEach((grant,j) => {
      const p=`${path}/authority/grants/${j}`;
      ref('participants',grant.participant,`${p}/participant`);
      if(!members.has(grant.participant)) issue('authority-scope',p,'Grant recipient is not an endpoint');
      if(grant.permissions.some(permission=>['read','write'].includes(permission)) && !grant.stateRefs.length) issue('authority-scope',p,'State access must declare its state scope');
      grant.stateRefs.forEach((sid,k) => {
        const state=ref('states',sid,`${p}/stateRefs/${k}`);
        if(!edge.stateRefs.includes(sid)) issue('authority-scope',p,'Grant state is outside interaction');
        if(grant.permissions.includes('write') && state && state.owner!==grant.participant && !state.authorizedWriters.includes(grant.participant)) issue('state-authority',p,'Writer not authorized by state owner declaration');
      });
      if(grant.permissions.some(p=>!['read','write','invoke','subscribe'].includes(p))) issue('unsupported-permission',p,'Permission semantics undetermined','warning');
    });
  });
  document.configurations.forEach((c,i) => {
    const path=`/configurations/${i}`;
    refs('participants',c.participants,`${path}/participants`);
    refs('interactions',c.interactions,`${path}/interactions`);
    refs('obligations',c.obligationRefs,`${path}/obligationRefs`);
    for(const o of document.obligations) {
      const selected = !o.configurationRefs.length || o.configurationRefs.includes(c.id);
      const active = o.scope.kind==='ecosystem' ||
        (o.scope.kind==='configuration' && o.scope.ref===c.id) ||
        (o.scope.kind==='participant' && c.participants.includes(o.scope.ref)) ||
        (o.scope.kind==='interaction' && c.interactions.includes(o.scope.ref));
      if(selected && active && !c.obligationRefs.includes(o.id)) issue('obligation-missing',`${path}/obligationRefs`,`${o.id} is applicable but omitted`,'warning');
    }
    for(const oid of c.obligationRefs) {
      const o=tables.obligations.get(oid);
      if(!o) continue;
      if(o.configurationRefs.length && !o.configurationRefs.includes(c.id)) issue('obligation-scope',`${path}/obligationRefs`,`${oid} excludes configuration`);
      if(o.scope.kind==='participant' && !c.participants.includes(o.scope.ref)) issue('obligation-scope',`${path}/obligationRefs`,`${oid} has inactive participant`);
      if(o.scope.kind==='interaction' && !c.interactions.includes(o.scope.ref)) issue('obligation-scope',`${path}/obligationRefs`,`${oid} has inactive interaction`);
      if(o.scope.kind==='configuration' && o.scope.ref!==c.id) issue('obligation-scope',`${path}/obligationRefs`,`${oid} belongs to another configuration`);
    }
    for(const id of Object.keys(c.bindings ?? {})) if(!c.participants.includes(id)) issue('binding-scope',`${path}/bindings/${id}`,'Inactive participant');
    for(const id of c.interactions) {
      const edge=tables.interactions.get(id);
      for(const endpoint of [...edge?.from ?? [],...edge?.to ?? []]) if(!c.participants.includes(endpoint.participant)) issue('inactive-endpoint',path,endpoint.participant);
      for(const sid of edge?.stateRefs ?? []) {
        const state=tables.states.get(sid);
        if(state && !c.participants.includes(state.owner)) issue('inactive-state-owner',path,state.owner);
      }
    }
  });
  document.obligations.forEach((o,i) => {
    const path=`/obligations/${i}`;
    const table={ecosystem:'ecosystems',participant:'participants',interaction:'interactions',configuration:'configurations'}[o.scope.kind];
    ref(table,o.scope.ref,`${path}/scope/ref`);
    refs('configurations',o.configurationRefs,`${path}/configurationRefs`);
    refs('evidence',o.evidenceRefs,`${path}/evidenceRefs`);
    o.requirementRefs.forEach((r,n)=>requirementRef(r,`${path}/requirementRefs/${n}`));
    for(const cid of o.configurationRefs) {
      const c=tables.configurations.get(cid);
      const active = o.scope.kind==='participant'? c?.participants : o.scope.kind==='interaction'?c?.interactions:undefined;
      if(active && !active.includes(o.scope.ref)) issue('obligation-scope',path,`Inactive scope in ${cid}`);
      if(o.scope.kind==='configuration' && o.scope.ref!==cid) issue('obligation-scope',path,cid);
    }
    if(o.scope.kind==='ecosystem' && tables.ecosystems.has(o.scope.ref) && !tables.ecosystems.get(o.scope.ref).obligationRefs.includes(o.id)) issue('obligation-scope',path,'Collective obligation must be listed by its ecosystem');
    for(const eid of o.evidenceRefs) if(tables.evidence.has(eid) && tables.evidence.get(eid).obligation!==o.id) issue('evidence-scope',path,eid);
  });
  document.evidence.forEach((e,i) => {
    const path=`/evidence/${i}`;
    const o=ref('obligations',e.obligation,`${path}/obligation`);
    const c=ref('configurations',e.configuration,`${path}/configuration`);
    recordRef(e.recordRef,`${path}/recordRef`,'evidence');
    for(const field of ['artifact','scopeArtifact']) if(!safeRelativePath(e[field].path)) issue('unsafe-path',`${path}/${field}/path`,'Expected plain relative artifact path');
    if(o && (!o.evidenceRefs.includes(e.id) || (o.configurationRefs.length && !o.configurationRefs.includes(e.configuration)))) issue('evidence-scope',path,'Evidence is not scoped to this obligation/configuration');
    if(o && c && !c.obligationRefs.includes(o.id)) issue('evidence-scope',path,'Evidence obligation is not selected by configuration');
    for(const pid of Object.keys(e.subjectDigests)) if(!c?.participants.includes(pid)) issue('evidence-scope',`${path}/subjectDigests/${pid}`,'Inactive subject');
    if(c && c.participants.some(pid=>!Object.hasOwn(e.subjectDigests,pid))) issue('evidence-subjects',path,'Evidence must bind every active participant artifact');
    issue('evidence-unverified',path,'Declared evidence has not been independently authenticated or executed','warning');
  });
  // Explicit independent obligations are required at collective and interaction scope.
  for(const e of document.ecosystems) if(!document.obligations.some(o=>o.scope.kind==='ecosystem' && o.scope.ref===e.id)) issue('obligation-missing','/ecosystems',e.id,'warning');
  for(const e of document.interactions) if(!document.obligations.some(o=>o.scope.kind==='interaction' && o.scope.ref===e.id)) issue('obligation-missing','/interactions',e.id,'warning');
  return finish(document.obligations.map(o=>({id:o.id,status:'UNKNOWN',reason:o.evidenceRefs.length?'Evidence claims require independent verification':'No independent evidence supplied'})).sort((a,b)=>compare(a.id,b.id)));
}
