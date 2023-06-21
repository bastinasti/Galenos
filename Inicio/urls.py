from django.urls import path
from .views import doctores, horasDisp, obtener_medicos,agregar_dia, inicio, misHoras, monitoPaciente, especialidad, registro2, iniciosesion, registrar_usuario, iniciar_sesion, salir, registrar_paciente, registroUsuario, crear_agenda


urlpatterns =[
    path('',inicio, name="inicio"),
    path('especialidad/', especialidad, name="especialidad"),
    path('registro2/', registro2, name="registro2"),
    path('registroUsuario/', registroUsuario, name="registroUsuario"),
    path('registrar_paciente/', registrar_paciente, name="registrar_paciente"),
    path('registrar_usuario', registrar_usuario, name="registrar_usuario"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('salir/', salir, name="salir"),
    path('crear_agenda/', crear_agenda, name="crear_agenda"),
    path('agregar_dia/', agregar_dia, name="agregar_dia"),
    path('monitoPaciente/', monitoPaciente, name="monitoPaciente"),
    path('misHoras/', misHoras, name="misHoras"),
    path('obtener_medicos/', obtener_medicos, name='obtener_medicos'),
    path('doctores/<int:idEspe>/', doctores, name='doctores'),
    path('horasDisp/<int:idMedico>/', horasDisp, name='horasDisp'),
]