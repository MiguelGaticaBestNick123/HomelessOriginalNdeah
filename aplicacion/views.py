from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm
from django.shortcuts import render,get_object_or_404,redirect
from .models import Accion, DetallePlan

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
    return render(request, 'aplicacion/registration/login.html', contexto)

@login_required
def notasmedicas(request):
    notas= Accion.objects.all()
    contexto= {
        "notas":notas
    }
    return render (request, 'aplicacion/administrador/notasmedicas.html', contexto)

def verpagos(request):
    pago= DetallePlan.objects.all()
    contexto = {
        "pago":pago
    }
    return render (request, 'aplicacion/administrador/pagos.html', contexto)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

