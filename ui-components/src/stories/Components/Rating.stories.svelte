<script lang="ts" context="module">
  import { Story, Template } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import Rating from "../../lib/svelte-components/Rating.svelte";

  export const meta: Meta<Rating> = {
    component: Rating,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              "example-data": "5",
            },
          },
        },
      },
    },
    argTypes: {
      max: {
        description: "Maximum value.",
        control: { type: "number" },
      },
    },
  };
</script>

<Template let:args>
  <Rating {...args}></Rating>
</Template>

<Story name="Default" args={{ name: "example-data", max: 5 }} />
