<script lang="ts" context="module">
  import { Story } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import ColorPicker from "../../lib/svelte-components/ColorPicker.svelte";

  export const meta: Meta<ColorPicker> = {
    component: ColorPicker,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": "#A8BEF1",
            },
          },
        },
      },
    },
  };
</script>

<Story name="Default">
  <ColorPicker name="example-data"></ColorPicker>
</Story>
