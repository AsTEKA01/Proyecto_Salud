from django import forms
from captcha.fields import CaptchaField


TIPO_IDENTIFICACION_OPCIONES = [
    ('CC', 'Cédula de ciudadanía'),
    ('TI', 'Tarjeta de identidad'),
    ('CE', 'Cédula de extranjería'),
]

class CustomLoginForm(forms.Form):
    tipo_identificacion = forms.ChoiceField(choices=TIPO_IDENTIFICACION_OPCIONES)
    numero_id = forms.CharField(max_length=50)
    fecha_nac = forms.DateField(input_formats=['%Y-%m-%d'])
    captcha = CaptchaField()  # Campo CAPTCHA
