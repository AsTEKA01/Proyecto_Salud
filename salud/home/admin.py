from django.contrib import admin
from .models import OrdenLaboratorio, sexo_biologico, tipo_examen, medico, administrador_salud
from login.models import Persona

admin.site.register(sexo_biologico)
admin.site.register(OrdenLaboratorio)
admin.site.register(tipo_examen)
admin.site.register(Persona)
admin.site.register(administrador_salud)
admin.site.register(medico)


