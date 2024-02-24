<script lang="ts">
  import { page } from "$app/stores";
  export let name: string;
  export let value: string = $page.data?.[name]?.toISOString().split("T")[0];
</script>

<input {name} type="date" class="input" bind:value />
