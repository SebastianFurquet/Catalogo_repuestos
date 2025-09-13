from django.urls import path
from . import views

urlpatterns = [
    
    
    #path('', views.base, name='base'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
    # LISTA
    path('clases/', views.ClaseListView.as_view() , name='clase_list'), # Esta es la nueva URL vinculada a la clase ClaseListView
    
    # DETALLE
    path('clases/detail/<int:pk>',views.ClaseDetailView.as_view(), name='clase_detail'), # Esta es la nueva URL vinculada a la clase ClaseDetailView
    
    # ELIMINACION
    path('clases/delete/<int:pk>',views.ClaseDeleteView.as_view(), name='clase_delete'), # Esta es la nueva URL vinculada a la clase ClaseDeleteView
    
    # CREACION
    #path('clases/from', views.clase_from, name='clase_form' ), URL de Funcion Create
    path('clases/from', views.ClaseCreateView.as_view(), name='clase_form' ), # Esta es la nueva URL vinculada a la clase ClaseCreateView
    
    # ACTUALIZACIONN
    #path('clases/update/<int:pk>',views.clase_update, name='clase_update'), # URL de Funcion Update
    path('clases/update/<int:pk>',views.ClaseUpdateView.as_view(), name='clase_update'), # Esta es la nueva URL vinculada a la clase ClaseUpdateView
    


]
