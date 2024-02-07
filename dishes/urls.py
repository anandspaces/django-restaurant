from django.urls import path
from .views import home,web,inform,confirm

urlpatterns = [
    path('',home,name='home'),
    path('restaurantweb/',web,name='web'),
    path('inform/',inform,name='inform'),
    path('confirm/',confirm,name='confirm'),
]