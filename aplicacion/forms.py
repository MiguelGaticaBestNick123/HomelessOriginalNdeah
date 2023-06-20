from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    
    class Meta:
        Model = User
        fields = ["username","password1"]
        
class CustomUserCreationForm(UserCreationForm):
    pass
