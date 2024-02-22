<script lang="ts" context="module">
  import { Story, Template } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import Ticket from '../../lib/svelte-components/Ticket.svelte';

  export const meta: Meta<Ticket> = {
    component: Ticket,
    tags: ['autodocs'],
    parameters: {
      fetchMock: { },
      sveltekit_experimental: {
        stores: {
          page: {
            data: {
              'example-data': {
                name: 'Pronto Dinner',
                date: new Date(),
                venue: 'London',
                ticketid: 'A1B2C3'
              }
            }
          }
        }
      }
    },
    argTypes: {
      eventName: {
        description: "Name of the event.",
        control: { type: 'text' }
      },
      eventDate: {
        description: "Date of the event.",
        control: { type: 'date' }
      },
      eventVenue: {
        description: "Location of the event.",
        control: { type: 'text' }
      },
      ticketId: {
        description: "Unique identifier of the ticket.",
        control: { type: 'text' }
      }
    }
  };
</script>

<Template let:args>
  <Ticket {...args}></Ticket>
</Template>

<Story name="Default" args={ {name: "example-data"} }/>