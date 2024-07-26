from django.urls import path
from .views import consulta_tarifa, cargar_vehiculo, listar_vehiculos

urlpatterns = [
    path ('consultartarifa', consulta_tarifa, name='consultar_tarifa'),
    path ('cargarvehiculo', cargar_vehiculo, name='cargar_vehiculo'),
    path ('listarvehiculos', listar_vehiculos, name='listar_vehiculos'),
]