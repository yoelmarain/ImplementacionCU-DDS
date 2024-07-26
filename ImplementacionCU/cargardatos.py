import os
import django

# Configura el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ImplementacionCU.settings')
django.setup()

from api.models import tarifas

tarifass = [
    {'tarifa_id': 1, 'tarifa' : 350, 'categoria': 'Sedan', 'frecuencia': 'Diaria'},
    {'tarifa_id': 2, 'tarifa' : 350,'categoria': 'Sedan', 'frecuencia': 'Semanal'},
    {'tarifa_id': 300,'tarifa' : 350, 'categoria': 'Sedan', 'frecuencia': 'Mensual'},
    {'tarifa_id': 150,'tarifa' : 350, 'categoria': 'Camioneta', 'frecuencia': 'Diaria'},
    {'tarifa_id': 250,'tarifa' : 350, 'categoria': 'Camioneta', 'frecuencia': 'Semanal'},
    {'tarifa_id': 350,'tarifa' : 350, 'categoria': 'Camioneta', 'frecuencia': 'Mensual'},
]

for tarifa_data in tarifass:
    tarifa = tarifas(tarifa_id=tarifa_data['tarifa_id'], tarifa=tarifa_data['tarifa'], categoria=tarifa_data['categoria'], frecuencia=tarifa_data['frecuencia'])
    tarifa.save()

print("Datos cargados exitosamente.")

from api.models import Vehiculo

# Lista de usuarios a agregar
usuarios = [
    {'marca': 'Toyota', 'modelo': 'Corolla', 'anio': 2015, 'tipo': 'Sedan', 'tarifa_id': 1},
    {'marca': 'Nissan', 'modelo': 'Sentra', 'anio': 2018, 'tipo': 'Sedan', 'tarifa_id': 2},
]
# Agregar usuarios a la base de datos
for vehiculo_data in usuarios:
    vehiculo = Vehiculo(marca=vehiculo_data['marca'], modelo=vehiculo_data['modelo'], anio=vehiculo_data['anio'], tipo=vehiculo_data['tipo'], tarifa_id=vehiculo_data['tarifa_id'])
    vehiculo.save()

print("Datos cargados exitosamente.")
