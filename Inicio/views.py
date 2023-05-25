from datetime import date, datetime
from django.shortcuts import render, redirect
from .models import Medico, Persona, Usuario, TipoUsuario, Paciente, Agenda
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.


def inicio(request):
    return render(request, "Inicio/DelanekoShop.html")


def registro(request):
    return render(request, "Inicio/Registro/registro.html")


def registro2(request):
    return render(request, "Inicio/Registro2/registro2.html")


def registroUsuario(request):
    return render(request, "Inicio/registroUsuario/registroUsuario.html")


def iniciosesion(request):
    return render(request, "Inicio/InicioSesion/sesion.html")

def monitoPaciente(request):
    return render(request, "Inicio/MonitorPaciente/visualPaciente.html")

# Registrar Usuario


def registrar_usuario(request):
    repClave = request.POST["repClave"]

    nombre = request.POST["nombre"]
    rut = request.POST["rut"]
    clave = request.POST["clave"]
    correo = request.POST["correo"]

    if clave != repClave:
        messages.success(request, "Las contraseñas deben coincidir")
        return redirect("inicio")

    else:
        tipousuario = TipoUsuario.objects.get(idTipoUsuario=2)
        Usuario.objects.create(
            nombre=nombre,
            rut=rut,
            clave=clave,
            correo=correo,
            idTipoUsuario=tipousuario,
        )
        return redirect("iniciosesion")


def registrar_paciente(request):
    rut1 = request.POST["rut1"]
    prevision1 = request.POST["prevision1"]
    especialidad1 = request.POST["especialidad1"]
    medico1 = request.POST["medico1"]
    fecha = request.POST["inputFecha"]

    # * OBTENER FECHA ACTUAL
    fecha_actual = date.today()

    # Convertir la fecha ingresada en el formulario a objeto de fecha
    fecha_ingresada = date.fromisoformat(fecha)

    if fecha_ingresada >= fecha_actual:
        Paciente.objects.create(
            rutPaciente=rut1,
            prevision=prevision1,
            especialidad=especialidad1,
            nomMedico=medico1,
        )
    else:
        # La fecha ingresada es menor que la fecha actual
        # Maneja el error o muestra un mensaje al usuario
        messages.error(request, "La fecha ingresa ya paso segun calendario, porfavor seleccione el dia de hoy u otra proxima")

    return redirect("registro")


def iniciar_sesion(request):
    correo  =request.POST["correoinicio"]
    clave = request.POST["contrainicio"]

    try:
        usuario = Usuario.objects.get(correo=correo, clave=clave)
    
        if clave == usuario.clave:
            print('si entro')
            tipo = TipoUsuario.objects.get(idTipoUsuario=usuario.idTipoUsuario)
            print(tipo)

            return redirect('inicio')
        else:
            messages.error(request, "Correo o Contraseña incorrecta..")
            print('no entro')
    except ObjectDoesNotExist:
        messages.error(request, "Correo o Contraseña incorrecta...")
    
    return redirect('iniciosesion')

# def validarinicio(request):
#     correo = request.POST['email']
#     password = request.POST['password']

#     try:
#         u = usuario.objects.get(correo=correo, contrasena=password)
#         if not u:
#             return redirect('/Principal/inicio-sesi.html')
        
#         else:
#             rol = usuario_has_tipo.objects.get(id_usuario = u.id_usuario)
#             request.session['correo'] = u.correo

#             r = tipo_usuario.objects.get(nom_tipo = rol.id_tipo)

#             request.session['alfin'] = r.nom_tipo
#             request.session['nombre'] = u.nombres

#             messages.success(request, 'Bienvenido ' + u.nombres)
#             return redirect('inicio')
#     except:
#         messages.error(request, 'Usuario o contraseña incorrectos')
#         return redirect('inicio_sesi')

def salir(request):
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente")
    return redirect("inicio")


# Agregar horas medicas


def crear_agenda(request):
    medicos = Medico.objects.all()
    personas = []

    for m in medicos:
        persona = Persona.objects.get(rutPersona=m.rutMedico)
        personas.append(persona)

    contexto = {"personas": personas}
    return render(request, "Inicio/crear_agenda.html", contexto)


def agregar_dia(request):
    rutMedico = request.POST["inputMedico"]
    fecha = request.POST["inputFecha"]
    hora = request.POST['inputHora']

    # * OBTENER FECHA ACTUAL
    fecha_actual = date.today()

    fecha2 = datetime.strptime(fecha, "%Y-%m-%d")
    # Convertir la fecha ingresada en el formulario a objeto de fecha
    fecha_ingresada = date.fromisoformat(fecha)

    if fecha_ingresada >= fecha_actual:
        # La fecha ingresada es igual o mayor que la fecha actual
        # Realiza la lógica adicional aquí
        fecha_formateada = fecha2.strftime("%d/%m/%y")

        existeeee = Agenda.objects.filter(rutPersona = rutMedico, fechaDisp = fecha_formateada, horaDisp = hora)

        if existeeee:
            messages.error(request, "la fecha y hora que se quiere registrar ya existe")
        else:
            Agenda.objects.create(rutPersona = rutMedico, fechaDisp = fecha_formateada, horaDisp = hora, estado = 'Disponible')
            messages.success(request, "Se genero la fecha con exito")
    else:
        # La fecha ingresada es menor que la fecha actual
        # Maneja el error o muestra un mensaje al usuario
        messages.error(request, "La fecha ingresa ya paso segun calendario, porfavor seleccione el dia de hoy u otra proxima")

    return redirect('crear_agenda')
