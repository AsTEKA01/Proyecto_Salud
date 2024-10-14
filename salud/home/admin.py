from django.contrib import admin
from .models import sexo_biologico, tipo_examen, medico, administrador_salud
from .obervaciones_lab import OrdenLaboratorios
from .pacientes import Persona
from django import forms

class OrdenLaboratoriosAdmin(admin.ModelAdmin):
    list_display = ('numero_orden', 'paciente__numero_id', 'fecha_orden', 'medico', 'name_group')
    search_fields = ('numero_orden', 'paciente__numero_id', 'medico__nombre')
    list_filter = ('fecha_orden', 'name_group')  # Filtrar por fecha y grupo de pruebas
    ordering = ('-fecha_orden',)  # Ordenar por fecha de forma descendente

admin.site.register(OrdenLaboratorios, OrdenLaboratoriosAdmin)
admin.site.register(sexo_biologico)
admin.site.register(tipo_examen)
admin.site.register(Persona)
admin.site.register(administrador_salud)
admin.site.register(medico)


