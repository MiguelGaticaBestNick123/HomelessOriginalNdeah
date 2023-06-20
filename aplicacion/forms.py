from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    
    class Meta:
        Model = User
        fields = ["username","password1"]