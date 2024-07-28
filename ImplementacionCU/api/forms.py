from django import forms
from .models import Vehiculo, tarifas

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio', 'tipo']
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CargarVehiculoForm(forms.ModelForm):
    tarifa_id = forms.ModelChoiceField(queryset=tarifas.objects.all(), to_field_name="id")
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio', 'tipo', 'tarifa_id']