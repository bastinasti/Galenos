from django.urls import path
from .views import inicio, registro, registro2, iniciosesion, registrar_usuario, iniciar_sesion, salir, registrar_paciente, registroUsuario

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




]