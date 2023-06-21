from django.db import models


# Create your models here.
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

class TipoUsuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key = True, verbose_name = "Id tipo")
    nombreTipo = models.CharField(max_length = 10, verbose_name = "Admin Cliente", null = False, blank = False)
    
    def __str__(self):
        return self.nombreTipo


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key = True, verbose_name = "Id usuarios")
    nombre = models.CharField(max_length = 15, verbose_name = "Nombre Cliente")
    rut = models.CharField(max_length = 10, verbose_name = "Rut del paciente")
    clave = models.CharField(max_length = 16, verbose_name = "Contraseña", blank = False, null = False)
    correo = models.CharField(max_length = 40, verbose_name = "Correo")
    telefono = models.CharField(max_length = 9,verbose_name = "Telefono de la persona")
    idTipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Paciente(models.Model):
    idPaciente =  models.AutoField(primary_key = True, verbose_name = "La primary key del paciente")
    idPrevision = models.ForeignKey(Prevision, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.idPaciente
    
    
class Medico(models.Model):
    idMedico =  models.AutoField(primary_key = True, verbose_name = "La primary key del medico")
    fechaContra = models.CharField(max_length = 8,verbose_name = "Fecha de contratación del medico")
    sueldo = models.IntegerField(verbose_name = "Sueldo del medico")
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.idUsuario.nombre
    
    
class MedicoEspec(models.Model):
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    idEspe = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.idMedico.idUsuario.nombre

class Agenda(models.Model):
    idAgenda = models.AutoField(primary_key = True, verbose_name = "Id agenda")
    fechaDisp = models.CharField(max_length = 8,verbose_name = "Fecha de atencion disponible")
    horaDisp = models.CharField(max_length = 8,verbose_name = "hora de atencion disponible")
    estado = models.CharField(max_length = 50, verbose_name = "estado de la hora")
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)

class horaS(models.Model):
    id_horasol = models.AutoField(primary_key = True, verbose_name = "Id de hora solicitada")
    rutPaciente = models.CharField(max_length = 10, verbose_name = "Rut del paciente")
    idAgenda = models.ForeignKey(Agenda,on_delete=models.CASCADE)
    idMedico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    idEspe = models.ForeignKey(Especialidad, on_delete=models.CASCADE)