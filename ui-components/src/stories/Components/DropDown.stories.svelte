<script lang="ts" context="module">
  import { Story, Template } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import DropDown from "../../lib/svelte-components/DropDown.svelte";

  export const meta: Meta<DropDown> = {
    component: DropDown,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": "Li",
            },
          },
        },
      },
    },
    argTypes: {
      items: {
        description: "Array of objects representing available items.",
        control: { type: "array" },
      },
    },
  };
</script>

<Template let:args>
  <DropDown {...args}></DropDown>
</Template>

<Story
  name="Default"
  args={{
    name: "example-data",
    items: [
      { label: "Hydrogen", value: "H" },
      { label: "Helium", value: "He" },
      { label: "Lithium", value: "Li" },
      { label: "Beryllium", value: "Be" },
      { label: "Sodium", value: "Na" },
      { label: "Magnesium", value: "Mg" },
      { label: "Potassium", value: "K" },
      { label: "Calcium", value: "Ca" },
      { label: "Rubidium", value: "Rb" },
      { label: "Strontium", value: "Sr" },
      { label: "Cesium", value: "Cs" },
      { label: "Barium", value: "Ba" },
      { label: "Francium", value: "Fr" },
      { label: "Radium", value: "Ra" },
    ],
  }}
/>
