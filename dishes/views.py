from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def home(request):
    temp = 'index.html'
    return render(request,temp,{})

def web(request):
    temp = 'RestaurantWeb.html'
    return render(request,temp,{})

def inform(request):
    temp = 'ReservationInformation.html'
    return render(request,temp,{})

def confirm(request):
    temp = 'ReservationConfirmation.html'
    return render(request,temp,{})