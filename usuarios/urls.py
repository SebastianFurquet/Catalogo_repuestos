from django.urls import path
from usuarios.views import registro, login_request, Logout
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    #path('logout/', auth_views.LogoutView.as_view(next_page='usuarios/logout.html'), name='logout'), # le deberia poner a donde me redirige 
    path('logout/', LogoutView.as_view(template_name= 'usuarios/logout.html'), name='logout'), 
    path('registro/', registro, name='registro'),
]