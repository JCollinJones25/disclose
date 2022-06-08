console.log("linked to index.js");

// Mapbox API

const $lat = $('.lat')
const $lng = $('.lng')
const $name = $('.name')
console.log($lat, $lng)
console.log($name[0].innerText, $lat[0].innerText, $lng[0].innerText)



const map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/satellite-streets-v11",
  center: [-84.5, 30],
  zoom: 2,
});

map.scrollZoom.enable({around: 'right'});
map.addControl(new mapboxgl.NavigationControl());


for (let i = 0; i < $lat.length; i++){
  for (let j = 0; j < $lng.length; j++){
  console.log($lat[i].innerText)
  const marker1 = new mapboxgl.Marker({color: 'purple'})
  .setLngLat([$lng[i].innerText, $lat[j].innerText])
  .addTo(map);
  }
}

for (const feature of geojson.features) {
  // create a HTML element for each feature
  const el = document.createElement("div");
  el.className = "marker";

  // make a marker for each feature and add to the map
  new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates).addTo(map);
}

