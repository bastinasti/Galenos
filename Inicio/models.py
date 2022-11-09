from django.db import models


# Create your models here.
class TipoProducto(models.Model):
    idTipProducto = models.AutoField(primary_key = True, verbose_name = "ID tipo producto")
    nomTipo = models.CharField(max_length = 15, verbose_name = "Gato Perro Exotico", blank = False, null = False)

    def __str__(self):
        return self.nomTipo


class Producto(models.Model):
    idProducto = models.AutoField(primary_key = True, verbose_name = "La primary key de productos")
    nomProducto = models.CharField(max_length = 50, verbose_name = "Nombre del producto")
    valor = models.IntegerField(verbose_name = "Valor producto")
    descripcion = models.CharField(max_length = 300, verbose_name = "Descripción del producto")
    stock = models.IntegerField(verbose_name = "Cantidad de productos", blank = False, null = True)
    imgProducto = models.ImageField(upload_to = "productos", null = True)
    idTipProducto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomProducto

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key = True, verbose_name = "Id tipo")
    nombreTipo = models.CharField(max_length = 10, verbose_name = "Admin Cliente", null = False, blank = False)
    
    def __str__(self):
        return self.nombreTipo


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, verbose_name = "Id usuarios")
    nombre = models.CharField(max_length = 15, verbose_name = "Nombre Cliente")
    apellido = models.CharField(max_length = 15, verbose_name = "Apellido Cliente")
    clave = models.CharField(max_length = 16, verbose_name = "Contraseña", blank = False, null = False)
    correo = models.CharField(max_length = 40, verbose_name = "Correo")
    idTipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre