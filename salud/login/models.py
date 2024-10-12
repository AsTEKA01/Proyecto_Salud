from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from home.models import administrador_salud, sexo_biologico

class PersonaManager(BaseUserManager):
    def create_user(self, tipo_identificacion, numero_id, fecha_nac, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(tipo_identificacion=tipo_identificacion, numero_id=numero_id, fecha_nac=fecha_nac, email=email, **extra_fields)
        user.set_password(password)  # Aquí puedes manejar contraseñas si lo deseas
        user.save(using=self._db)
        return user

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
    nombre2 = models.CharField(max_length=50, null=True)
    fecha_nac = models.DateField()
    email = models.EmailField(unique=True)
    id_sexo_biologico = models.ForeignKey(sexo_biologico, on_delete=models.SET_NULL, null=True)
    admin_salud = models.ForeignKey(administrador_salud, on_delete=models.SET_NULL, null=True)
    direccion = models.TextField(null=True)
    tel_movil = models.CharField(max_length=20, null=True)
    # Aquí hacemos que el campo password sea opcional
    password = models.CharField(max_length=128, null=True)  

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=timezone.now)

    objects = PersonaManager()

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
        return f"{self.numero_id}  / {self.nombre1}  / {self.apellido1}"
