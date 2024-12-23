from django.urls import path
from .views import home,web,inform,confirm,login,signup,booking,about,team,service,testimonial,contact,menu

urlpatterns = [
    path('',home,name='home'),
    path('web/',web,name='web'),
    path('inform/',inform,name='inform'),
    path('confirm/',confirm,name='confirm'),
    path('login/',login,name='login'),
    path('signup/',signup,name='signup'),
    path('booking/',booking,name='booking'),
    path('about/',about,name='about'),
    path('menu/',menu,name='menu'),
    path('team/',team,name='team'),
    path('testimonial/',testimonial,name='testimonial'),
    path('service/',service,name='service'),
    path('contact/',contact,name='contact'),
]