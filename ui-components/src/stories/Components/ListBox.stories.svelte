<script lang="ts" context="module">
  import { Story, Template } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import ListBox from "../../lib/svelte-components/ListBox.svelte";

  export const meta: Meta<ListBox> = {
    component: ListBox,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": ["H"],
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
  <ListBox {...args}></ListBox>
</Template>

<Story
  name="Default"
  args={{
    name: "example-data",
    multiple: true,
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
