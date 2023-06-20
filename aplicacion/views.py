from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm
from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.

def index(request):
    return render(request, 'aplicacion/index.html')

def Login(request):
    
    form= LoginForm
    contexto = {
        "form": form
    }
    if request.method == "POST":
        form.save()
        return redirect(to="index.html")
    return render(request, 'aplicacion/registration/login.html')

def notasmedicas(request):
    return render (request, 'aplicacion/notasmedicas.html')

# @permission_required('aplicacion.view_login')