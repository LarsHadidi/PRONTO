import { glob } from 'glob';
import { createWriteStream } from 'fs';
import { basename, extname } from 'path';

glob('./src/lib/svelte-components/*.svelte').then((components) =>
{
	components = components.map((file: string) => {return basename(file, extname(file))});
	let writeStream = createWriteStream('./src/lib/index.ts', {flags: 'w'});

	for(const component of components)
	{
		writeStream.write(`export { default as ${component} } from './svelte-components/${component}.svelte';\n`);
	}

	writeStream.end();
});