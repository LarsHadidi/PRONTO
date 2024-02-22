<script lang="ts" context="module">
  import { Story } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import GeoAddress from '../../lib/svelte-components/GeoAddress.svelte';

  export const meta: Meta<GeoAddress> = {
    component: GeoAddress,
    tags: ['autodocs'],
    parameters: {
      fetchMock: {
        mocks: [
          {
            matcher: {
              name: 'geocoder',
              url: 'path:/api/address/autocomplete',
              method: 'GET'
            },
            response: {
              status: 200,
              body: {
                items: [
                  {title: 'London SW1A 0AA, UK'},
                  {title: 'London SW1B 0AA, UK'},
                  {title: 'London SW1C 0AA, UK'}
                ]
              }
            }
          }
        ]
      },
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              'example-data': 'London'
            }          
          }
        }
      }
    }
  };
</script>

<Story name="Default">
  <GeoAddress name="example-data"></GeoAddress>
</Story>