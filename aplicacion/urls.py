
from django.urls import path
from .views import index, iniciosession

urlpatterns = [
    path('', index, name="index"),

    path('iniciosession/', iniciosession, name="iniciosession")
]
