from django.contrib import admin
from .models import Clase
# Register your models here.

#admin.site.register(Clase)
@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ['cod_clase', 'nombre'] # son las columnas de datos que veo en el admin
    list_filter = ['cod_clase', 'nombre'] # Cuadro de filtro derecho
    search_fields = ['cod_clase', 'nombre'] # barra de busqueda
    ordering = ['cod_clase'] # orden por el campo que elija