from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from home.pacientes import Persona
from django.core.exceptions import ValidationError

class IdentificacionBackend(BaseBackend):
    def authenticate(self, request, tipo_identificacion=None, numero_id=None, fecha_nac=None):
        try:
            # Busca al usuario en tu modelo basado en los campos de identificación
            user = Persona.objects.get(tipo_identificacion=tipo_identificacion, numero_id=numero_id, fecha_nac=fecha_nac)
            return user
        except Persona.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Persona.objects.get(pk=user_id)
        except Persona.DoesNotExist:
            return None