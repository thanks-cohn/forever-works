import test from 'node:test';
import assert from 'node:assert/strict';
import {readFile, writeFile, mkdtemp, mkdir, symlink, rm} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {validateComposition, normalizeComposition, safeRelativePath} from '../../ecosystem-composition/src/core.js';
import {loadComposition} from '../../ecosystem-composition/src/node.js';
import {loadModel, createForeverApi} from '../src/index.js';
const root='conformance/ecosystem-composition/v0.1';
const fixture=async name=>JSON.parse(await readFile(`${root}/valid/${name}.json`,'utf8'));
const model=await loadModel('conformance/fixtures/complete/forever');
assert.deepEqual(model.validate(),[]);
const records=model.records;

test('optional composition shared conformance catalog',async t=>{
  const {cases}=JSON.parse(await readFile(`${root}/cases.json`,'utf8'));
  for(const entry of cases) await t.test(entry.name,async()=>{
    const document=await loadComposition(root,entry.path);
    const result=validateComposition(document,{records});
    assert.equal(result.valid,entry.valid,normalizeComposition(result));
    assert.equal(result.verification.status,entry.verificationStatus);
    assert.ok(result.verification.obligations.every(o=>o.status==='UNKNOWN'));
    if(entry.error) assert.ok(result.issues.some(i=>i.code===entry.error && i.severity==='error'),normalizeComposition(result));
    if(entry.warning) assert.ok(result.issues.some(i=>i.code===entry.warning && i.severity==='warning'),normalizeComposition(result));
    assert.deepEqual(validateComposition(document,{records}),result);
  });
});

test('four-party graph, multiedges, cycles and alternatives are exercised',async()=>{
  const fan=await fixture('four-participant-fan');
  assert.equal(fan.participants.length,4);
  assert.equal(fan.interactions[0].to.length,2);
  assert.equal(fan.interactions[1].from.length,2);
  const multi=await fixture('many-to-many-multiedge-cycle');
  assert.ok(multi.interactions.some(e=>e.from.length>1 && e.to.length>1));
  const alts=await fixture('deployment-alternatives');
  assert.equal(alts.configurations.length,2);
  assert.notEqual(alts.configurations[0].participants.length,alts.configurations[1].participants.length);
});

test('canonical model references require exact ID and record kind',async()=>{
  const d=await fixture('single-component');
  const unresolved=validateComposition(d);
  assert.equal(unresolved.valid,true);
  assert.ok(unresolved.issues.some(i=>i.code==='record-unresolved'));
  assert.equal(validateComposition(d,{records}).issues.some(i=>i.code==='record-unresolved'),false);
  d.ecosystems[0].intentRefs[0].id='intent.missing';
  assert.ok(validateComposition(d,{records}).issues.some(i=>i.code==='record-not-found'));
});

test('forged PASS metadata and existing component evidence never verify a suite',async()=>{
  const d=await fixture('unverified-pass-claim');
  assert.equal(d.evidence[0].claimedStatus,'PASS');
  assert.ok(records.some(r=>r.id===d.evidence[0].recordRef.id));
  const result=validateComposition(d,{records});
  assert.equal(result.valid,true);
  assert.equal(result.verification.status,'UNKNOWN');
  assert.ok(result.verification.obligations.every(o=>o.status==='UNKNOWN'));
  d.evidence[0].claimedStatus='FAIL';
  assert.equal(validateComposition(d,{records}).verification.status,'UNKNOWN');
});

test('normalization preserves provenance, opaque extensions, and meaningful array order',async()=>{
  const d=await fixture('four-participant-fan');
  d.extensions={'example.org.opaque':{z:1,a:[3,1,2]}};
  const before=structuredClone(d);
  const output=normalizeComposition(d);
  assert.deepEqual(JSON.parse(output),d);
  assert.equal(output,normalizeComposition(JSON.parse(output)));
  const reversed=Object.fromEntries(Object.entries(d).reverse());
  assert.equal(normalizeComposition(reversed),output);
  validateComposition(d,{records});
  assert.deepEqual(d,before);
  assert.equal(d.provenance.reviewStatus,'unreviewed');
  assert.equal(d.provenance.sourceType,'agent-proposed');
});

test('loader rejects traversal, encoded paths, absolute paths and symlink escape',async()=>{
  const dir=await mkdtemp(join(tmpdir(),'forever-composition-'));
  try {
    await mkdir(join(dir,'inside'));
    await writeFile(join(dir,'outside.json'),'{}');
    await symlink(join(dir,'outside.json'),join(dir,'inside','linked.json'));
    for(const path of ['../outside.json','/outside.json','a\\b.json','%2e%2e/x','C:/outside.json','./x','a//b']) {
      assert.equal(safeRelativePath(path),false,path);
      await assert.rejects(loadComposition(join(dir,'inside'),path),{code:'unsafe-path'});
    }
    await assert.rejects(loadComposition(join(dir,'inside'),'linked.json'),{code:'unsafe-path'});
    await writeFile(join(dir,'inside','bad.json'),'not json');
    await assert.rejects(loadComposition(join(dir,'inside'),'bad.json'),{code:'invalid-json'});
    await assert.rejects(loadComposition(join(dir,'inside'),'missing.json'),{code:'load-failed'});
    await writeFile(join(dir,'inside','safe.json'),'{}');
    assert.deepEqual(await loadComposition(join(dir,'inside'),'safe.json'),{});
  } finally {await rm(dir,{recursive:true,force:true});}
});

test('legacy models and Public API v0.1 do not opt in or advertise profile operations',async()=>{
  const api=await createForeverApi('conformance/fixtures/minimal/forever');
  assert.equal(api.validateModel().valid,true);
  assert.equal(api.describe().foreverApiVersion,'0.1');
  for(const op of ['validateComposition','listEcosystems','resolveConfiguration']) assert.equal(api.describe().operations.includes(op),false);
});

test('malformed JSON values produce structural issues, not exceptions',()=>{
  for(const value of [null,[],1,'text',{}, {profileVersion:'0.1'}]) {
    const result=validateComposition(value);
    assert.equal(result.valid,false);
    assert.equal(result.verification.status,'UNKNOWN');
  }
});

test('optional manifest extension preserves Standard 0.1 validity and requires opt-in',async()=>{
  const {loadOptionalComposition}=await import('../../ecosystem-composition/src/node.js');
  const {Model}=await import('../src/model.js');
  const pointer={profileVersion:'0.1',path:'valid/four-participant-fan.json'};
  const manifest={...model.manifest,extensions:{'forever.works.ecosystem-composition':pointer}};
  assert.deepEqual(new Model(manifest,records).validate(),[]);
  assert.deepEqual(await loadOptionalComposition(root,model.manifest),{enabled:false,document:null,validation:null});
  const loaded=await loadOptionalComposition(root,manifest,{records});
  assert.equal(loaded.enabled,true);
  assert.equal(loaded.validation.valid,true);
  assert.equal(loaded.validation.verification.status,'UNKNOWN');
  const version={extensions:{'forever.works.ecosystem-composition':{...pointer,profileVersion:'9.0'}}};
  await assert.rejects(loadOptionalComposition(root,version),{code:'unsupported-profile'});
  const unsafe={extensions:{'forever.works.ecosystem-composition':{...pointer,path:'../outside.json'}}};
  await assert.rejects(loadOptionalComposition(root,unsafe),{code:'unsafe-path'});
  const extra={extensions:{'forever.works.ecosystem-composition':{...pointer,verified:true}}};
  await assert.rejects(loadOptionalComposition(root,extra),{code:'invalid-profile-reference'});
});

test('bounded input handles cyclic, excessively deep, non-JSON and malformed record context',async()=>{
  const cycle={};cycle.self=cycle;
  let deep={};for(let i=0;i<70;i++) deep={next:deep};
  for(const value of [cycle,deep,{n:Infinity},{n:undefined},{n:1n},{n:new Date()},new Array(2)]) {
    const result=validateComposition(value);
    assert.equal(result.valid,false);
    assert.equal(result.issues[0].code,'input-limit');
  }
  const d=await fixture('single-component');
  assert.ok(validateComposition(d,{records:{}}).issues.some(i=>i.code==='record-context'));
  assert.ok(validateComposition(d,{records:[...records,records[0]]}).issues.some(i=>i.code==='record-context'));
});

