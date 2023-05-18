from django.urls import path
from .views import agregar_dia, inicio, registro, registro2, iniciosesion, registrar_usuario, iniciar_sesion, salir, registrar_paciente, registroUsuario, crear_agenda

urlpatterns =[
    path('',inicio, name="inicio"),
    path('registro/', registro, name="registro"),
    path('registro2/', registro2, name="registro2"),
    path('registroUsuario/', registroUsuario, name="registroUsuario"),
    path('registrar_paciente/', registrar_paciente, name="registrar_paciente"),
    path('registrar_usuario', registrar_usuario, name="registrar_usuario"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('salir/', salir, name="salir"),
    path('crear_agenda/', crear_agenda, name="crear_agenda"),
    path('agregar_dia/', agregar_dia, name="agregar_dia"),
]