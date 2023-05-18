// Obtener referencias a los elementos select
const select1 = document.getElementById('select1');
const select2 = document.getElementById('select2');

// Definir los datos para rellenar el segundo select
const opcionesSelect2 = {
  opcion1: ["Opción 1.1", "Opción 1.2", "Opción 1.3"],
  opcion2: ["Opción 2.1", "Opción 2.2", "Opción 2.3"],
  opcion3: ["Opción 3.1", "Opción 3.2", "Opción 3.3"]
};

// Función para actualizar el contenido del segundo select
function actualizarSelect2() {
  // Obtener el valor seleccionado del primer select
  const valorSelect1 = select1.value;

  // Limpiar el contenido actual del segundo select
  select2.innerHTML = '';

  // Obtener las opciones correspondientes al valor seleccionado en el primer select
  const opciones = opcionesSelect2[valorSelect1];

  // Crear y añadir las opciones al segundo select
  opciones.forEach(opcion => {
    const option = document.createElement('option');
    option.textContent = opcion;
    select2.appendChild(option);
  });
}

// Escuchar los cambios en el primer select
select1.addEventListener('change', actualizarSelect2);

// Actualizar el contenido del segundo select al cargar la página
actualizarSelect2();