from django.contrib import admin
from .models import Agenda, TipoUsuario, Usuario, Prevision, Especialidad, Medico, Paciente, MedicoEspec, horaS

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Prevision)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(MedicoEspec)
admin.site.register(Agenda)
admin.site.register(horaS)

