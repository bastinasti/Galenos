from django.urls import path
from .views import inicio, registro, registro2, iniciosesion, plantillaProducts, registrar_usuario, pag_admin, pag_reportes, pedidos_admin, anadir_product_m, productos_admin, formulario, iniciar_sesion, modificar_product, modificar, eliminar_pro, stock, salir

urlpatterns =[
    path('',inicio, name="inicio"),
    path('registro/', registro, name="registro"),
    path('registro2/', registro2, name="registro2"),
    path('registrar_usuario', registrar_usuario, name="registrar_usuario"),
    path('iniciosesion/', iniciosesion, name="iniciosesion"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('plantillaProducts/<idProducto>', plantillaProducts, name="plantillaProducts"),
    path('pag_admin/', pag_admin, name="pag_admin"),
    path('pag_reportes/', pag_reportes, name="pag_reportes"),
    path('pedidos_admin/', pedidos_admin, name="pedidos_admin"),
    path('formulario/',formulario,name="formulario"),
    path('registrar/', anadir_product_m, name="registrar"),
    path('productos_admin/', productos_admin, name="productos_admin"),
    path('modificar_product/<int:idProducto>', modificar_product, name = "modificar_product"),
    path('modificar/<int:id>', modificar, name="modificar"),
    path('eliminar_pro/<int:idProducto>', eliminar_pro, name="eliminar_pro"),
    path('stock/', stock, name="stock"),
    path('salir/', salir, name="salir"),




]