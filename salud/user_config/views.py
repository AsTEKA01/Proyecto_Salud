from django.shortcuts import render
from home.pacientes import Persona

def user_date(request):
    if request.user.is_authenticated:
        context = {'user': request.user}

    return render(request, 'user_config.html')

def filt_name(request):
    user = Persona.objects.all
    
    if user.Persona:
        name2 = user.Persona.nombre2
        
    else:
        name2 = ''