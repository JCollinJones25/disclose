console.log("hello world from index.js");

// const URL = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAPS_API_KEY}`

function initMap() {
  const options = {
    zoom: 4,
    center: {
      lat: 35.56480,
      lng: -77.8583,
    },
  };
  const map = new google.maps.Map(document.getElementById("map"), options);
}

window.initMap = initMap;
