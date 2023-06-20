
from django.urls import path
from .views import index, iniciosession, notasmedicas

urlpatterns = [
    path('', index, name="index"),

    path('iniciosession', iniciosession, name="iniciosession"),
    path('notasmedicas', notasmedicas, name="notasmedicas")
]
