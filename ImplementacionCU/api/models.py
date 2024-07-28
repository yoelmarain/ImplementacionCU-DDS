from django.db import models
import random
import string

# Create your models here.
# agregar los null = false

#no se lo usa
def crear_id():
    while True:
        id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
        if not Vehiculo.objects.filter(id=id).exists():
            break


class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    tipo = models.CharField(max_length=20)
    tarifa_id = models.ForeignKey('tarifas', to_field='tarifa_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.marca} {self.modelo} {self.tipo} {self.año}'

class tarifas (models.Model):
    tarifa_id = models.CharField(max_length=2, unique=True)
    tarifa = models.FloatField()
    categoria = models.CharField(max_length=20)
    frecuencia = models.CharField(max_length=20)

    def __str__(self):
        return self.tarifa_id

