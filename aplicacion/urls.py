
from django.urls import path
from .views import index, iniciosession, aportes

urlpatterns = [
    path('', index, name="index"),

    path('iniciosession/', iniciosession, name="iniciosession"),
    path('aportes/', aportes, name="aportes")
]
