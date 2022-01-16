function createMap(accidents) {

    // Create the tile layer that will be the background of our map.
    var streetmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });
  
    // Create a baseMaps object to hold the streetmap layer.
    var baseMaps = {
      "Street Map": streetmap
    };
  
    // Create an overlayMaps object to hold the accidents layer.
    var overlayMaps = {
      "Accident Locations": accidents
    };
  
    // Create the map object with options.
    var map = L.map("map-id", {
      center: [40.73, -74.0059],
      zoom: 12,
      layers: [streetmap, accidents]
    });
  
    // Create a layer control, and pass it baseMaps and overlayMaps. Add the layer control to the map.
    L.control.layers(baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(map);
  }
  
  function createMarkers(metaData) {
  
    // Pull the "stations" property from response.data.
    // var stations = response.data.stations;
  
    // Initialize an array to hold bike markers.
    var accidentMarkers = [];
  
    // Loop through the accident array.
    for (var i = 0; i < metaData.length; i++) {
      var accident = metaData[i];
  
      // For each accident, create a marker, and bind a popup with the city, doa_status, manner of collision, route
      var accidentMarker = L.marker([accident.lat, accident.lon])
        .bindPopup("<h5>City: " + accident.city + "</h5><h5>Outcome: " + accident.doa_status + "</h5><h5>Manner of Collision: " + accident.man_collision + "</h5><h5>Route: " + accident.route);
  
      // Add the marker to the bikeMarkers array.
      accidentMarkers.push(accidentMarker);
    }
  
    // Create a layer group that's made from the bike markers array, and pass it to the createMap function.
    createMap(L.layerGroup(accidentMarkers));
  }
  
  // Perform an API call to the Citi Bike API to get the station information. Call createMarkers when it completes.
  
  d3.json("http://127.0.0.1:5000/accident-data/?index=True").then(createMarkers);

  // d3.json("http://127.0.0.1:5000/accident-data/?index=true").then(createMarkers);