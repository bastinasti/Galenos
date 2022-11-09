from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductoSerializer, UsuarioSerializer , TipoUsarioSerializer
from Inicio.models import Producto, Usuario, TipoUsuario

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@csrf_exempt
# Funciones para tabla de producto
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarP(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def controlP(request, codigo):
    try:
        p = Producto.objects.get(idProducto = codigo)
    except Producto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(p)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializer(p, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

# Funciones para tablas de usuario
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarU(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def controlU(request, codigo):
    try:
        u = Usuario.objects.get(correo = codigo)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(u)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = UsuarioSerializer(u, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        u.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_tipouser(request):
    if request.method == 'GET':
        productos = TipoUsuario.objects.all()
        serializer = TipoUsarioSerializer(productos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = TipoUsarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def agregarP(request):
    if request.method == 'POST':
        data2 = JSONParser().parse(request)
        serializer = TipoUsarioSerializer(data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def controlT(request, codigo):
    try:
        T = TipoUsuario.objects.get(idTipoUsuario = codigo)
    except TipoUsuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TipoUsarioSerializer(T)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = TipoUsarioSerializer(T, data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        T.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)