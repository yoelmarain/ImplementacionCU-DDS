from django import forms
from .models import Vehiculo, tarifas

class VehiculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        marca = kwargs.pop('marca', None)
        modelo = kwargs.pop('modelo', None)
        super(VehiculoForm, self).__init__(*args, **kwargs)
        marcas = Vehiculo.objects.values_list('marca', flat=True).distinct()
        self.fields['marca'] = forms.ChoiceField(
            choices=[('', 'Seleccione una marca')] + [(marca, marca) for marca in marcas],
            widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_marca'})
        )
        if marca:
            modelos = Vehiculo.objects.filter(marca=marca).values_list('modelo', flat=True).distinct()
            self.fields['modelo'] = forms.ChoiceField(
                choices=[('', 'Seleccione un modelo')] + [(modelo, modelo) for modelo in modelos],
                widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_modelo'})
            )
        else:
            self.fields['modelo'] = forms.ChoiceField(
                choices=[('', 'Seleccione un modelo')],
                widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_modelo'})
            )
        if marca and modelo:
            tipos = Vehiculo.objects.filter(marca=marca, modelo=modelo).values_list('tipo', flat=True).distinct()
            self.fields['tipo'] = forms.ChoiceField(
                choices=[('', 'Seleccione un tipo')] + [(tipo, tipo) for tipo in tipos],
                widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_tipo'})
            )
        else:
            self.fields['tipo'] = forms.ChoiceField(
                choices=[('', 'Seleccione un tipo')],
                widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_tipo'})
            )

    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'tipo', 'año']
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CargarVehiculoForm(forms.ModelForm):
    tarifa_id = forms.ModelChoiceField(queryset=tarifas.objects.all(), to_field_name="id")
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'año', 'tipo', 'tarifa_id']