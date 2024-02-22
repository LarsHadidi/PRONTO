<script lang="ts">
	export let title: string;
	export let colorLeft: string = '#000';
	export let colorRight: string = '#000';
</script>

<div class="heading font-extrabold" style="--color_left: {colorLeft}; --color_right: {colorRight};">{@html title}</div>

<style>
	.heading {
	  padding: 0.5em;
	  font-size: 2em;
	  background: -webkit-linear-gradient(left, var(--color_left), var(--color_right));
	  background-clip: text;
	  -webkit-background-clip: text;
	  -webkit-text-fill-color: transparent;
	}
</style>