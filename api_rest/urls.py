from django.urls import path
from api_rest.views import agregarU, controlU, lista_productos, agregarP, controlP, lista_usuarios
from api_rest.viewsLogin import login

urlpatterns = [
    path('lista_productos/', lista_productos, name="lista_productos"),
    path('agregarP/', agregarP, name="agregarP"),
    path('controlP/<codigo>', controlP, name="controlP"),
    path('login', login, name="login"),
    path('lista_usuario/', lista_usuarios, name="lista_usuario"),
    path('agregarU/', agregarU, name="agregarU"),
    path('controlU/<codigo>', controlU, name="controlU"),
]