# localidades/views.py
from django.http import JsonResponse
from .models import Estado, Municipio
from django.shortcuts import render

def formulario(request):
    """Vista para cargar el formulario de selección de estados y municipios."""
    estados = Estado.objects.all()  # Obtener todos los estados de la base de datos
    return render(request, 'localidades/formulario.html', {'estados': estados})


def lista_estados(request):
    """Devuelve la lista de estados en formato JSON."""
    estados = list(Estado.objects.values())  # Convierte los estados a un diccionario
    return JsonResponse(estados, safe=False)

def lista_municipios(request, estado_id):
    """Devuelve la lista de municipios según el estado seleccionado en formato JSON."""
    municipios = list(Municipio.objects.filter(estado_id=estado_id).values())
    return JsonResponse(municipios, safe=False)
