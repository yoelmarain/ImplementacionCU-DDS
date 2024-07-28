from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Vehiculo, tarifas

admin.site.register(Vehiculo)
admin.site.register(tarifas)
