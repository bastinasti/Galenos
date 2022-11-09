



/*validacion form*/
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input')




const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo (NOSE OCUPA por ahora 0 preguntas plis ta de emergencia grasia.)
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{8,16}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{8,9}$/ // 7 a 14 numeros.
  
}
const campos = {
  nombre: false,
  ap1: false,
  numero: false,
  email: false,
  password: false,
}

const validarFormulario = (e) => {
  switch(e.target.name){
    case "nombre":
      validarCampo(expresiones.nombre, e.target, 'nombre');
    break;
      

    case "apellido1":
      validarCampo(expresiones.nombre, e.target, 'ap1');
    break;

    case "numero":
      validarCampo(expresiones.telefono, e.target, 'numero');
    break;

    case "email":
      validarCampo(expresiones.correo, e.target, 'email');
    break;

    case "con1":
      validarCampo(expresiones.password, e.target, 'password');
      validarPassword2();
    break;

    case "con2":
      validarPassword2();
    break;

  }

}

const validarCampo = (expresion, input, campo) => {
  if(expresion.test(input.value)){
    document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
    document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
    document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
    document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
    document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
    campos[campo] = true;
  
  } else {
    document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
    document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
    document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
    document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
    document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
    campos[campo] = false;
  }
}

const validarPassword2 = () => {
  const inputCon1 = document.getElementById('con1');
  const inputCon2 = document.getElementById('con2');

  if(inputCon1.value !== inputCon2.value){
    document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
    document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
    document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
    document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
    document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
    campos['password'] = false;
  } else {
    document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
    document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
    document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
    document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
    document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
    campos['password'] = true;
  }
}

inputs.forEach((input) => {
  input.addEventListener('keyup', validarFormulario);
  input.addEventListener('blur', validarFormulario);
});


formulario.addEventListener('submit', (e) => {
  


  const terminos = document.getElementById('terminos');
  if(campos.nombre && campos.ap1 && campos.email && campos.password && terminos.checked ){
    formulario();

    document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
    setTimeout(() => {
      document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
    }, 5000)
    


    document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
      icono.classList.remove('formulario__grupo-correcto');
    })
  } else {
    document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
  }
});


