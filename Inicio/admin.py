from django.contrib import admin
from .models import TipoProducto, Producto, TipoUsuario, Usuario

# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)

