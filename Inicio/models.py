from django.db import models


# Create your models here.
class TipoProducto(models.Model):
    idTipProducto = models.AutoField(primary_key = True, verbose_name = "ID tipo producto")
    nomTipo = models.CharField(max_length = 15, verbose_name = "Gato Perro Exotico", blank = False, null = False)

    def __str__(self):
        return self.nomTipo


class Persona(models.Model):
    idPersona = models.AutoField(primary_key = True, verbose_name = "La primary key de persona")
    rutPersona = models.CharField(max_length = 10, verbose_name = "Rut de la persona")
    nomPersona = models.CharField(max_length = 50, verbose_name = "Nombre de la persona")
    apellido = models.CharField(max_length = 50,verbose_name = "Apellido/s de la persona")
    correo = models.CharField(max_length = 300, verbose_name = "Correo de la persona")
    telefono = models.CharField(max_length = 9,verbose_name = "Telefono de la persona")
    fechaNac = models.CharField(max_length = 8,verbose_name = "Fecha de nacimiento de la persona")

    def __str__(self):
        return self.rutPersona


class Prevision(models.Model):
    idPrevision =  models.AutoField(primary_key = True, verbose_name = "La primary key de la previsión")
    nombrePrevi = models.CharField(max_length = 50, verbose_name = "Nombre de la previsión")

    def __str__(self):
        return self.nombrePrevi


class Especialidad (models.Model):
    idEspe = models.AutoField(primary_key = True, verbose_name = "La primary key de la especialidad")
    nombreEspe = models.CharField(max_length = 50, verbose_name = "Nombre de la especialidad")

    def __str__(self):
        return self.nombreEspe
    

class Medico(models.Model):
    idMedico =  models.AutoField(primary_key = True, verbose_name = "La primary key del medico")
    rutMedico = models.CharField(max_length = 10, verbose_name = "Rut del medico")
    fechaContra = models.CharField(max_length = 8,verbose_name = "Fecha de contratación del medico")
    sueldo = models.IntegerField(verbose_name = "Sueldo del medico")
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.rutMedico


class Paciente(models.Model):
    idPaciente =  models.AutoField(primary_key = True, verbose_name = "La primary key del paciente")
    rutPaciente = models.CharField(max_length = 10, verbose_name = "Rut del paciente")
    idPersona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    idPrevision = models.ForeignKey(Prevision, on_delete=models.CASCADE)

    def __str__(self):
        return self.rutPaciente

class MedicoEspec(models.Model):
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    idEspe = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.idMedico


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