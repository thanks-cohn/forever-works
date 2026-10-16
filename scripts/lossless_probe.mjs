import {readFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
const binding=await import(pathToFileURL(process.argv[2]));
if(process.argv[3]==='vectors'){
 const vectors=JSON.parse(await readFile('conformance/lossless/numbers.json','utf8'));
 console.log(JSON.stringify(vectors.map(({token})=>{const d=binding.parseLossless(token);return {source:d.source(),canonical:d.canonical()};})));
}else{
 try {const m=await binding.loadModelLossless(process.argv[3]);const errors=m.validate();console.log(JSON.stringify({valid:!errors.length,errors,normalized:errors.length?null:m.normalized(),sources:m.sourceDocuments().map(({document})=>document.source())}));}
 catch(error){console.log(JSON.stringify({valid:false,error:String(error)}));}
}
