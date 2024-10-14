from django.shortcuts import render, get_object_or_404
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


    return render(request, 'home.html', {'ordenes': ordenes, 'page_obj': page_obj})

def ver_examen(request, id):
    orden = get_object_or_404(OrdenLaboratorios, id=id)

    # Verifica si orden.persona está correctamente referenciada
    if orden.paciente:
        edad = orden.paciente.calcular_edad()  # Llama al método para calcular la edad
        sexo = orden.paciente.sexo_biologico # Obtén el sexo directamente
        identificacion = orden.paciente.numero_id # aqui obtengo el numero de documento del paciente
        number = orden.paciente.tel_movil # aqui obtengo el numero de documento del paciente
        
    if orden.medico:
        medico = orden.medico.nombre

    else:
        edad = None
        sexo = None

    context = {
        'orden': orden,
        'edad': edad,
        'sexo': sexo,
        'identificacion': identificacion,
        'number': number,
        'medico': medico
    }
    return render(request, 'home_view.html', context)