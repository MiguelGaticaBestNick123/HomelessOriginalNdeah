from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
# Create your views here.

def index(request):
    return render(request, 'aplicacion/index.html')

def login(request):
    return render(request, 'aplicacion/registration/login.html')

# @permission_required('aplicacion.view_login')