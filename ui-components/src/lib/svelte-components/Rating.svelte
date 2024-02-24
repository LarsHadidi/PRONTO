<script lang="ts">
  import { Ratings } from "@skeletonlabs/skeleton";
  import { page } from "$app/stores";
  export let name: string;
  export let max: number;
  export let value: number = $page.data?.[name] ?? 0;

  function iconClick(event: CustomEvent<{ index: number }>): void {
    value = event.detail.index;
  }
</script>

<Ratings {name} {max} bind:value interactive on:icon={iconClick}>
  <svelte:fragment slot="empty">◯</svelte:fragment>
  <svelte:fragment slot="full">⚫</svelte:fragment>
</Ratings>
