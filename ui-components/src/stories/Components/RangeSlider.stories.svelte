<script lang="ts" context="module">
  import { Story, Template } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import RangeSlider from "../../lib/svelte-components/RangeSlider.svelte";

  export const meta: Meta<RangeSlider> = {
    component: RangeSlider,
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
    argTypes: {
      min: {
        description: "Minimum value of the slider's range.",
        control: { type: "number" },
      },
      max: {
        description: "Maximum value of the slider's range.",
        control: { type: "number" },
      },
      step: {
        description: "Step offset.",
        control: { type: "number" },
      },
    },
  };
</script>

<Template let:args>
  <RangeSlider {...args}></RangeSlider>
</Template>

<Story
  name="Default"
  args={{ name: "example-data", min: 5, max: 15, step: 5 }}
/>
