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
            print("submitted")
    context = {'form':form}
    return render(request,'RestaurantWeb.html',context)

def inform(request):
    if request.method == 'POST':
        content = request.POST.dict()
    context = {'info':content}
    return render(request,'ReservationInformation.html',context)

def confirm(request):
    return render(request,'ReservationConfirmation.html',{})