from django import forms
from .models import Clase, Marca, Modelo

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__' #['cod_clase', 'nombre']
        
class MarcaForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Marca
        fields = '__all__' #['cod_marca', 'nombre', etc]
        
class ModeloForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)
    class Meta:
        model = Modelo
        fields = '__all__' #['cod_marca', 'nombre', etc]


