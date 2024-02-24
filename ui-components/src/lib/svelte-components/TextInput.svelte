<script lang="ts">
  import { page } from "$app/stores";
  export let name: string;
  export let value: string = $page.data?.[name] ?? "";
</script>

<input {name} type="text" class="input" bind:value />
