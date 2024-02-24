<script lang="ts" context="module">
  import { Story } from "@storybook/addon-svelte-csf";
  import type { Meta } from "@storybook/svelte";
  import Card from "../../lib/svelte-components/Card.svelte";

  export const meta: Meta<Card> = {
    component: Card,
    tags: ["autodocs"],
    parameters: {
      fetchMock: {},
    },
  };
</script>

<Story name="Default">
  <Card>
    <b>Card</b>
    <br />
    I am a card
  </Card>
</Story>
