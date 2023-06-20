from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm, CustomUserCreationForm 
from django.shortcuts import render,get_object_or_404,redirect
from .models import Accion, DetallePlan
from django.contrib.auth import authenticate, login
from django.contrib import messages
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
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        if formulario.is_valid():
        formulario = CustomUserCreationForm(data=request.POST)
            formulario.save()
            User = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, User)
            return redirect(to="index")
            messages.success(request, "Te has registrado correctamente")
        data['form'] = formulario
    return render (request, 'registration/registro.html', data)
        