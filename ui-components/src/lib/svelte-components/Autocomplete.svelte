<script lang="ts">
	import { page } from '$app/stores';
	import { Autocomplete, InputChip } from '@skeletonlabs/skeleton';
	import type { AutocompleteOption } from '@skeletonlabs/skeleton';

	export let name: string;
	export let options: AutocompleteOption[];

	let inputChip = '';
	let inputChipList: string[] = $page.data?.[name] ?? [];
	inputChipList = inputChipList.map((value) => ((options.find((option) => option.value === value))?.label ?? ''));
	$: values = inputChipList.map((label) => ((options.find((option) => option.label === label))?.value));

	function inputChipOptions(options: AutocompleteOption[]): string[] 
	{
		return options.map(option => (option.label));
	}
	function onInputChipSelect(event: any): void 
	{
		if (inputChipList.includes(event.detail.label) === false) {
			inputChipList = [...inputChipList, event.detail.label];
			inputChip = '';
		}
	}
</script>

<InputChip {name} placeholder="" bind:input={inputChip} bind:value={inputChipList} whitelist={inputChipOptions(options)} allowUpperCase />
<div class="card w-full max-h-24 overflow-y-auto" tabindex="-1">
	<Autocomplete 
		bind:input={inputChip} 
		options={options} 
		denylist={values} 
		on:selection={onInputChipSelect}
	/>
</div>