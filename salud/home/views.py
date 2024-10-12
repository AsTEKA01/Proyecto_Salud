from django.shortcuts import render
from .obervaciones_lab import OrdenLaboratorios
# views.py
def name_sal(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'home.html', context)
    
def name_sal(request):
    observaciones = OrdenLaboratorios.objects.all()
    return render(request, 'home.html', {'observaciones': observaciones}) 
