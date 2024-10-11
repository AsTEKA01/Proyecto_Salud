from django.db import models
from home.models import sexo_biologico

class Persona(models.Model):
    TIPOS_IDENTIFICACION = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cédula de Ciudadania'),
        ('CE', 'Cédula de Extranjería'),
    ]
    id = models.AutoField(primary_key=True) 
    tipo_identificacion = models.CharField(max_length=20, choices=TIPOS_IDENTIFICACION)
    numero_id = models.CharField(max_length=50) 
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50, null=True)
    fecha_nac = models.DateField()
    id_sexo_biologico = models.ForeignKey(sexo_biologico, on_delete=models.SET_NULL, null=True)
    direccion = models.TextField()
    tel_movil = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.numero_id}  / {self.nombre1}  / {self.apellido1}"