<script lang="ts" context="module">
  import { Story } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import DatePicker from '../../lib/svelte-components/DatePicker.svelte';

  export const meta: Meta<DatePicker> = {
    component: DatePicker,
    tags: ['autodocs'],
    parameters: {
      fetchMock: { },
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              'example-data': new Date()
            }
          }
        }
      }
    }
  };
</script>

<Story name="Default">
  <DatePicker name="example-data"></DatePicker>
</Story>