from django.contrib import admin
from .models import sexo_biologico, tipo_examen, medico, administrador_salud
from .obervaciones_lab import OrdenLaboratorios
from .pacientes import Persona

admin.site.register(sexo_biologico)
admin.site.register(OrdenLaboratorios)
admin.site.register(tipo_examen)
admin.site.register(Persona)
admin.site.register(administrador_salud)
admin.site.register(medico)


