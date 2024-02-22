<script lang="ts">
	import { page } from '$app/stores';
	export let name: string;
	export let value: number = $page.data?.[name];
</script>

<input {name} type="number" class="input" bind:value>