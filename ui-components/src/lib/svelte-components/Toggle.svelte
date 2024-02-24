<script lang="ts">
  import { page } from "$app/stores";
  import { SlideToggle } from "@skeletonlabs/skeleton";

  export let name: string;
  export let label: string;
  export let value: boolean = $page.data?.[name] ?? false;
</script>

<SlideToggle {name} bind:checked={value}>{label}</SlideToggle>
