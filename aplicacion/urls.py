
from django.urls import path
from .views import index, Login, notasmedicas, verpagos, registro, pagar, donacion

urlpatterns = [
    path('', index, name="index"),
    path('verpagos', verpagos, name='verpagos'),
    path('login', Login, name="login"),
    path('registro/', registro, name="registro"),
    path('pagar', pagar, name="pagar"),
    path('notasmedicas', notasmedicas, name="notasmedicas"),
    path('registro/', registro, name="registro"),
    path('donacion/', donacion, name='donacion'),
]
