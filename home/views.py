from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.forms import UserForm
from home.models import User
from event.models import Event
# from authentication import Authentication


# # Create your views here.
# @Authentication.valid_user

def index(request):
    event = Event.objects.all()
    
    return render(request,"home/home_page.html", {'event':event})

def loginPage(request):

    if request.method == 'POST':

        request.session['email'] = request.POST['email']
        request.session['password'] = request.POST['password']
        return redirect('main')

    else:
            messages.info(request, "Incorrect Username or Password")

    return render(request,"login/login.html")

def register(request):

    print(request.POST)
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()

        return redirect('login')
    else:   
        form = UserForm()

    return render(request,"register/register.html", {'form':form})
 
def starting(request):
    return render(request, "home/starting.html")

  