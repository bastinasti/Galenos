from django.shortcuts import render, redirect 
from .models import  Usuario, TipoUsuario, Paciente
from django.contrib import messages
from django.contrib.auth import logout 



# Create your views here.


def inicio(request):
    return render(request, 'Inicio/DelanekoShop.html')

def registro(request):
    return render(request, 'Inicio/Registro/registro.html')

def registro2(request):
    return render(request, 'Inicio/Registro2/registro2.html')

def registroUsuario(request):
    return render(request, 'Inicio/registroUsuario/registroUsuario.html')


def iniciosesion(request):
    return render (request, 'Inicio/InicioSesion/sesion.html')


#Registrar Usuario

def registrar_usuario(request):
    
    nombre = request.POST['nombre']
    apellido1 = request.POST['apellido1']
    email = request.POST['email']
    con1 = request.POST['con1']
    tipousuario = TipoUsuario.objects.get(idTipoUsuario = 2)
    
    Usuario.objects.create(nombre = nombre, apellido = apellido1, clave = con1, correo = email ,idTipoUsuario = tipousuario)
    return redirect('inicio')

def registrar_paciente(request):

    rut1 = request.POST['rut1']
    prevision1 = request.POST['prevision1']
    especialidad1 = request.POST['especialidad1']
    medico1 = request.POST['medico1']

    Paciente.objects.create(rutPaciente = rut1, prevision = prevision1, especialidad = especialidad1, nomMedico = medico1)
    return redirect ('registro')




def iniciar_sesion(request):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(correo = request.POST['correoinicio'], clave = request.POST['contrainicio'])
            request.session['correo'] = usuario.correo
           
            if (usuario.idTipoUsuario.idTipoUsuario == 1):
                return render(request, 'Inicio/Admin/pag_admin.html')
            else:
                contexto = {"usuario":usuario}
                return render(request, 'Inicio/DelanekoShop.html')
        except Usuario.DoesNotExist as e: 
            messages.error(request, 'Nombre de usuario o contraseña incorrecta...')   

    return render(request, 'Inicio/InicioSesion/sesion.html')

def salir(request):
    logout(request)
    messages.success(request,'Sesion cerrada exitosamente')
    return redirect('inicio')


# Agregar horas medicas

def registroHoras(request):
    return render(request, 'Inicio/registro_horas.html')
