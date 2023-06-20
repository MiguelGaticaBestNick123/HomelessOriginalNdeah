from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from .forms import LoginForm, CustomUserCreationForm 
from django.shortcuts import render,get_object_or_404,redirect
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

def notasmedicas(request):
    return render (request, 'aplicacion/notasmedicas.html')





















def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            User = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, User)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data['form'] = formulario
    
    
    return render (request, 'registration/registro.html', data)