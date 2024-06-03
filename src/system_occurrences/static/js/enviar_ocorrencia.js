$(function () {
  $(".errorlist").addClass("text-danger");

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

    const map = L.map("map").setView(latlng, 12);

    L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
      maxZoom: 19,
      attribution:
        '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);

    var marker = null;

    if ($("#invalidForm").attr("value")) {
      marker = L.marker(JSON.parse($("#id_localizacao").html()));
      marker.addTo(map).on("click", () => {
        modalForm.show();
      });
    }

    function onMapClick(e) {
      if (marker) {
        
        marker.setLatLng(e.latlng);

      } else {

        marker = L.marker(e.latlng);

        marker.addTo(map).on("click", () => {
          modalForm.show();
        }).bindPopup('Clique em mim para continuar!').openPopup().unbindPopup();
      }

      map.flyTo(e.latlng, 19);

      $("#id_localizacao").html(JSON.stringify(e.latlng));
    }

    map.on("click", onMapClick);
  }

  createMap();

  if ($("#invalidForm").attr("value"))
    modalForm.show();
  else
    modalInstrucoes.show();

  const form = document.querySelector('form');

  form.addEventListener('submit', (event) => {
    $(".errorlist").html("");

    var isValid = true;

    for (let i = 0; i < form.length; i++)
      $(form[i]).removeClass("is-invalid is-valid");

    for (let i = 0; i < form.length; i++) {

      var id = $(form[i]).attr("id");

      if (id && id.includes("id") && !id.includes("img")) {

        if (!form[i].value) {
          $(form[i]).addClass("is-invalid");
          isValid = false;
        } else
          $(form[i]).addClass("is-valid");
      }

      else
        $(form[i]).addClass("is-valid");
    }


    if (isValid) {
      form.submit();
      return;
    } else {
      event.preventDefault();
      event.stopPropagation();
    }
  });
});
