from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Clase 
from .forms import ClaseForm, BusquedaClaseForm



# Create your views here.

def base(request):
    return render(request, 'inventario/base.html')

def clase_list(request):
    busqueda = request.GET.get('busqueda', None)
    if busqueda:
        clase_list=Clase.objects.filter(
        Q(cod_clase__icontains=busqueda) | # Con el modulo Q puedo convinar la busqueda de varios campos
        Q(nombre__icontains=busqueda)
        )
    else:
        clase_list = Clase.objects.all()
    return render(request, 'inventario/clase_list.html', {'clase': clase_list})

def clase_detail(request, pk):
    clase = get_object_or_404(Clase, pk=pk)
    return render(request, 'inventario/clase_detail.html', {'clase': clase})

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
    return render(request, 'inventario/clase_form.html', {'form': form})    

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

