from datetime import date, datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Medico, MedicoEspec, Usuario, TipoUsuario, Paciente, Agenda, Prevision, Especialidad, horaS
from django.contrib import messages
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password, make_password


#* --------------------------------------------------------------------- ---- Paginas ---- ---------------------------------------------------------------------


def inicio(request):
    return render(request, "Inicio/DelanekoShop.html")


def obtener_medicos(request):
    especialidad_id = request.GET.get('especialidad', None)
    medicos = Medico.objects.filter(medicoespec__idEspe_id=especialidad_id)
    
    medicos_data = [{'id': medico.idMedico, 'nombre': medico.idUsuario.nombre} for medico in medicos]
    return JsonResponse({'medicos': medicos_data})

def especialidad(request):
    espe = Especialidad.objects.all()
    medicos = Medico.objects.all()
    espeM = MedicoEspec.objects.all()
    context = {'espe' : espe, 'medicos' : medicos, 'espeM' : espeM}
    return render(request, "Inicio/Registro/especialidades.html",context)


def registro2(request):
    return render(request, "Inicio/Registro2/registro2.html")


def registroUsuario(request):
    return render(request, "Inicio/registroUsuario/registroUsuario.html")


def iniciosesion(request):
    return render(request, "Inicio/InicioSesion/sesion.html")

def monitoPaciente(request):
    pac = Paciente.objects.all()
    contexto = {'pac': pac }
    return render(request, "Inicio/MonitorPaciente/monitor.html", contexto)

#* --------------------------------------------------------------------- ---- Registrar paciente ---- ---------------------------------------------------------------------

def registrar_usuario(request):
    repClave = request.POST["repClave"]

    nombre = request.POST["nombre"]
    rut = request.POST["rut"]
    clave = request.POST["clave"]
    correo = request.POST["correo"]

    if (clave != repClave):
        messages.success(request, "Las contraseñas deben coincidir")
        return redirect("registroUsuario")
    
    elif (len(rut) != 10):
        messages.success(request, "El rut debe tener el siguiente formato 12345678-9")
        return redirect("registroUsuario")
    
    elif (rut.find("-") == -1):
        messages.success(request, "El rut debe ir sin puntos y con guión")
        return redirect("registroUsuario")
    
    elif (len(clave) != 8):
        messages.success(request, "La contraseña debe tener una longitud de 8 caracteres")
        return redirect("registroUsuario")
    
    elif (len(clave) == 8):
        
        tipousuario = TipoUsuario.objects.get(idTipoUsuario=2)
        Usuario.objects.create(
        nombre=nombre,
        rut=rut,
        clave=clave,
        correo=correo,
        idTipoUsuario=tipousuario,
        )
        return redirect("iniciosesion")
    else:
        messages.success(request, "Ingresó mal un dato, vuelva a revisar")
        return redirect("registroUsuario")


#* --------------------------------------------------------------------- ---- Registrar paciente ---- ---------------------------------------------------------------------        


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

#* --------------------------------------------------------------------- ---- Inicio de Sesión ---- ---------------------------------------------------------------------

def iniciar_sesion(request):
    correo  =request.POST["correoinicio"]
    clave = request.POST["contrainicio"]

    try:
        usuario = Usuario.objects.get(correo=correo, clave=clave)
    
        if clave == usuario.clave:
            print('si entro')
            request.session['correo'] = usuario.correo
            tipo = TipoUsuario.objects.get(nombreTipo=usuario.idTipoUsuario)
            request.session['alfin'] = tipo.nombreTipo
            request.session['nombre'] = usuario.nombre

            return redirect('inicio')
        else:
            messages.error(request, "Correo o Contraseña incorrecta..")
            print('no entro')
    except ObjectDoesNotExist:
        messages.error(request, "Correo o Contraseña incorrecta...")
    
    return redirect('iniciosesion')

#* --------------------------------------------------------------------- ---- Cerrar sesión ---- ---------------------------------------------------------------------

def salir(request):
    del request.session['correo']
    del request.session['alfin']
    del request.session['nombre']
    logout(request)
    messages.success(request, "Sesion cerrada exitosamente")
    return redirect("inicio")


# Agregar horas medicas

#* --------------------------------------------------------------------- ---- Crear agenda ---- ---------------------------------------------------------------------

def crear_agenda(request):
    medicos = Medico.objects.all()
  
    contexto = {"medicos": medicos}
    return render(request, "Inicio/crear_agenda.html", contexto)

#* --------------------------------------------------------------------- ----  ---- ---------------------------------------------------------------------

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
        med = Usuario.objects.get(rut = rutMedico)
        existeeee = Agenda.objects.filter(idMedico = rutMedico, fechaDisp = fecha_formateada, horaDisp = hora)

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

#* --------------------------------------------------------------------- ---- Mis horas ---- ---------------------------------------------------------------------
def misHoras(request):
    try:
        correo = request.session['correo']
        usuarios = Usuario.objects.get(correo = correo)
        hor = horaS.objects.filter(rutPaciente = usuarios.rut)
        if hor:
            contexto = {'hor' : hor}
            return render(request, "Inicio/misHoras/misHoras.html", contexto)
        else:
            return render(request, "Inicio/misHoras/misHoras.html")
    except:
        return redirect('iniciosesion')
    
#* --------------------------------------------------------------------- ---- Mostrar doctores ---- ---------------------------------------------------------------------
def doctores(request, idEspe):
    med = MedicoEspec.objects.filter(idEspe = idEspe)
    contexto = {'med' : med}
    return render(request, "Inicio/registro/doctores.html", contexto)

def horasDisp(request, idMedico):
    try:
        horasm = Agenda.objects.get(idMedico = idMedico)
        contexto = {'horasm' : horasm}

        return render(request, "Inicio/horasDoc.html", contexto)
    except:
        return render(request, "Inicio/horasDoc.html")