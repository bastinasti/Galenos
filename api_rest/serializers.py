from dataclasses import fields
from rest_framework import serializers
from Inicio.models import Producto, TipoUsuario, Usuario

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nomProducto', 'valor', 'descripcion', 'stock','imgProducto','idTipProducto']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario','nombre','apellido','clave','correo','idTipoUsuario']

class TipoUsarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoUsuario
        fields = ['idTipoUsuario','nombreTipo']