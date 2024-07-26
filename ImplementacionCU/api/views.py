from django.shortcuts import render, redirect
from .forms import VehiculoForm
from .models import Vehiculo
from .models import tarifas
from .forms import CargarVehiculoForm

def consulta_tarifa(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            anio = form.cleaned_data['anio']
            tipo = form.cleaned_data['tipo']
            vehiculo = Vehiculo.objects.filter(marca=marca, modelo=modelo, anio=anio, tipo=tipo).first()
            if vehiculo:
                tarifa = tarifas.objects.get(id=vehiculo.tarifa_id)
                resultado = f"Vehiculo encontrado: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Tipo: {vehiculo.tipo}, Tarifa: {tarifa.tarifa}"
            else:
                resultado = "Vehiculo no encontrado"
            return render(request, 'resultado.html', {'resultado': resultado})
    else:
        form = VehiculoForm()
    return render(request, 'index.html', {'form': form})


def cargar_vehiculo(request):
    if request.method == 'POST':
        form = CargarVehiculoForm(request.POST)
        if form.is_valid():
            vehiculo = form.save(commit=False)
            vehiculo.tarifa_id = request.POST.get('tarifa_id')
            vehiculo.save()
            resultado = "Vehículo cargado exitosamente"
            return render(request, 'exito.html', {'resultado': resultado})  # Render the 'exito.html' template with the success message
    else:
        form = CargarVehiculoForm()
    return render(request, 'cargar_vehiculo.html', {'form': form})

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'listar_vehiculos.html', {'vehiculos': vehiculos})