test('opaque implementation bindings are not interpreted as privilege or extension declarations',async()=>{
  const d=await fixture('single-component');
  d.participants[0].implementationBindings={extensions:null,authority:{inheritPrivileges:true},technology:'arbitrary-future-runtime'};
  assert.equal(validateComposition(d,{records}).valid,true);
  assert.equal(validateComposition(d,{records}).verification.status,'UNKNOWN');
});

test('loader bounds size, requires UTF-8, and does not read evidence artifacts',async()=>{
  const dir=await mkdtemp(join(tmpdir(),'forever-composition-limits-'));
  try {
    await writeFile(join(dir,'large.json'),' '.repeat(4*1024*1024+1));
    await assert.rejects(loadComposition(dir,'large.json'),{code:'input-limit'});
    await writeFile(join(dir,'invalid-utf8.json'),Buffer.from([123,34,120,34,58,34,255,34,125]));
    await assert.rejects(loadComposition(dir,'invalid-utf8.json'),{code:'invalid-encoding'});
    const d=await fixture('unverified-pass-claim');
    await writeFile(join(dir,'composition.json'),JSON.stringify(d));
    const loaded=await loadComposition(dir);
    assert.equal(validateComposition(loaded,{records}).verification.status,'UNKNOWN');
  } finally {await rm(dir,{recursive:true,force:true});}
});

test('normalization defines lexical object ordering independently of numeric key enumeration',()=>{
  const text=normalizeComposition({'2':'two','10':'ten','\ue000':1,'\u{10000}':2});
  assert.ok(text.indexOf('"10"')<text.indexOf('"2"'));
  assert.ok(text.indexOf('\ue000')<text.indexOf('\u{10000}'));
  assert.equal(text,normalizeComposition(JSON.parse(text)));
});

test('profile CLI preserves success, validation failure, and operational failure exit codes',async()=>{
  const {execFile}=await import('node:child_process');
  const {promisify}=await import('node:util');
  const run=promisify(execFile);
  const script='scripts/validate_composition.mjs';
  const {stdout}=await run(process.execPath,[script,root,'valid/four-participant-fan.json','conformance/fixtures/complete/forever']);
  assert.equal(JSON.parse(stdout).valid,true);
  assert.equal(JSON.parse(stdout).verification.status,'UNKNOWN');
  await assert.rejects(run(process.execPath,[script,root,'invalid/dangling-port.json']),e=>e.code===1 && JSON.parse(e.stdout).valid===false);
  await assert.rejects(run(process.execPath,[script,root,'../outside.json']),e=>e.code===2 && JSON.parse(e.stdout).error.code==='unsafe-path');
  await assert.rejects(run(process.execPath,[script]),e=>e.code===2 && JSON.parse(e.stdout).error.code==='invalid-argument');
});

test('profile normalization and validation match versioned shared goldens',async()=>{
  for(const name of ['four-participant-fan','unverified-pass-claim']) {
    const d=await fixture(name);
    assert.equal(normalizeComposition(validateComposition(d,{records})),await readFile(`${root}/expected/${name}.validation.json`,'utf8'));
  }
  assert.equal(normalizeComposition(await fixture('four-participant-fan')),await readFile(`${root}/expected/four-participant-fan.normalized.json`,'utf8'));
});

test('configuration inventory cannot silently omit applicable obligations',async()=>{
  const d=await fixture('four-participant-fan');
  d.configurations[0].obligationRefs=[];
  const result=validateComposition(d,{records});
  assert.equal(result.valid,true);
  assert.equal(result.issues.filter(i=>i.code==='obligation-missing').length,3);
  assert.equal(result.verification.status,'UNKNOWN');
});

test('unknown policy and permission semantics stay visibly undetermined',async()=>{
  const d=await fixture('four-participant-fan');
  d.contracts[0].kind='future-ordering-model';
  d.contracts[0].parameters={ordering:'future-policy',retry:{strategy:'future-strategy'}};
  d.interactions[0].authority.grants=[{participant:'participant.collector',permissions:['future-permission'],stateRefs:[]}];
  const result=validateComposition(d,{records});
  assert.equal(result.valid,true);
  for(const code of ['unsupported-semantics','parameters-uninterpreted','unsupported-permission']) assert.ok(result.issues.some(i=>i.code===code));
  assert.equal(result.verification.status,'UNKNOWN');
});
