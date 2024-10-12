from django.db import models
from django.contrib.auth.models import BaseUserManager

class PersonaManager(BaseUserManager):
    def create_user(self, tipo_identificacion, numero_id, fecha_nac, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(tipo_identificacion=tipo_identificacion, numero_id=numero_id, fecha_nac=fecha_nac, email=email, **extra_fields)
        user.set_password(password)  # Aquí puedes manejar contraseñas si lo deseas
        user.save(using=self._db)
        return user

    
