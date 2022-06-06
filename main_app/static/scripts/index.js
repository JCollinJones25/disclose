console.log("hello world from index.js");


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
