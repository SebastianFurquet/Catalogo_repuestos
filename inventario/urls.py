from django.urls import path
from . import views

urlpatterns = [
    
    
    #path('', views.base, name='base'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # ---------------------------------------------// CLASES // -----------------------------------------------
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
    
    # ---------------------------------------------// MARCAS // -----------------------------------------------
    # LISTA
    path('marcas/', views.MarcaListView.as_view() , name='marca_list'),
    
    # CREACION
    path('marcas/from', views.MarcaCreateView.as_view(), name='marca_form' ),
    
    # DETALLE
    path('marcas/detail/<int:pk>',views.MarcaDetailView.as_view(), name='marca_detail'), 
    
    # ACTUALIZACIONN
    path('marcas/update/<int:pk>',views.MarcaUpdateView.as_view(), name='marca_update'),
    
    # ELIMINACION
    path('marcas/delete/<int:pk>',views.MarcaDeleteView.as_view(), name='marca_delete'),
    
    
    # ---------------------------------------------// MODELOS // -----------------------------------------------
    # LISTA
    path('modelos/', views.ModeloListView.as_view() , name='modelo_list'),
    
    # CREACION
    path('modelos/from', views.ModeloCreateView.as_view(), name='modelo_form' ),
    
    # DETALLE
    path('modelos/detail/<int:pk>',views.ModeloDetailView.as_view(), name='modelo_detail'), 
    
    # ACTUALIZACIONN
    path('modelos/update/<int:pk>',views.ModeloUpdateView.as_view(), name='modelo_update'),
    
    # ELIMINACION
    path('modelos/delete/<int:pk>',views.ModeloDeleteView.as_view(), name='modelo_delete'),
    
    # ---------------------------------------------// PARTES // -----------------------------------------------
    # LISTA
    path('partes/', views.ParteListView.as_view() , name='parte_list'),
    
    # CREACION
    path('partes/from', views.ParteCreateView.as_view(), name='parte_form' ),
    
    # DETALLE
    #path('partes/detail/<int:pk>',views.ParteDetailView.as_view(), name='parte_detail'), 
    
    # ACTUALIZACIONN
    path('partes/update/<int:pk>',views.ParteUpdateView.as_view(), name='parte_update'),
    
    # ELIMINACION
    path('partes/delete/<int:pk>',views.ParteDeleteView.as_view(), name='parte_delete'),
    
    # ---------------------------------------------// ELEMENTOS // -----------------------------------------------
    # LISTA
    path('elemetos/', views.ElementoListView.as_view() , name='elemento_list'),
    
    # CREACION
    path('elemetos/from', views.ElementoCreateView.as_view(), name='elemento_form' ),
    
    # DETALLE
    path('elemetos/detail/<int:pk>',views.ElementoDetailView.as_view(), name='elemento_detail'), 
    
    # ACTUALIZACIONN
    path('elemetos/update/<int:pk>',views.ElementoUpdateView.as_view(), name='elemento_update'),
    
    # ELIMINACION
    path('elemetos/delete/<int:pk>',views.ElementoDeleteView.as_view(), name='elemento_delete'),
    
    # ---------------------------------------------// ESTRUCTURA // -----------------------------------------------
    # LISTA
    path('estructuras/', views.EstructuraListView.as_view() , name='estructura_list'),
    
    # CREACION
    path('estructuras/from', views.EstructuraCreateView.as_view(), name='estructura_form' ),
    
    # DETALLE
    path('estructuras/detail/<int:pk>',views.EstructuraDetailView.as_view(), name='estructura_detail'), 
    
    # ACTUALIZACIONN
    path('estructuras/update/<int:pk>',views.EstructuraUpdateView.as_view(), name='estructura_update'),
    
    # ELIMINACION
    path('estructuras/delete/<int:pk>',views.EstructuraDeleteView.as_view(), name='estructura_delete'),

        # Catalogo
    path('estructuras/detail/catalogo',views.CatalogoListView.as_view(), name='index'),
]
