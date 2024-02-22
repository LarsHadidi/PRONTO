<script lang="ts" context="module">
  import { Story } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import TextInput from '../../lib/svelte-components/TextInput.svelte';

  export const meta: Meta<TextInput> = {
    component: TextInput,
    tags: ['autodocs'],
    parameters: {
      fetchMock: { },
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              'example-data': "Example Text"
            }
          }
        }
      }
    }
  };
</script>

<Story name="Default">
  <TextInput name="example-data"></TextInput>
</Story>