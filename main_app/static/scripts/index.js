
// Mapbox API

const $lat = $('.lat')
const $lng = $('.lng')
const $img = $('.home-img')
$lat.hide() 
$lng.hide() 
$img.hide() 
const $name = $('.name')
const $cityState = $('.city-state')


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
  console.log($img[i].src)
  console.log('-----------')

  const popup = new mapboxgl.Popup({ offset: 25 }).setHTML($name[i].innerText, $img[i].src);
  const el = document.createElement('div');
  el.id = 'marker';

  const marker = new mapboxgl.Marker({color: 'rgb(0, 148, 115)'})
  .setLngLat([$lng[i].innerText, $lat[i].innerText])
  .setPopup(popup) 
  .addTo(map);

  }
  
  
  


