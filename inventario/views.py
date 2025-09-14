from django.contrib.auth.decorators import login_required # esto se usa con las funciones
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Clase, Marca, Modelo, Parte, Elemento, Estructura
from .forms import ClaseForm, MarcaForm, ModeloForm, ParteForm, ElementoForm, EstructuraForm

# Create your views here.

def base(request):
    return render(request, 'inventario/base.html')

# def index(request):
#     return render(request, 'inventario/index.html')

def about(request):
    return render(request, 'inventario/about.html')

# **************************************************************************************
# LEER - con Funcion -- LISTA + BUSQUEDA

def clase_list(request):
    busqueda = request.GET.get('busqueda', None)
    if busqueda:
        clase_list=Clase.objects.filter(
        Q(cod_clase__icontains=busqueda) | # Con el modulo Q puedo convinar la busqueda de varios campos
        Q(nombre__icontains=busqueda)
        )
    else:
        clase_list = Clase.objects.all()
    return render(request, 'inventario/clase/clase_list.html', {'clase': clase_list})

# --------------------------
# Clase Basada en vista LISTA + BUSQUEDA

class ClaseListView(ListView):
    model = Clase
    template_name = 'inventario/clase/clase_list.html'
    context_object_name = 'clase'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                Q(cod_clase__icontains=busqueda) | # Con el modulo Q puedo convinar la busqueda de varios campos
                Q(nombre__icontains=busqueda)
            )
        return queryset    


