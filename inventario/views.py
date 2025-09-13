from django.contrib.auth.decorators import login_required # esto se usa con las funciones
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Clase 
from .forms import ClaseForm



# Create your views here.

def base(request):
    return render(request, 'inventario/base.html')

def index(request):
    return render(request, 'inventario/index.html')

def about(request):
    return render(request, 'inventario/about.html')

# **************************************************************************************
# LEER - con Funcion

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
# Clase Basada en vista para LEER

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
# CREAR

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
# Clase Basada en vista para CREAR

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
# Clase Basada en vista para Update

class ClaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'inventario/clase/clase_update.html'
    success_url = reverse_lazy('clase_list')
    
    
# ***************************************************************************************