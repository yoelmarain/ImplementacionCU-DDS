from django.shortcuts import render
from .models import Tarifa
from .models import Vehiculo
from django.http import JsonResponse
from .forms import ConsultaForm

def load_modelos(request):
    marca = request.GET.get('marca')
    modelos = Vehiculo.objects.filter(marca=marca).values('modelo').distinct()
    return JsonResponse(list(modelos), safe=False)


def consultarTarifa(request):
    form = ConsultaForm()
    marcas = Vehiculo.objects.values('marca').distinct()
    return render(request, 'consultar_tarifa.html', {'form': form, 'marcas': marcas})


def index(request):
    return render(request, 'index.html')


def verTarifa(request):
    print(request.POST)

    try:
        vehiculo = Vehiculo.objects.filter(marca=request.POST['marca']).get(modelo=request.POST['modelo'])
        tarifa = Tarifa.objects.get(id=vehiculo.tarifa_id_id)
        
        return render(request, 'ver_tarifa.html', {'tarifa':tarifa, 'vehiculo':vehiculo})
    except:
        return render(request, 'consultar_tarifa.html', {'error': 'No se encontró ninguna tarifa para ese vehiculo. Puede ver la lista completa de tarifas en el apartado "Tarifas", sino puede comunicarse con nosotros al #333 444555'})


def verTodasTarifas(request):
    try:
        vehiculos = Vehiculo.objects.all()
        conjunto = []
        
        for v in vehiculos:
            tarifa = Tarifa.objects.get(id=v.tarifa_id_id)
            conjunto.append({'marca':v.marca, 'modelo':v.modelo, 'frecuencia':tarifa.frecuencia, 'categoria':tarifa.categoria, 'precio': tarifa.precio, 'antiguedad': v.antiguedad})
        return render(request, 'todas_las_tarifas.html', {'vehiculos':conjunto})
    except:
        return render(request, 'todas_las_tarifas.html', {'error':"No se encotró ninguna tarifa aún."})


    
