import {pathToFileURL} from 'node:url';
const {loadModel}=await import(pathToFileURL(process.argv[2]));
try {
 const m=await loadModel(process.argv[3]);
 const errors=m.validate();
 console.log(JSON.stringify({valid:errors.length===0,count:m.records.length,errors}));
}catch(e){console.log(JSON.stringify({valid:false,error:String(e)}));}
