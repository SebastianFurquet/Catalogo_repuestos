from django import forms
from .models import Clase, Marca, Modelo, Parte, Elemento, Estructura


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


class EstructuraForm(forms.ModelForm):
    imagen = forms.ImageField(required=False)

    clase = forms.ModelChoiceField(
        queryset=Clase.objects.none(),
        empty_label="Seleccione una Clase",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    marca = forms.ModelChoiceField(
        queryset=Marca.objects.none(),
        empty_label="Seleccione una Marca",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    modelo = forms.ModelChoiceField(
        queryset=Modelo.objects.none(),
        empty_label="Seleccione un Modelo",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    # cod_veh = forms.ModelChoiceField(
    #     queryset=Modelo.objects.none(),
    #     empty_label="Seleccione un codigo",
    #     widget=forms.Select(attrs={"class": "form-select"})
    # )
    parte = forms.ModelChoiceField(
        queryset=Parte.objects.none(),
        empty_label="Seleccione una Ubicacion",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    elemento = forms.ModelChoiceField(
        queryset=Elemento.objects.none(),
        empty_label="Seleccione un Elemento",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Estructura
        fields = ["clase", "marca", "modelo", "parte", "elemento", "nro_pieza", "precio", "imagen"]

    def __init__(self, *args, **kwargs):
        """
        Seteamos todos los querysets ordenados por campos que EXISTEN.
        Si en el futuro se quiere filtrar modelo por marca/clase, este es el lugar.
        """
        super().__init__(*args, **kwargs)
        self.fields["clase"].queryset = Clase.objects.order_by("cod_clase")
        self.fields["marca"].queryset = Marca.objects.order_by("cod_marca")   # o .order_by("nombre")
        self.fields["modelo"].queryset = Modelo.objects.order_by("cod_modelo")
        self.fields["parte"].queryset  = Parte.objects.order_by("cod_parte")
        self.fields["elemento"].queryset = Elemento.objects.order_by("cod_elemento")
        
        # 2) Etiqueta personalizada SOLO para el desplegable de Modelo:
        #    Usamos la descripción, y si viene vacía, mostramos un fallback.
        
        self.fields["modelo"].label_from_instance = lambda obj: (obj.descripcion or "Sin descripción")

    
    def save(self, commit=True):
        obj = super().save(commit=False)
        # Derivo el cod_veh del modelo elegido, así NUNCA se des-sincroniza
        obj.cod_veh = obj.modelo.cod_veh if obj.modelo_id else None
        if commit:
            obj.save()
        return obj