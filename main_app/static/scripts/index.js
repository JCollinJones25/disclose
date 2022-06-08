console.log("linked to index.js");

// Mapbox API

const $lat = $('.lat')
const $lng = $('.lng')
$lat.hide() 
$lng.hide() 
const $name = $('.name')

console.log($lat, $lng)

const map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/mapbox/satellite-streets-v11",
  center: [-84.5, 30],
  zoom: 2,
});

map.scrollZoom.enable({around: 'mouse'});
map.addControl(new mapboxgl.NavigationControl());
map.boxZoom.enable();



for (let i = 0; i < $lat.length; i++){
  console.log(i +1)
  console.log($name[i].innerText)
  console.log($lat[i].innerText)
  console.log($lng[i].innerText)
  console.log('-----------')
  const popup = new mapboxgl.Popup({ offset: 25 }).setText(
    $name[i].innerText
    );
     
  const el = document.createElement('div');
  el.id = 'marker';
  const marker = new mapboxgl.Marker({color: 'purple'})
  .setLngLat([$lng[i].innerText, $lat[i].innerText])
  .setPopup(popup) 
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

