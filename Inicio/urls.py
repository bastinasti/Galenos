from django.urls import path
from .views import tomar_hora,formulario_paci,doctores, editarHoras, pagos, horasDisp, obtener_medicos,agregar_dia, inicio, misHoras, monitoPaciente, especialidad, registro2, iniciosesion, registrar_usuario, iniciar_sesion, salir, registrar_paciente, registroUsuario, crear_agenda


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
    path('horasDisp/<int:idMedico>/<int:idEspe>/', horasDisp, name='horasDisp'),
    path('obtener_medicos/', obtener_medicos, name='obtener_medicos'),
    path('editarHoras/', editarHoras, name='editarHoras'),
    path('pagos/', pagos, name='pagos'),
    path('formulario_paci/<int:idAgenda>/<int:idMedico>/<int:idEspe>/',formulario_paci,name="formulario_paci"),
    path('tomar_hora/<int:idAgenda>/<int:idMedico>/<int:idEspe>/',tomar_hora, name="tomar_hora")
]