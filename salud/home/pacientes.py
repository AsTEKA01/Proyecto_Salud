from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from home.models import administrador_salud, sexo_biologico

class Persona(AbstractBaseUser, PermissionsMixin):
    TIPOS_IDENTIFICACION = [
        ('TI', 'Tarjeta de Identidad'),
        ('CC', 'Cédula de Ciudadania'),
        ('CE', 'Cédula de Extranjería'),
    ]

    id = models.AutoField(primary_key=True)
    tipo_identificacion = models.CharField(max_length=20, choices=TIPOS_IDENTIFICACION)
    numero_id = models.CharField(max_length=50, unique=True)
    apellido1 = models.CharField(max_length=50)
    apellido2 = models.CharField(max_length=50)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50, default='No especificado', null=False)
    fecha_nac = models.DateField()
    email = models.EmailField(unique=True)
    sexo_biologico = models.ForeignKey(sexo_biologico, on_delete=models.SET_NULL, null=True)
    admin_salud = models.ForeignKey(administrador_salud, on_delete=models.SET_NULL, null=True)
    direccion = models.TextField(null=True)
    tel_movil = models.CharField(max_length=20, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='persona_set',  # Cambia este nombre según tus necesidades
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='persona_user_permissions',  # Cambia este nombre para evitar conflictos
    )

    USERNAME_FIELD = 'numero_id'
    REQUIRED_FIELDS = ['email', 'tipo_identificacion', 'fecha_nac']

    def __str__(self):
        return f"{self.numero_id}  / {self.nombre1}  / {self.apellido1} / {self.apellido2}"
