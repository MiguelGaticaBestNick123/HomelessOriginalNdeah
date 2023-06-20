
from django.urls import path
from .views import index, Login, notasmedicas, verpagos, registro

urlpatterns = [
    path('', index, name="index"),
    path('verpagos', verpagos, name='verpagos'),
    path('login', Login, name="login"),
    path('registro/', registro, name="registro"),
    path('notasmedicas', notasmedicas, name="notasmedicas")
    # path('pagar', pagar, name="pagar")
    path('notasmedicas', notasmedicas, name="notasmedicas"),
    path('registro/', registro, name="registro"),
]
