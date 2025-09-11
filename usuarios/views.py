from .forms import EditarContraseniaForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm 
from usuarios.forms import CustomUserCreationForm, EditarPerfilForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib import messages

# Create your views here.

# <!-- Login -->

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
    

# <!-- Registro -->

def registro(request):

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            return redirect('login') # envía al usuario a la página de login para que inicie sesion
        else:
            return render(request, 'usuarios/registro.html', {"formulario": formulario})

    else:
        formulario = CustomUserCreationForm()
        return render(request,"usuarios/registro.html" ,  {"formulario": formulario})



# <!-- Logout -->

class Logout(LogoutView):
    template_name = "usuarios/logout.html"
    
    
@login_required
def perfil(request):
    usuario = request.user
    contexto = {
        "usuario": usuario,
        "username": usuario.username,
        "email": usuario.email,
        "first_name": usuario.first_name,
        "last_name": usuario.last_name,
        # Si usás campos extras en tu modelo de usuario (ej: avatar, bio, etc.) también podés pasarlos acá
        # "avatar": usuario.avatar.url if usuario.avatar else None,
    }

    return render(request, 'usuarios/perfil.html', contexto)


# <!-- Editar Perfil -->

@login_required
def editar_perfil(request):
    
    if request.method == 'POST':
        formulario = EditarPerfilForm(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')  # envía al usuario a su perfil después de editar el perfil
    else:
        formulario = EditarPerfilForm(instance=request.user)
    return render(request, 'usuarios/editar_perfil.html', {"formulario": formulario})



# <!-- Editar Contraseña -->

class EditarContrasenia(PasswordChangeView):
    template_name = "usuarios/editar_contrasenia.html"
    success_url = reverse_lazy('perfil')  # envía al usuario a la página perfil
    form_class = EditarContraseniaForm






# -----------------------------------------------------------------------------------------------------    
    
    
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
    
    

def registrarse(request):
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('login')
    else:
        formulario = CustomUserCreationForm()
    return render(request, "usuarios/registro.html", {"formulario": formulario})
