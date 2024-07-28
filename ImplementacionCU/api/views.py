from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .forms import VehiculoForm
from .models import Vehiculo
from .models import tarifas
from .forms import CargarVehiculoForm

def consulta_tarifa(request):
    global estado_resultado
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            año = form.cleaned_data['año']
            tipo = form.cleaned_data['tipo']
            vehiculo = Vehiculo.objects.filter(marca=marca, modelo=modelo, año=año, tipo=tipo).first()
            if vehiculo:
                try:
                    tarifa = tarifas.objects.get(tarifa_id=vehiculo.tarifa_id) 
                    estado_resultado = 'encontrado'
                    resultado = f"""
                        <div class='resultado'>
                            <div class='vehiculo'>
                            <span class='marca'>{vehiculo.marca}</span>
                            <span class='modelo'>{vehiculo.modelo}</span>
                            <span class='tipo'>{vehiculo.tipo}</span>
                            <span class='anio'>{vehiculo.año}</span>
                            </div>
                            <span class='tarifa'>Tarifa: ${tarifa.tarifa}</span>
                        </div>
                    """
                except ObjectDoesNotExist:
                    resultado = "Tarifa no encontrado"
            else:
                resultado = """<div class='resultado'> Lo sentimos, el vehiculo no se encuentra cargado en la base de datos </div>"""
                estado_resultado = 'no_encontrado'
            return render(request, 'resultado.html', {'resultado': resultado, 'estado_resultado': estado_resultado})
    else:
        form = VehiculoForm()
    return render(request, 'index.html', {'form': form})


def cargar_vehiculo(request):
    if request.method == 'POST':
        form = CargarVehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            tarifa_id = form.cleaned_data['tarifa_id'].id  # Obtener el ID de la tarifa
            tarifa_instance = get_object_or_404(tarifas, id=tarifa_id)  # Obtener la instancia de tarifas
            vehiculo.tarifa_id = tarifa_instance  # Asignar la instancia de tarifas
            vehiculo.save()
            resultado = "Vehículo cargado exitosamente"
            return render(request, 'exito.html', {'resultado': resultado})  # Redirigir a la página de éxito
    else:
        form = CargarVehiculoForm()
    return render(request, 'cargar_vehiculo.html', {'form': form})


def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})
