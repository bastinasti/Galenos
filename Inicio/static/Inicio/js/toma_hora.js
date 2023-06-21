$(document).ready(function() {
  const especialidadSelect = document.getElementById("especialidadSelect");
  const medicoSelect = document.getElementById("medicoSelect");

  especialidadSelect.addEventListener("change", function() {
    const especialidadValue = especialidadSelect.value;

    medicoSelect.innerHTML = '<option value="">Selecionar medico</option>';

    if (especialidadValue !== "") {
      $.ajax({
        url: "/obtener_medicos/",
        type: "GET",
        data: {
          especialidad: especialidadValue
        },
        success: function(response) {
          for (let i = 0; i < response.medicos.length; i++) {
            const medico = response.medicos[i];
            const option = document.createElement("option");
            option.value = medico.idMedico;
            option.textContent = medico.idUsuario.nombre;
            medicoSelect.appendChild(option);
          }
        },
        error: function(error) {
          console.log(error);
        }
      });
    }
  });
});