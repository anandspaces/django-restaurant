from django.shortcuts import render,redirect
from .forms import CustomerForm
from datetime import datetime
from .models import Customer
# Create your views here.

def home(request):
    return render(request,'index.html',{})

def menu(request):
    return render(request,'menu.html',{})

def service(request):
    return render(request,'service.html',{})

def team(request):
    return render(request,'team.html',{})

def testimonial(request):
    return render(request,'testimonial.html',{})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def booking(request):
    return render(request,'booking.html',{})

def web(request):
    def generate_reference_no():
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        return f"REF{timestamp}"
    
    form = CustomerForm
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid:
            global reference_no_var
            reference_no_var = generate_reference_no()
            form.instance.reference_no = reference_no_var
            form.save()
            print("form submitted!")
            return redirect('inform')
    context = {'form':form}
    return render(request,'RestaurantWeb.html',context)

def inform(request):
    # if request.method == 'POST':
    #     content = request.POST.dict()
    content = Customer.objects.get(reference_no=reference_no_var)
    context = {'info':content}
    return render(request,'ReservationInformation.html',context)

def confirm(request):
    return render(request,'ReservationConfirmation.html',{'RID':reference_no_var})

def login(request):
    return render(request,'login.html',{})

def signup(request):
    return render(request,'signup.html',{})
