from django.db import models
from .pacientes import Persona

class OrdenLaboratorios(models.Model):
    fecha_orden = models.DateField()
    paciente = models.ForeignKey(Persona, on_delete=models.CASCADE)
    documento_orden = models.CharField(max_length=50)
    numero_orden = models.IntegerField()
    codigo_prueba = models.CharField(max_length=20)
    nombre_prueba = models.CharField(max_length=100)
    resultado = models.CharField(max_length=200)  # Ajusta el tamaño según tus necesidades
    valores_referencia = models.TextField()  # Para almacenar múltiples valores, separados por comas o en formato JSON
    unidad = models.CharField(max_length=20)

    def __str__(self):
        return f"Orden #{self.numero_orden} - {self.nombre_prueba} - {self.fecha_orden} - {self.paciente}"
    