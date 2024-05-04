from django.urls import path
from .views import home,web,inform,confirm,login,signup

urlpatterns = [
    path('',home,name='home'),
    path('web/',web,name='web'),
    path('inform/',inform,name='inform'),
    path('confirm/',confirm,name='confirm'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
]