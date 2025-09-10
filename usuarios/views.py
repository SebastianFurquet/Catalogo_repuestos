from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from usuarios.forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView
from django.contrib import messages

# Create your views here.

def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return redirect('clase_list')  # envía al usuario a la página inicial por ahora clase_list
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')
                return render(request, 'usuarios/login.html', {"formulario": formulario, 'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'usuarios/login.html', {"formulario": formulario, 'mensaje': 'Usuario o contraseña incorrectos'})
    
    else:
        formulario = AuthenticationForm()
        return render(request, "usuarios/login.html", {"formulario": formulario})
    


def registro(request):

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return redirect('clase_list') # envía al usuario a la página inicial o a la pagina de registro //por ahora clase_list
        else:
            return render(request, 'usuarios/registro.html', {"formulario": formulario})

    else:
        formulario = CustomUserCreationForm()
        return render(request,"usuarios/registro.html" ,  {"formulario": formulario})

class Logout(LogoutView):
    template_name = "usuarios/logout.html"
    
    
    
    
    
    
def iniciar_sesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.get_user()
            
            login(request, usuario)
            return redirect('clase_list') # envía al usuario a la página inicial por ahora clase_list        
    else:
        formulario = AuthenticationForm()
        return render(request, "usuarios/login.html", {"formulario": formulario})