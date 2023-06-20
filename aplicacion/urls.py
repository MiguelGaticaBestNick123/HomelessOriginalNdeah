
from django.urls import path
from .views import index, Login, notasmedicas, registro

urlpatterns = [
    path('', index, name="index"),

    path('login', Login, name="login"),
    path('notasmedicas', notasmedicas, name="notasmedicas"),
    path('registro/', registro, name="registro"),
]
