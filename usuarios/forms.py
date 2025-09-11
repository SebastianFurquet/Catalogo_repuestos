from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
        labels = {
            'username': 'Usuario',  # Define la etiqueta personalizada para el campo 'username'
        }
        
class EditarPerfilForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    
    class Meta:
        model= User
        fields = [ 'email', 'first_name', 'last_name']
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }
        help_texts = {k:"" for k in fields}
        
        
class EditarContraseniaForm(PasswordChangeForm):
    
    old_password = forms.CharField(
    label="Contraseña actual",
    widget=forms.PasswordInput()
    )
    new_password1 = forms.CharField(
        label="Nueva contraseña",
        widget=forms.PasswordInput()
    )
    new_password2 = forms.CharField(
        label="Confirmar nueva contraseña",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']