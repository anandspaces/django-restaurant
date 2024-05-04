from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import CustomerForm
from .models import Customer
# Create your views here.

def home(request):
    return render(request,'index.html',{})

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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('username')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)
        if user is None:
            messages.error(request,'Invalid username/password')
            return redirect('/login/')
        else: 
            login()
            return redirect('/home/')

    return render(request,'login.html',{})

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'username already taken!')
            return redirect(request, '/signup/')

        user = User.objects.create(
            name = name,
            username = username,
            email = email,
            # password = password
        )
        user.set_password(password) # salting
        user.save()
        messages.info(request, 'Account created successfully!')
        return redirect('/signup/')

    return render(request,'signup.html',{})