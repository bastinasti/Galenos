// Obtener referencia a los elementos select
const especialidadSelect = document.getElementById("select1");
const medicoSelect = document.getElementById("select2");

// Escuchar el evento de cambio en el select de especialidad
especialidadSelect.addEventListener("change", function () {
  // Obtener el valor seleccionado de la especialidad
  const especialidadValue = especialidadSelect.value;

  // Limpiar todas las opciones del select de médico
  medicoSelect.innerHTML = '<option value="">Seleccionar</option>';

  // Verificar la especialidad seleccionada y agregar las opciones correspondientes
  if (especialidadValue === "1") {
    // Agregar la opción de "Manuel Reyes" al select de médico
    const option = document.createElement("option");
    const option2 = document.createElement("option");
    const option3 = document.createElement("option");
    option.value = "1";
    option2.value = "2";
    option3.value = "3";
    option.textContent = "Claudio Opazo";
    option2.textContent = "Jorge Zabaleta";
    option3.textContent = "Pancho Sabedra";
    medicoSelect.appendChild(option);
    medicoSelect.appendChild(option2);
    medicoSelect.appendChild(option3);
  } else if (especialidadValue === "2") {
    // Agregar la opción de "Maria Gonzales" al select de médico
    const option = document.createElement("option");
    const option3 = document.createElement("option");
    const option4 = document.createElement("option");
    option.value = "2";
    option3.value = "3";
    option4.value = "4";
    option.textContent = "Maria Gonzales";
    option3.textContent = "Alexis Sanchez";
    option4.textContent = "Ben Brereton";
    medicoSelect.appendChild(option);
    medicoSelect.appendChild(option3);
    medicoSelect.appendChild(option4);
  } else if (especialidadValue === "3") {
    // Agregar la opción de "Leonardo Dicaprio" al select de médico
    const option = document.createElement("option");
    const option4 = document.createElement("option");
    const option5 = document.createElement("option");
    option.value = "3";
    option4.value = "4";
    option5.value = "5";
    option.textContent = "Leonardo Dicaprio";
    option4.textContent = "Nayaret Albornoz";
    option5.textContent = "Victor Rosendo";
    medicoSelect.appendChild(option);
    medicoSelect.appendChild(option4);
    medicoSelect.appendChild(option5);
  }
});