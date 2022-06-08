console.log("linked to index.js");

// Mapbox API

const $lat = $('.lat')
const $lng = $('.lng')
const $name = $('.name')

console.log($lat, $lng)

const map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/satellite-streets-v11",
  center: [-84.5, 30],
  zoom: 2,
});

map.scrollZoom.enable({around: 'right'});
map.addControl(new mapboxgl.NavigationControl());


for (let i = 0; i < $lat.length; i++){
  console.log(i +1)
  console.log($name[i].innerText)
  console.log($lat[i].innerText)
  console.log($lng[i].innerText)
  console.log('-----------')
  const marker = new mapboxgl.Marker({color: 'purple'})
  .setLngLat([$lng[i].innerText, $lat[i].innerText])
  .addTo(map);
  marker.setPitchAlignment('map');
  }



/*

TODO:   Wednesday

Pop ups

data entry

style home and list template ???
  - overflow scroll window on left of map with locations?

*/

