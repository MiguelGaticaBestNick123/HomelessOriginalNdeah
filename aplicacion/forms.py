from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Pago
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    
    class Meta:
        Model = User
        fields = ["username","password1"]
        model = Pago
class CustomUserCreationForm(UserCreationForm):
    pass
class FrmPagar(forms.ModelForm):
    class Meta: 
        fields = ("tipo_pago","nro_tarjeta","fecha_caducidad","titular")
        
class CustomUserCreationForm(UserCreationForm):
    pass
