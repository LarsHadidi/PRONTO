<script lang="ts" context="module">
  import { Story } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import TimePicker from "../../lib/svelte-components/TimePicker.svelte";

  export const meta: Meta<TimePicker> = {
    component: TimePicker,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": new Date(),
            },
          },
        },
      },
    },
  };
</script>

<Story name="Default">
  <TimePicker name="example-data"></TimePicker>
</Story>
