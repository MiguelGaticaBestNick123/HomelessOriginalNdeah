from django import forms
from django.contrib.auth.models import User
from .models import Pago


class LoginForm(forms.ModelForm):
    
    class Meta:
        Model = User
        fields = ["username","password1"]






























class FrmPagar(forms.ModelForm):
    class Meta: 
        model = Pago
        fields = ("tipo_pago","nro_tarjeta","fecha_caducidad","titular")
                
        