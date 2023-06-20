
from django.urls import path
from .views import index, Login, notasmedicas, verpagos

urlpatterns = [
    path('', index, name="index"),
    path('verpagos', verpagos, name='verpagos'),
    path('login', Login, name="login"),
    path('notasmedicas', notasmedicas, name="notasmedicas")
    
    
    
    
    
    path('pagar', pagar, name="pagar")
    
]
