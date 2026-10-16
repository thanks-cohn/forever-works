// cmd.exe does not expand POSIX globs. Pass real test files to Node on every host.
import {readdirSync} from 'node:fs';
import {join} from 'node:path';
import {spawnSync} from 'node:child_process';
const directory=process.argv[2];
const files=readdirSync(directory).filter(name=>name.endsWith('.test.js')).sort().map(name=>join(directory,name));
if(!files.length)throw new Error('No test files discovered');
const result=spawnSync(process.execPath,['--test',...files],{stdio:'inherit'});
if(result.error)throw result.error;
process.exit(result.status??1);
