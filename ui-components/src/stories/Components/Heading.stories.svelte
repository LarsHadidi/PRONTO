<script lang="ts" context="module">
  import { Story, Template } from '@storybook/addon-svelte-csf';
  import type { Meta } from '@storybook/svelte';
  import Heading from '../../lib/svelte-components/Heading.svelte';

  export const meta: Meta<Heading> = {
    component: Heading,
    tags: ['autodocs'],
    parameters: {
      fetchMock: { }
    },
    argTypes: {
      title: {
        description: "The text to be rendered.",
        control: { type: 'text' }
      },
      colorLeft: {
        description: "Color on the left side of the gradient.",
        control: { type: 'color' }
      },
      colorRight: {
        description: "Color on the right side of the gradient.",
        control: { type: 'color' }
      }
    }
  };
</script>

<Template let:args>
  <Heading {...args}></Heading>
</Template>

<Story name="Default" args={
  {title: 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr', colorLeft: '#A8BEF1',colorRight: '#47947D'} 
}/>