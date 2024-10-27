# localidades/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario, name='formulario'),  # Cargar el formulario si acceden a /localidades/
    path('formulario/', views.formulario, name='formulario'),
    path('estados/', views.lista_estados, name='lista_estados'),
    path('municipios/<int:estado_id>/', views.lista_municipios, name='lista_municipios'),
]
