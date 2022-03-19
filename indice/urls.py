from django.urls import path
from .views import inicio, otra_vista, numero_random,numero_del_usuario, edad_usuario, mi_plantilla

urlpatterns = [
    path('', inicio),
    path('otra-vista/', otra_vista),
    path('numero-random/', numero_random),
    path('dame-numero/<int:numero>', numero_del_usuario),
    path('mi-plantilla', mi_plantilla),
    # path('dame-numero/<numero>', numero_del_usuario),
    path('tu-edad/<int:numero>', edad_usuario),
]
    
