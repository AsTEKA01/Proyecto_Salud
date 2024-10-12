from django.db import models
from .pacientes import Persona
from .models import medico


class OrdenLaboratorios(models.Model):
    fecha_orden = models.DateField()
    paciente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    medico = models.ForeignKey(medico, null=True, on_delete=models.CASCADE)
    NAME_GROUP = [
        ('Hematologia', 'Hematologia'),
        ('Oncología', 'Oncología'),
        ('Cardiología', 'Cardiología'),
        ('Neurología', 'Neurología'),
        ('Pediatría', 'Pediatría'),
        ('Ginecología', 'Ginecología'),
        ('Urología', 'Urología'),
        ('Gastroenterología', 'Gastroenterología'),
        ('Oftalmología', 'Oftalmología'),
        ('Dermatología', 'Dermatología'),
        ('Psiquiatría', 'Psiquiatría'),
    ]
    documento_orden = models.CharField(max_length=50)
    name_group = models.CharField(max_length=50, default='Desconocida', choices=NAME_GROUP)
    numero_orden = models.IntegerField()
    codigo_prueba = models.CharField(max_length=20)
    nombre_prueba = models.CharField(max_length=100)
    resultado = models.CharField(max_length=200)  # Ajusta el tamaño según tus necesidades
    valores_referencia = models.TextField()  # Para almacenar múltiples valores, separados por comas o en formato JSON
    unidad = models.CharField(max_length=20)

    def __str__(self):
        return f"Orden #{self.numero_orden} - {self.nombre_prueba} - {self.fecha_orden} - {self.paciente}"
    