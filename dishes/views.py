from django.shortcuts import render
from .forms import CustomerForm
# Create your views here.
def home(request):
    return render(request,'index.html',{})

def web(request):
    form = CustomerForm
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid:
            form.save()
    context = {'form':form}
    return render(request,'RestaurantWeb.html',context)

def inform(request):
    return render(request,'ReservationInformation.html',{})

def confirm(request):
    return render(request,'ReservationConfirmation.html',{})