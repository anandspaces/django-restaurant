from django.urls import path
from .views import home,web,inform,confirm

urlpatterns = [
    path('',home,name='home'),
    path('restaurantweb/',web),
    path('restaurantweb/information/',inform),
    path('restaurantweb/information/confirmation/',confirm),
]