from django.db import models


class OrdenLaboratorio(models.Model):
    fecha_orden = models.DateField()
    documento_orden = models.CharField(max_length=50)
    numero_orden = models.IntegerField()
    codigo_prueba = models.CharField(max_length=20)
    nombre_prueba = models.CharField(max_length=100)
    resultado = models.CharField(max_length=200)  # Ajusta el tamaño según tus necesidades
    valores_referencia = models.TextField()  # Para almacenar múltiples valores, separados por comas o en formato JSON
    unidad = models.CharField(max_length=20)

    def __str__(self):
        return f"Orden #{self.numero_orden} - {self.nombre_prueba} - {self.fecha_orden}"
    
class sexo_biologico (models.Model):
    descripcion = models.CharField (max_length=20)

    def __str__(self):
        return self.descripcion

class tipo_examen (models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class medico (models.Model):
    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre
    
class administrador_salud (models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre