# expenses/forms.py
from django import forms
from .models import Departamento, Empleado, Gasto

class FiltroFechaForm(forms.Form):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2'})
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2'})
    )

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['dept']
        widgets = {
            'dept': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'})
        }

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'departamento']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'departamento': forms.Select(attrs={'class': 'border rounded p-2 w-full'})
        }

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['fecha', 'descripcion', 'monto', 'empleado']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'border rounded p-2 w-full'}),
            'descripcion': forms.TextInput(attrs={'class': 'border rounded p-2 w-full'}),
            'monto': forms.NumberInput(attrs={'class': 'border rounded p-2 w-full'}),
            'empleado': forms.Select(attrs={'class': 'border rounded p-2 w-full'}),
            
        }