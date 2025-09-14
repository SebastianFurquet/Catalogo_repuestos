from django import forms
from .models import Clase, Marca, Modelo, Parte, Elemento


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
    
    clase = forms.ModelChoiceField(
        queryset=Clase.objects.order_by("cod_clase"),   # orden alfabético en el combo
        empty_label="Seleccione una clase",          # placeholder de la opción vacía
        widget=forms.Select(attrs={"class": "form-select"})  # estilo Bootstrap
    )
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.order_by("cod_marca"),
        empty_label="Seleccione una marca",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Modelo
        fields = ["cod_modelo", "clase", "marca", "descripcion", "cod_veh", "imagen"]


class ParteForm(forms.ModelForm):
    class Meta:
        model = Parte
        fields = '__all__' 



class ElementoForm(forms.ModelForm):
    #imagen = forms.ImageField(required=False)
    
    clase = forms.ModelChoiceField(
        queryset=Clase.objects.order_by("cod_clase"),   # orden alfabético en el combo
        empty_label="Seleccione una clase",          # placeholder de la opción vacía
        widget=forms.Select(attrs={"class": "form-select"})  # estilo Bootstrap
    )
    parte = forms.ModelChoiceField(
        queryset=Parte.objects.order_by("cod_parte"),
        empty_label="Seleccione una ubicacion",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Elemento
        fields = ["cod_elemento", "clase", "parte", "nombre"]