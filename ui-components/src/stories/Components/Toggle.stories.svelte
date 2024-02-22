<script lang="ts" context="module">
  import { Story, Template } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import Toggle from '../../lib/svelte-components/Toggle.svelte';

  export const meta: Meta<Toggle> = {
    component: Toggle,
    tags: ['autodocs'],
    parameters: {
      fetchMock: { },
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              'example-data': true
            }
          }
        }
      }
    },
    argTypes: {
      label: {
        description: "Label for the Toggle to be displayed.",
        control: { type: 'text' }
      }
    }
  };
</script>

<Template let:args>
  <Toggle {...args}></Toggle>
</Template>

<Story name="Default" args={ {name: "example-data", label: "Light-Switch"} }/>