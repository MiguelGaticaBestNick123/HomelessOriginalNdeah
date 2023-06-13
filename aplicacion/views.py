from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'aplicacion/index.html')

def iniciosession(request):
    return render(request, 'aplicacion/iniciosession.html')
def aportes(request):
    return render(request,'aplicacion/aportes.html')