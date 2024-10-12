from django.db import models

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