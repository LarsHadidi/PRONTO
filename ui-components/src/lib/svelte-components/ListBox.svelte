<script lang="ts">
	import { page } from '$app/stores';
	import { ListBox, ListBoxItem } from '@skeletonlabs/skeleton';
	export let items: {value: unknown; label: string}[];
	export let name: string;
	export let multiple: boolean;

	let values: string[]|string = $page.data?.[name] ?? [];
	values = Array.isArray(values) ? values.map(String) : values.toString();
</script>

<ListBox {name} {multiple}>
	{#each items as item}
		<ListBoxItem bind:group={values} name={name} value={item.value}>{item.label}</ListBoxItem>
	{/each}
</ListBox>