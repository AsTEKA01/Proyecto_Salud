from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .obervaciones_lab import OrdenLaboratorios
# views.py

def name_sal(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        
@login_required
def list_orden(request):
    usuario = request.user
    ordenes = OrdenLaboratorios.objects.filter(paciente=usuario)

    # Obtener filtros del formulario
    numero_orden = request.GET.get('numero_orden')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    # Aplicar filtros si están presentes
    if numero_orden:
        ordenes = ordenes.filter(numero_orden__icontains=numero_orden)

    if fecha_inicio and fecha_fin:
        ordenes = ordenes.filter(fecha_orden__range=[fecha_inicio, fecha_fin])
        
    # Paginación
    paginator = Paginator(ordenes, 5)  # 5 órdenes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'ordenes': ordenes})