<script lang="ts">
	import { page } from '$app/stores';
	import { decode } from '$lib/flex-polyline.js';

	export let name: string;
	export let initialLatitude: number = 51.5;
	export let initialLongitude: number = 0;
	export let initialZoom: number = 12;

	let polylines: string[] = $page.data?.[name]?.polylines ?? [];
	let markers: GeoJSON.Feature[] = $page.data?.[name]?.markers ?? [];

	function decodeMultiPolyline(multiPolyline: string) {
		return multiPolyline.split(",").map(decode).map((result) => result.polyline);
	}

	async function mount(node: HTMLElement): Promise<void>
	{
		const L = await import('leaflet');
		let map = L.map(node).setView([initialLatitude, initialLongitude], initialZoom);
		L.tileLayer(
			'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
			{
				maxZoom: 19,
				attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, &copy; <a href="http://cartodb.com/attributions">CartoDB</a>'
			})
		.addTo(map);
		if(polylines.length > 0 && markers.length > 0)
		{
			const segments = polylines.map((multiPolyline: string) => decodeMultiPolyline(multiPolyline)).flat();
			const polylineLayer = L.polyline(segments, { color: "cornflowerblue" }).addTo(map);
			const markerLayer = L.geoJSON(markers).addTo(map);
			const polylinesBounds = polylineLayer.getBounds();
			const markersBounds = markerLayer.getBounds();
			const bounds = L.latLngBounds(
				[
					polylinesBounds.getNorthWest(),
					polylinesBounds.getNorthEast(),
					polylinesBounds.getSouthWest(),
					polylinesBounds.getSouthEast(),
					markersBounds.getNorthWest(),
					markersBounds.getNorthEast(),
					markersBounds.getSouthWest(),
				markersBounds.getSouthEast()
				]
			);
			map.fitBounds(bounds);
		}
		else if(polylines.length > 0)
		{
			const segments = polylines.map((multiPolyline) => decodeMultiPolyline(multiPolyline)).flat();
			const polylineLayer = L.polyline(segments, { color: "cornflowerblue" }).addTo(map);
			map.fitBounds(polylineLayer.getBounds());
		}
		else if(markers.length > 0)
		{
			const markerLayer = L.geoJSON(markers).addTo(map);
			map.fitBounds(markerLayer.getBounds());
		}
		else
		{
			map.setView([initialLatitude, initialLongitude], initialZoom);
		}
	}
</script>


<div {name} use:mount class='h-full'></div>

<style>
	@import url('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css');
</style>