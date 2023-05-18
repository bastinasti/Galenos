// Supongamos que tienes un array de objetos con la información de los pacientes
var pacientes = [
    { hora: '09:00', doctor: 'Dr. Pérez', paciente: 'Juan Pérez' },
    { hora: '10:30', doctor: 'Dr. Gómez', paciente: 'María Gómez' },
    { hora: '11:45', doctor: 'Dra. Rodríguez', paciente: 'Ana Rodríguez' },
    // ...
  ];
  
  // Función para crear las filas del visualizador de pacientes
  function crearFilasPacientes() {
    var visualizador = document.getElementById('visualizador');
  
    // Limpiar contenido existente
    visualizador.innerHTML = '';
  
    // Crear una fila por cada paciente en el array
    pacientes.forEach(function(paciente) {
      var fila = document.createElement('div');
      fila.className = 'fila';
  
      // Crear celdas para cada columna y asignarles el contenido del paciente
      var horaCelda = document.createElement('div');
      horaCelda.className = 'columna';
      horaCelda.textContent = paciente.hora;
      fila.appendChild(horaCelda);
  
      var doctorCelda = document.createElement('div');
      doctorCelda.className = 'columna';
      doctorCelda.textContent = paciente.doctor;
      fila.appendChild(doctorCelda);
  
      var pacienteCelda = document.createElement('div');
      pacienteCelda.className = 'columna';
      pacienteCelda.textContent = paciente.paciente;
      fila.appendChild(pacienteCelda);
  
      // Agregar la fila al visualizador
      visualizador.appendChild(fila);
    });
  }
  
  // Llamar a la función para mostrar los pacientes al cargar la página
  crearFilasPacientes();