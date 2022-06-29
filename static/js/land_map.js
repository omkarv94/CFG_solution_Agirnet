let drewmap;
let flag = 0;

function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: { lat: 23.004189, lng: 78.2214453 },
        mapTypeId: "terrain",
    });
    let land_points = [];
    map.addListener("click", (mapsMouseEvent) => {
        console.log(land_points.length);
        if (flag == 1)
            drewmap.setMap(null);
        land_points.push(mapsMouseEvent.latLng.toJSON());
        if (land_points.length > 2) {
            for (let i = 0; i < land_points.length; ++i)
                console.log(JSON.stringify(land_points[i]));
            drewmap = drawOnMap(map, land_points);
            flag = 1;
        }
        else {
            for (let i = 0; i < land_points.length; ++i)
                console.log(JSON.stringify(land_points[i]));
        }
    });
}

function drawOnMap(map, land_points) {
    // Construct the polygon
    const landMap = new google.maps.Polygon({
        paths: land_points,
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
    });
    landMap.setMap(map);
    return landMap;
}
window.initMap = initMap;
export {};