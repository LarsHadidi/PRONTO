<script lang="ts">
	import { page } from "$app/stores";
	export let name: string;
	export let value: string = $page.data?.[name]?.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
</script>

<input name={name} type="time" class="input" bind:value>