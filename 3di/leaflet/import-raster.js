// initalize leaflet map
var map = L.map('map').setView([52.55509172663781, 4.730346372352345], 14);

// add OpenStreetMap basemap
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);


// Get the checkboxes
var checkbox3di = document.getElementById('3di');
var checkboxRaster = document.getElementById('raster');


var imageOverlay = null
var rasterLayer = null

// Add event listener to check the state when the checkboxes change
checkbox3di.addEventListener('change', function () {
    if (checkbox3di.checked) {
        console.log('3Di Layer is checked');

        if (imageOverlay) {
            imageOverlay.setOpacity(0.5);
        }
    } else {
        if (imageOverlay) {
            imageOverlay.setOpacity(0);
        }
        console.log('3Di Layer is unchecked');
    }
});

checkboxRaster.addEventListener('change', function () {
    if (checkboxRaster.checked) {
        console.log('Raster is checked');
        if (rasterLayer) {
            rasterLayer.addTo(map);

            map.fitBounds(rasterLayer.getBounds());
        }

    } else {
        console.log('Raster is unchecked');
        if (rasterLayer) {
            map.removeLayer(rasterLayer);
        }

    }
});

document.getElementById("geotiff-file").addEventListener("change", function (event) {
    var file = event.target.files[0];
    console.log("file:", file);

    var reader = new FileReader();
    reader.readAsArrayBuffer(file);
    reader.onloadend = function () {
        var arrayBuffer = reader.result;
        parseGeoraster(arrayBuffer).then(georaster => {

            // GeoJSON data representing the bounding box
            var geojsonData = {
                type: 'Feature',
                properties: {},
                geometry: {
                    type: 'Polygon',
                    coordinates: [
                        [
                            [4.716376372352345, 52.54509172663781],
                            [4.716376372352345, 52.58032420234745],
                            [4.749301792390481, 52.58032420234745],
                            [4.749301792390481, 52.54509172663781],
                            [4.716376372352345, 52.54509172663781]
                        ]
                    ]
                }
            };

            // URL to the image
            var imageUrl = '../3di.png';

            // Create a GeoJSON layer and add it to the map
            // L.geoJSON(geojsonData).addTo(map);

            // Extract polygon bounds
            var bounds = L.geoJSON(geojsonData).getBounds();

            // Add the image overlay to the map within the polygon bounds
            imageOverlay = L.imageOverlay(imageUrl, bounds).addTo(map);
            imageOverlay.setOpacity(0.5);



            //-------- RASTER
            console.log("georaster:", georaster);
            /*
                GeoRasterLayer is an extension of GridLayer,
                which means can use GridLayer options like opacity.

                Just make sure to include the georaster option!

                http://leafletjs.com/reference-1.2.0.html#gridlayer
            */
            rasterLayer = new GeoRasterLayer({
                georaster: georaster,
                opacity: 0.5,
                resolution: 256,
                // pixelValuesToColorFn: (value) => {
                //     if (0 <= value && value <= 50) {
                //         return "#00FF66"
                //     }

                //     if (50 < value && value <= 100) {
                //         return "#FFB300"
                //     }

                //     if (100 < value && value <= 150) {
                //         return "#B300FF"
                //     }

                //     if (150 < value && value <= 200) {
                //         return "#FF00FF"
                //     }

                //     if (200 < value && value <= 250) {
                //         return "#091EE1"
                //     }

                //     if (250 < value && value <= 300) {
                //         return "#00FFF7"
                //     }

                //     if (300 < value && value <= 350) {
                //         return "#A56C4A"
                //     }

                //     if (350 < value && value <= 400) {
                //         return "#E5DF32"
                //     }

                //     return "#000000"
                // }
            });
            console.log("layer:", rasterLayer);
            rasterLayer.addTo(map);

            map.fitBounds(rasterLayer.getBounds());
            document.getElementById("overlay").style.display = "none";
        });
    };
});