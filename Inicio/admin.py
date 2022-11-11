from django.contrib import admin
from .models import TipoUsuario, Usuario, Persona, Prevision, Especialidad, Medico, Paciente, MedicoEspec

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Persona)
admin.site.register(Prevision)
admin.site.register(Especialidad)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(MedicoEspec)

