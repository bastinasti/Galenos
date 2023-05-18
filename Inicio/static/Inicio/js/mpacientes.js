$(document).ready(function() {
    // Obtener datos de la base de datos mediante AJAX
    $.ajax({
      url: '/obtener_pacientes/',  // el url para obtener el paciente (nose cual es)
      type: 'GET',
      dataType: 'json',
      success: function(data) {
        // Llamar a la función para mostrar los pacientes con los datos obtenidos
        crearFilasPacientes(data);
      },
      error: function() {
        alert('Error al obtener los pacientes.');
      }
    });
  });
  
  function crearFilasPacientes(pacientes) {
    var tablaPacientes = document.getElementById('tablaPacientes');
  
    // Limpiar contenido existente
    tablaPacientes.innerHTML = '';
  
    // Obtener la hora actual del computador
    var horaActual = new Date();
  
    // Crear una fila por cada paciente en el array
    pacientes.forEach(function(paciente) {
      // Convertir la hora de atención en un objeto Date
      var horaAtencion = new Date(paciente.hora);
  
      // Comparar la hora de atención con la hora actual + 5 horas
      var horaLimite = new Date();
      horaLimite.setHours(horaLimite.getHours() + 5);
  
      if (horaAtencion >= horaActual && horaAtencion <= horaLimite) {
        var fila = document.createElement('tr');
  
        // Crear celdas para cada columna y asignarles el contenido del paciente
        var horaCelda = document.createElement('td');
        horaCelda.textContent = paciente.hora;
        fila.appendChild(horaCelda);
  
        var doctorCelda = document.createElement('td');
        doctorCelda.textContent = paciente.doctor;
        fila.appendChild(doctorCelda);
  
        var pacienteCelda = document.createElement('td');
        pacienteCelda.textContent = paciente.paciente;
        fila.appendChild(pacienteCelda);
  
        // Agregar la fila a la tabla
        tablaPacientes.appendChild(fila);
      }
    });
  }
  
  // Llamar a la función para mostrar los pacientes al cargar la página
  crearFilasPacientes();