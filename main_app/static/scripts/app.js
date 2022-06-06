console.log("hello world from app.js");

function initMap() {
  const options = {
    zoom: 4,
    center: {
      lat: 37.8393,
      lng: 86.27,
    },
  };
  const map = new google.maps.Map(document.getElementById("map"), options);
}
initMap();
