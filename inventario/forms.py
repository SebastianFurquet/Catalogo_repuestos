from django import forms
from .models import Clase

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__' #['cod_clase', 'nombre']
        

class BusquedaClaseForm(forms.Form):
    cod_clase = forms.CharField(label= 'Cod Clase')
    #nombre = forms.CharField(label= 'nombre')