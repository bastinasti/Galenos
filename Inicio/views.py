from django.shortcuts import render, redirect 
from .models import Producto, Usuario, TipoUsuario, TipoProducto
from .Carrito import Carrito
from django.contrib import messages
from django.contrib.auth import logout 



# Create your views here.


def inicio(request):
    return render(request, 'Inicio/DelanekoShop.html')

def registro(request):
    return render(request, 'Inicio/Registro/registro.html')

def seccionperro(request):
    perro = Producto.objects.filter(idTipProducto = 2).order_by('idProducto')
    contexto = {"producto":perro}
    return render(request, 'Inicio/PagAnimales/Perros.html',contexto)

def secciongato(request):
    gato = Producto.objects.filter(idTipProducto = 1).order_by('idProducto')
    contexto = {"producto":gato}
    return render(request, 'Inicio/PagAnimales/Gato.html',contexto)

def seccionexotico(request):
    exotico = Producto.objects.filter(idTipProducto = 3).order_by('idProducto')
    contexto = {"producto":exotico}
    return render(request, 'Inicio/PagAnimales/Exotico.html',contexto)


def iniciosesion(request):
    return render (request, 'Inicio/InicioSesion/sesion.html')

def plantillaProducts(request, idProducto):
    productos = Producto.objects.filter(idProducto = idProducto).order_by('idProducto')
    contexto = {"producto":productos}
    return render (request, 'Inicio/PagAnimales/PagProductos/Products.html', contexto)    


#Carrito

def carrito(request):
    return render(request, 'Inicio/carrito_compra.html')

def agregar_producto(request, idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto = idProducto)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")

#Registrar Usuario

def registrar_usuario(request):
    
    nombre = request.POST['nombre']
    apellido1 = request.POST['apellido1']
    email = request.POST['email']
    con1 = request.POST['con1']
    tipousuario = TipoUsuario.objects.get(idTipoUsuario = 2)
    
    Usuario.objects.create(nombre = nombre, apellido = apellido1, clave = con1, correo = email ,idTipoUsuario = tipousuario)
    return redirect('inicio')


#Pag admin

def pag_admin(request):
    return render(request, 'Inicio/Admin/pag_admin.html')

def pag_reportes(request):
    return render(request, 'Inicio/Admin/pag_reportes.html')

def pedidos_admin(request):
    return render(request, 'Inicio/Admin/pedidos_admin.html')

def stock(request):
    productos = Producto.objects.all()
    idp = TipoProducto.objects.all()
    data = {
        'productos': productos,
        'idp': idp
    }
    return render(request, 'Inicio/Admin/stock.html', data)

def formulario(request):
    categorias = TipoProducto.objects.all()
    contexto = {"tipoProducto": categorias}
    return render(request,"Inicio/Admin/añadir_product.html",contexto)

def anadir_product_m(request):
    nombrepro = request.POST['nombrepro']
    valor = request.POST['valor']
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']
    foto = request.FILES['foto']
    categoria = request.POST['categoria']


    idtipproducto = TipoProducto.objects.get(idTipProducto = categoria)
    Producto.objects.create(nomProducto = nombrepro, valor = valor, descripcion = descripcion, stock = stock, imgProducto = foto, idTipProducto = idtipproducto)

    messages.success(request,'Producto Añadido')

    return redirect('formulario')

def productos_admin(request):
    producto1 = Producto.objects.all().order_by('idProducto')
    contexto1 = {"producto":producto1}
    return render(request, 'Inicio/Admin/productos_admin.html', contexto1)


def modificar_product(request, idProducto):
    productomodi = Producto.objects.get(idProducto = idProducto)
    categoria1 = TipoProducto.objects.all()
    
    contexto = {
        "producto" : productomodi,
        "categoria" : categoria1    
    }
    
    return render(request,'Inicio/Admin/modificar_product.html',contexto)

def modificar(request,id):
    id2= id
    nombrepro = request.POST['nombrepro']
    valor = request.POST['valor']
    descripcion = request.POST['descripcion']
    stock = request.POST['stock']
    foto = request.FILES['foto']

    producto = Producto.objects.get(idProducto = id2)

    producto.nomProducto = nombrepro
    producto.valor = valor
    producto.descripcion = descripcion
    producto.stock = stock
    producto.imgProducto = foto


    producto.save()

    messages.success(request, 'Producto Modificado')
    return redirect('productos_admin')

def eliminar_pro(request, idProducto):
    producto3 = Producto.objects.get(idProducto = idProducto)
    producto3.delete()
    messages.success(request, 'Producto Eliminado')
    return redirect('productos_admin')


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


