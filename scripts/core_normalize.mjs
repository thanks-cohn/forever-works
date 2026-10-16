import {readFile} from 'node:fs/promises';
import {pathToFileURL} from 'node:url';
const binding=await import(pathToFileURL(process.argv[2]));
const value=JSON.parse(await readFile(process.argv[3],'utf8'));
process.stdout.write((binding.normalize??binding.canonical)(value));
