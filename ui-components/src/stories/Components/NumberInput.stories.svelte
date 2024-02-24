<script lang="ts" context="module">
  import { Story } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import NumberInput from "../../lib/svelte-components/NumberInput.svelte";

  export const meta: Meta<NumberInput> = {
    component: NumberInput,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": "10",
            },
          },
        },
      },
    },
  };
</script>

<Story name="Default">
  <NumberInput name="example-data"></NumberInput>
</Story>
