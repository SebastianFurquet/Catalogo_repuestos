from django.contrib import admin
from .models import Clase, Marca, Modelo, Parte, Elemento, Estructura
# Register your models here.

#admin.site.register(Clase)
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ['cod_clase', 'nombre'] # son las columnas de datos que veo en el admin
    list_filter = ['cod_clase', 'nombre'] # Cuadro de filtro derecho
    search_fields = ['cod_clase', 'nombre'] # barra de busqueda
    ordering = ['cod_clase'] # orden por el campo que elija
    
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ["cod_marca", "nombre"]
    search_fields = ["cod_marca", "nombre"]
    ordering = ['cod_marca'] # orden por el campo que elija
    
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ["cod_modelo", "marca", "clase", "descripcion", "cod_veh"]
    list_filter = ["marca", "clase"]
    search_fields = ["cod_modelo", "descripcion", "cod_veh"]
    ordering = ['cod_modelo'] # orden por el campo que elija

@admin.register(Parte)
class ParteAdmin(admin.ModelAdmin):
    list_display = ["cod_parte", "nombre"]
    search_fields = ["cod_parte", "nombre"]
    ordering = ['cod_parte'] # orden por el campo que elija
    
@admin.register(Elemento)
class ElementoAdmin(admin.ModelAdmin):
    list_display = ["cod_elemento", "nombre", "clase", "parte"]
    list_filter = ["clase", "parte"]
    search_fields = ["cod_elemento", "nombre"]
    ordering = ['cod_elemento'] # orden por el campo que elija

@admin.register(Estructura)
class EstructuraAdmin(admin.ModelAdmin):
    list_display = ["modelo", "parte", "elemento", "nro_pieza", "precio"]
    list_filter = ["modelo__marca", "modelo__clase", "parte"]
    search_fields = ["nro_pieza", "elemento__cod_elemento", "elemento__nombre", "modelo__cod_modelo"]