from django import forms
from .models import Vehiculo

class ConsultaForm(forms.Form):
    marca = forms.ChoiceField(choices=[], label="Marca")
    modelo = forms.ChoiceField(choices=[], label="Modelo")

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields['marca'].choices = [(vehiculo['marca'], vehiculo['marca']) for vehiculo in Vehiculo.objects.values('marca').distinct()]
