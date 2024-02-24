<script lang="ts" context="module">
  import { Story, Template } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import Autocomplete from "../../lib/svelte-components/Autocomplete.svelte";

  export const meta: Meta<Autocomplete> = {
    component: Autocomplete,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": ["H", "Li", "Ca"],
            },
          },
        },
      },
    },
    argTypes: {
      options: {
        description: "Array of objects representing available options.",
        control: { type: "array" },
      },
    },
  };
</script>

<Template let:args>
  <Autocomplete {...args}></Autocomplete>
</Template>

<Story
  name="Default"
  args={{
    name: "example-data",
    options: [
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
