
from django.urls import path
from .views import index, Login, notasmedicas

urlpatterns = [
    path('', index, name="index"),

    path('login', Login, name="login"),
    path('notasmedicas', notasmedicas, name="notasmedicas")
]
