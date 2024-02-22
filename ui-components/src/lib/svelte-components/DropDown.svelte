<script lang="ts">
	import { page } from '$app/stores';
	export let items: {value: unknown; label: string}[];
	export let name: string;
	export let value: string[] = $page.data?.[name];
</script>

<select {name} class="select" bind:value>
	{#each items as item}
		<option value={item.value}>{item.label}</option>
	{/each}
</select>