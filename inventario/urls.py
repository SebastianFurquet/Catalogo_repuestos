from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('clases/', views.clase_list, name='clase_list'),
    path('clases/<int:pk>/', views.clase_detail, name='clase_detail'),
    path('clases/from', views.clase_from, name='clase_form' ),
    #path('clases/busqueda', views.clase_buscar, name='clase_buscar')
]
