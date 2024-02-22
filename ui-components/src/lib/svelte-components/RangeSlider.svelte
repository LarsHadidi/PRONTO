<script lang="ts">
	import { page } from '$app/stores';
	import { RangeSlider } from '@skeletonlabs/skeleton';
	export let name: string;
	export let min: number;
	export let max: number;
	export let step: number;
	export let value: number = $page.data?.[name];
</script>

<RangeSlider {name} {min} {max} {step} bind:value ticked />