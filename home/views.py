from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"home/home_page.html")

def loginPage(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
    
        if user is not None:
            login(request, email)
            return redirect('main')
        else:
            messages.info(request, "Incorrect Username or Password")

    return render(request,"login/login.html")

def register(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    context = {'form': form}
    return render(request,"register/register.html", context)

def starting(request):
    return render(request, "home/starting.html")
    

