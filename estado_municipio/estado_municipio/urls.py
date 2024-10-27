
# estados_municipios/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_polls(request):
    return redirect('/localidades/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('localidades/', include('localidades.urls')),  # Asegúrate de que esta línea esté presente
    path('', redirect_to_polls),  # Redirige la raíz a /polls/
]

