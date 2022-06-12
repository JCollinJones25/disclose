
// jQuery used for map data

const $lat = $('.lat')
const $lng = $('.lng')
$lat.hide() 
$lng.hide() 
const $hideForm = $('.hide-form')
$hideForm.hide()
const $name = $('.name')
const $cityState = $('.city-state')

// Mapbox API

const map = new mapboxgl.Map({
  container: "map",
  style: "mapbox://styles/jcollinjones25/cl4ara6dv008z14nxivuupc01",
  center: [-84.5, 30],
  zoom: 3,
});

map.scrollZoom.enable({around: 'mouse'});
map.addControl(new mapboxgl.NavigationControl());
map.boxZoom.enable();


for (let i = 0; i < $lat.length; i++){

  const popup = new mapboxgl.Popup({ offset: 25 }).setHTML($name[i].innerText);
  const el = document.createElement('div');
  el.id = 'marker';

  const marker = new mapboxgl.Marker({color: '#5fa7ef'})
  .setLngLat([$lng[i].innerText, $lat[i].innerText])
  .setPopup(popup) 
  .addTo(map);

  }
