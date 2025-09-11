from django.urls import path
from usuarios.views import registro, login_request, perfil, editar_perfil, EditarContrasenia
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name= 'usuarios/logout.html'), name='logout'), 
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar', editar_perfil, name='editar_perfil'),
    path('perfil/editar/contrasenia', EditarContrasenia.as_view(), name='editar_contrasenia'),
    ]