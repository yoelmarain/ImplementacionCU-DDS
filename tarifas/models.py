from django.db import models

# Create your models here.
class Tarifa(models.Model):
    id = models.SmallIntegerField(primary_key=True, unique=True)
    categoria = models.CharField(max_length=30)
    frecuencia = models.CharField(max_length=30)
    precio = models.FloatField()

class Vehiculo(models.Model):
    id = models.SmallIntegerField(primary_key=True, unique=True)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    antiguedad = models.BigIntegerField(null=True, blank=True)
    tipo = models.CharField(max_length=30, null=True, blank=True)
    estado = models.BooleanField(null=True)
    tarifa_id = models.ForeignKey(Tarifa, on_delete=models.CASCADE) 