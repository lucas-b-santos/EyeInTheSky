$(function () {

    let getLocation = new Promise((resolve, reject) => {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
          resolve([position.coords.latitude, position.coords.longitude]);
        });
      } else {
        console.log("Geolocation is not supported by this browser.");
        resolve([-24.952289, -53.466682]);
      }
    });
  
    var modalInstrucoes = new bootstrap.Modal(
      document.getElementById("modalInstrucoes"),
      {
        keyboard: false,
      }
    );
  
    var modalForm = new bootstrap.Modal(document.getElementById("modalForm"), {
      keyboard: false,
    });
  
    async function createMap() {
      let latlng = await getLocation;
  
      const map = L.map("map").setView(latlng, 18);
  
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
        maxZoom: 19,
        attribution:
          '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
      }).addTo(map);
  
      var marker = null;
  
      function onMapClick(e) {
        if (marker) {
          marker.setLatLng(e.latlng)
        } else {
          marker = L.marker(e.latlng);
          marker.addTo(map).on("click", () => {
              modalForm.show();
            }).bindPopup('Clique em mim para continuar!').openPopup().unbindPopup();
        }
  
        map.flyTo(e.latlng, 19);
      }
  
      map.on("click", onMapClick);
    }
  
    createMap();
  
    modalInstrucoes.show();
  });
  