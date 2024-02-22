<script lang="ts" context="module">
  import { Story } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import Map from '../../lib/svelte-components/Map.svelte';

  export const meta: Meta<Map> = {
    component: Map,
    tags: ['autodocs'],
    parameters: {
      fetchMock: { },
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              'example-data': {
                'polylines': ["BG65rniDtszHG9FoB_YUrYAnGUvMoBrT3ITvHTjIAzFArOU3DA3DAzFT3DT_EnBzKT_EAjIUnBAzFoB7G8B7LgFvWkIvHwC7L4DjDU7G8B3S8B3SoBvHU7LA7LU3DUjNwCjrB0KjNkDnG8BzFoB_EoBjNkDnLkD_JwCjI8B3D8B3D8BrEwCrEwC7BwCvCoB7BA7BA7BT7B7BnB7BnB3DTrEUrEUjD8BvC8B7BkDzK4D_OoB_YoBvqBU3rBA_dA_dAvgBoBnsCAxE,BGg-_miD5x-HAxXoBj1BAzUUrYUzFoB_E8B_E8B3DkD_E0FnGwRrO8pBjcwWrOU3DoB7BoBTrEnQ7GrY7B3InB7GTrET7GnBUnBTnB7BTvCAvCU7B8BnBoBAoBU4D_J8BzFgFzP8B3D8BvCoBnBsEnB0FAoGU0KwCsT8BoGTgKvCsOnGkI_EwH_E4DjDgK3IgFzF4DnGgFrJwC_EoBvC4DvH8G7QsE7LgPzoBgF3NkDrJgK7foQ7zBgKnf4D_JkDvH4DvH8GvM8G_JgKnLopB4SwbkN8G4D0FsEgFgF8G4DwHkDkIToGrE0F_JwCzKAvMjDrOoBzoB"],
                 markers: [{"type":"Feature","geometry":{"type":"Point","coordinates":[-0.12462867304698788,51.50079091939711]}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-0.13033256727188167,51.4947804218879]}},{"type":"Feature","geometry":{"type":"Point","coordinates":[-0.14182012965768487,51.50166352684979]}}]
              }
            }
          }
        }
      }
    }
  };
</script>

<Story name="Default">
  <div class="h-96">
    <Map name="example-data"></Map>
  </div>
</Story>