# **************************************************************************************
# DETALLE
def clase_detail(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    return render(request, 'inventario/clase/clase_detail.html', {'clase': clase})


# --------------------------
# Clase Basada en vista para DETALLE

class ClaseDetailView(DetailView): # por defecto usa el contexto object
    model = Clase
    template_name = 'inventario/clase/clase_detail.html'
    #context_object_name = 'clase'


# ***************************************************************************************
# CREAR-FORM

def clase_from(request): 
    if request.method == 'POST':
        form = ClaseForm(request.POST)
        if form.is_valid():
            cod_clase = form.cleaned_data['cod_clase']
            nombre = form.cleaned_data['nombre']
            clase = Clase(cod_clase=cod_clase, nombre=nombre)
            clase.save()
            return redirect('clase_list')
    else:
        form = ClaseForm()
    return render(request, 'inventario/clase/clase_form.html', {'form': form})    

# --------------------------
# Clase Basada en vista para CREAR-FORM

class ClaseCreateView(LoginRequiredMixin, CreateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'inventario/clase/clase_form.html'
    success_url = reverse_lazy('clase_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.add_error(None, 'No se puede guardar el registro porque no ha iniciado sesión')
            return self.form_invalid(form)
        return super().form_valid(form)


# *************************************************************************************

# def clase_buscar(request):
#     if request.method =='GET':
#         form = BusquedaClaseForm(request.GET)
#         if form.is_valid():
#             cod_clase = form.cleaned_data['cod_clase']
#             #nombre = form.cleaned_data['nombre']
#             resultados = Clase.objects.filter(cod_clase__icontains=cod_clase) #nombre__icontains=nombre)
#             return render(request, 'inventario/clase_buscar_resultado.html', {'resultados': resultados, 'form':form})
#     else:
#         form = BusquedaClaseForm()
#     return render(request, 'inventario/clase_buscar.html', {'form':form})


# ***************************************************************************************
# ELIMINAR

class ClaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Clase
    template_name = 'inventario/clase/clase_confirm_delete.html'
    success_url = reverse_lazy('clase_list')

# ***************************************************************************************
# ACTUALIZAR c/funcion

def clase_update(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    if request.method == 'POST':
        form = ClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            return redirect('clase_list')
    else:
        form = ClaseForm(instance=clase)
    return render(request, 'inventario/clase/clase_update.html', {'form': form})

# --------------------------
# Clase Basada en vista para UPDATE

class ClaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'inventario/clase/clase_update.html'
    success_url = reverse_lazy('clase_list')
    
    
# ***************************************************************************************
#/////////////////////////////---- MARCA ----//////////////////////////////////////////

# Clase Basada en vista LISTA + BUSQUEDA

class MarcaListView(ListView):
    model = Marca
    template_name = 'inventario/marca/marca_list.html'
    context_object_name = 'marca'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                Q(cod_marca__icontains=busqueda) | # Con el modulo Q puedo combinar la busqueda de varios campos
                Q(nombre__icontains=busqueda)
            )
        return queryset    
    

# Clase Basada en vista para CREAR-FORM

class MarcaCreateView(LoginRequiredMixin, CreateView):
    model = Marca
    form_class = MarcaForm
    #context_object_name = 'marca'
    template_name = 'inventario/marca/marca_form.html'
    success_url = reverse_lazy('marca_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.add_error(None, 'No se puede guardar el registro porque no ha iniciado sesión')
            return self.form_invalid(form)
        return super().form_valid(form)
    

# Clase Basada en vista para DETALLE

class MarcaDetailView(DetailView): # por defecto usa el contexto object
    model = Marca
    template_name = 'inventario/marca/marca_detail.html'
    #context_object_name = 'marca'


# Clase Basada en vista para UPDATE

class MarcaUpdateView(LoginRequiredMixin, UpdateView):
    model = Marca
    form_class = MarcaForm
    template_name = 'inventario/marca/marca_update.html'
    success_url = reverse_lazy('marca_list')

# ELIMINAR

class MarcaDeleteView(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = 'inventario/marca/marca_confirm_delete.html'
    success_url = reverse_lazy('marca_list')


# ***************************************************************************************
#/////////////////////////////---- MODELO ----//////////////////////////////////////////

# Clase Basada en vista LISTA + BUSQUEDA

class ModeloListView(ListView):
    model = Modelo
    template_name = 'inventario/modelo/modelo_list.html'
    context_object_name = 'modelo'
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('marca', 'clase').order_by('cod_modelo')
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                Q(descripcion__icontains=busqueda) |
                Q(marca__nombre__icontains=busqueda) |   # FK → campo texto del relacionado
                Q(clase__nombre__icontains=busqueda) |   # FK → idem
                Q(cod_modelo__icontains=busqueda) |      # si es CharField
                Q(cod_veh__icontains=busqueda)           # si es CharField
            )
        return queryset    
    

# Clase Basada en vista para CREAR-FORM

class ModeloCreateView(LoginRequiredMixin, CreateView):
    model = Modelo
    form_class = ModeloForm
    #context_object_name = 'marca'
    template_name = 'inventario/modelo/modelo_form.html'
    success_url = reverse_lazy('modelo_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.add_error(None, 'No se puede guardar el registro porque no ha iniciado sesión')
            return self.form_invalid(form)
        return super().form_valid(form)
    

# Clase Basada en vista para DETALLE

class ModeloDetailView(DetailView): # por defecto usa el contexto object
    model = Modelo
    template_name = 'inventario/modelo/modelo_detail.html'
    #context_object_name = 'marca'


# Clase Basada en vista para UPDATE

class ModeloUpdateView(LoginRequiredMixin, UpdateView):
    model = Modelo
    form_class = ModeloForm
    template_name = 'inventario/modelo/modelo_update.html'
    success_url = reverse_lazy('modelo_list')

# ELIMINAR

class ModeloDeleteView(LoginRequiredMixin, DeleteView):
    model = Modelo
    template_name = 'inventario/modelo/modelo_confirm_delete.html'
    success_url = reverse_lazy('modelo_list')


# ***************************************************************************************
#/////////////////////////////---- PARTE ----//////////////////////////////////////////

# Clase Basada en vista LISTA + BUSQUEDA

class ParteListView(ListView):
    model = Parte
    template_name = 'inventario/parte/parte_list.html'
    context_object_name = 'parte'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                Q(cod_parte__icontains=busqueda) | # Con el modulo Q puedo combinar la busqueda de varios campos
                Q(nombre__icontains=busqueda)
            )
        return queryset    
    

# Clase Basada en vista para CREAR-FORM

class ParteCreateView(LoginRequiredMixin, CreateView):
    model = Parte
    form_class = ParteForm
    template_name = 'inventario/parte/parte_form.html'
    success_url = reverse_lazy('parte_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.add_error(None, 'No se puede guardar el registro porque no ha iniciado sesión')
            return self.form_invalid(form)
        return super().form_valid(form)
    

# Clase Basada en vista para DETALLE

#class ParteDetailView(DetailView): # por defecto usa el contexto object
#    model = Parte
#    template_name = 'inventario/parte/parte_detail.html'
#    #context_object_name = 'marca'


# Clase Basada en vista para UPDATE

class ParteUpdateView(LoginRequiredMixin, UpdateView):
    model = Parte
    form_class = ParteForm
    template_name = 'inventario/parte/parte_update.html'
    success_url = reverse_lazy('parte_list')

# ELIMINAR

class ParteDeleteView(LoginRequiredMixin, DeleteView):
    model = Parte
    template_name = 'inventario/parte/parte_confirm_delete.html'
    success_url = reverse_lazy('parte_list')
    
    

# ***************************************************************************************
#/////////////////////////////---- ELEMENTOS ----//////////////////////////////////////////

# Clase Basada en vista LISTA + BUSQUEDA

class ElementoListView(ListView):
    model = Elemento
    template_name = 'inventario/elemento/elemento_list.html'
    context_object_name = 'elemento'
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('parte', 'clase').order_by('cod_elemento')
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                Q(cod_elemento__icontains=busqueda) |
                Q(parte__nombre__icontains=busqueda) |   # FK → campo texto del relacionado
                Q(clase__nombre__icontains=busqueda) |   # FK → idem
                Q(nombre__icontains=busqueda)     
            )
        return queryset    
    

# Clase Basada en vista para CREAR-FORM

class ElementoCreateView(LoginRequiredMixin, CreateView):
    model = Elemento
    form_class = ElementoForm
    template_name = 'inventario/elemento/elemento_form.html'
    success_url = reverse_lazy('elemento_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.add_error(None, 'No se puede guardar el registro porque no ha iniciado sesión')
            return self.form_invalid(form)
        return super().form_valid(form)
    

# Clase Basada en vista para DETALLE

class ElementoDetailView(DetailView): # por defecto usa el contexto object
    model = Elemento
    template_name = 'inventario/elemento/elemento_detail.html'
    #context_object_name = 'marca'


# Clase Basada en vista para UPDATE

class ElementoUpdateView(LoginRequiredMixin, UpdateView):
    model = Elemento
    form_class = ElementoForm
    template_name = 'inventario/elemento/elemento_update.html'
    success_url = reverse_lazy('elemento_list')

# ELIMINAR

class ElementoDeleteView(LoginRequiredMixin, DeleteView):
    model = Elemento
    template_name = 'inventario/elemento/elemento_confirm_delete.html'
    success_url = reverse_lazy('elemento_list')



# ***************************************************************************************
#/////////////////////////////---- ESTRUCTURA ----//////////////////////////////////////////

# Clase Basada en vista LISTA + BUSQUEDA

class EstructuraListView(ListView):
    model = Estructura
    template_name = 'inventario/estructura/estructura_list.html'
    context_object_name = 'estructura'
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('clase','marca','modelo','parte','elemento').order_by('elemento')
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                Q(clase__nombre__icontains=busqueda)  |   # FK → campo texto del relacionado
                Q(marca__nombre__icontains=busqueda)  |
                Q(modelo__descripcion__icontains=busqueda) |
                Q(parte__nombre__icontains=busqueda)  |   
                Q(elemento__cod_elemento__icontains=busqueda)   |
                Q(elemento__nombre__icontains=busqueda)   |
                Q(nro_pieza__icontains=busqueda)     
            )
        return queryset    
    

# Clase Basada en vista para CREAR-FORM

class EstructuraCreateView(LoginRequiredMixin, CreateView):
    model = Estructura
    form_class = EstructuraForm
    template_name = 'inventario/estructura/estructura_form.html'
    success_url = reverse_lazy('estructura_list')
    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        else:
            form.add_error(None, 'No se puede guardar el registro porque no ha iniciado sesión')
            return self.form_invalid(form)
        return super().form_valid(form)
    

# Clase Basada en vista para DETALLE

class EstructuraDetailView(DetailView): # por defecto usa el contexto object
    model = Estructura
    template_name = 'inventario/estructura/estructura_detail.html'
    #context_object_name = 'marca'


# Clase Basada en vista para UPDATE

class EstructuraUpdateView(LoginRequiredMixin, UpdateView):
    model = Estructura
    form_class = EstructuraForm
    template_name = 'inventario/estructura/estructura_update.html'
    success_url = reverse_lazy('estructura_list')

# ELIMINAR

class EstructuraDeleteView(LoginRequiredMixin, DeleteView):
    model = Estructura
    template_name = 'inventario/estructura/estructura_confirm_delete.html'
    success_url = reverse_lazy('estructura_list')
    


# ***************************************************************************************
#/////////////////////////////---- CATALOGO ----//////////////////////////////////////////

# Clase Basada en vista LISTA + BUSQUEDA

class CatalogoListView(ListView):
    model = Estructura
    template_name = 'inventario/index.html'
    context_object_name = 'estructura'
    
    def get_queryset(self):
        queryset = super().get_queryset().select_related('clase','marca','modelo','parte','elemento').order_by('elemento')
        busqueda = self.request.GET.get('busqueda', None)
        if busqueda:
            queryset = queryset.filter(
                # FK → campo texto del relacionado
                Q(marca__nombre__icontains=busqueda)  |
                Q(modelo__descripcion__icontains=busqueda) |
                Q(parte__nombre__icontains=busqueda)  |   
                Q(elemento__cod_elemento__icontains=busqueda)   |
                Q(elemento__nombre__icontains=busqueda)   |
                Q(nro_pieza__icontains=busqueda)     
            )
        return queryset    