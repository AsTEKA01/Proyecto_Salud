from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from django.conf import settings
import os
from home.obervaciones_lab import OrdenLaboratorios

def generar_informe_pdf(request, orden_id):
    # Obtener los datos de la orden médica
    orden = OrdenLaboratorios.objects.get(id=orden_id)

    # Crear un objeto HttpResponse con el tipo de contenido 'application/pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="informe_orden_medica.pdf"'

    # Crear un objeto Canvas para generar el PDF
    pdf = canvas.Canvas(response, pagesize=A4)

    # Usar os.path.join y settings.STATICFILES_DIRS para obtener la ruta del logotipo
    logo_path = os.path.join(settings.STATICFILES_DIRS[0], 'img', 'logo.png')

    # Añadir el logotipo centrado en la parte superior
    try:
        pdf.drawImage(logo_path, 50, 710, width=100, height=100)  # Centrar y ajustar el tamaño del logo
    except OSError:
        pdf.setFont("Helvetica", 12)
        pdf.drawString(220, 750, "No se pudo cargar el logotipo")

    # Añadir espacio entre el logo y el título
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(180, 750, f"Informe de Orden Médica #{orden.id}")

    # Dibujar una línea divisoria debajo del título
    pdf.line(40, 710, 550, 710)

    # Información del paciente bien alineada
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, 690, f"Paciente: {orden.paciente.nombre1} {orden.paciente.apellido1} {orden.paciente.apellido2}")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, 670, f"Documento de la Orden: {orden.documento_orden}")
    pdf.drawString(40, 650, f"Médico: {orden.medico.nombre}")
    pdf.drawString(40, 630, f"Fecha de la Orden: {orden.fecha_orden}")

    # Añadir más espacio y una línea antes de la tabla
    pdf.line(40, 620, 550, 620)

    # Ajustar los datos en la tabla con los nuevos campos
    data = [
        ["Nombre del Examen", "Resultado", "Código de Prueba","Observaciones"],  # Encabezado
        [orden.name_group, orden.resultado, orden.codigo_prueba, orden.observaciones]
    ]

    # Ajustar los anchos de las columnas para mejor organización
    table = Table(data, colWidths=[1.8 * inch, 1.0 * inch, 2.2 * inch, 1.8 * inch, 1.8 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),  # Color para el encabezado
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto blanco en encabezado
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centrado en todo
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Negrita en encabezado
        ('FONTSIZE', (0, 0), (-1, 0), 12),  # Tamaño del encabezado
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightblue),  # Fondo azul claro para las filas
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Bordes negros para la tabla
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Fuente normal para los datos
        ('FONTSIZE', (0, 1), (-1, -1), 10),  # Tamaño de los datos
    ]))

    # Ajustar la posición de la tabla
    table.wrapOn(pdf, 40, 500)
    table.drawOn(pdf, 40, 500)

    # Pie de página
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(40, 100, "Este informe es generado automáticamente por el sistema de laboratorio.")
    pdf.drawString(40, 85, "www.vidaybienestar.com")
    
    # Finalizar el PDF
    pdf.showPage()
    pdf.save()

    return response
