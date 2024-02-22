<script lang="ts">
	import { page } from '$app/stores';
	import { Autocomplete } from '@skeletonlabs/skeleton';

	export let name: string;
	$: options = [];
	let value: string = $page.data?.[name] ?? '';

	async function updateOptions(value: string): Promise<void>
	{
		const params = new URLSearchParams({query: value});
		const data = await fetch('api/address/autocomplete'+ '?' + params).then((result) => result.json());
		options = data.items.map((item: {title: string; resultType: string}) => ({label: item.title, value: item.title}));
	}
</script>

<input {name} class="input" type="search" bind:value={value} on:input={updateOptions(value)} placeholder="" />
<div class="card w-full max-h-24 overflow-y-auto" tabindex="-1">
	<Autocomplete 
		bind:input={value}
		on:selection={(e) => {value = e.detail.label}}
		options={options}
		emptyState=''
	/>
</div>