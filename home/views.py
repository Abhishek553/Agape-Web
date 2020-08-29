from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,"home/home_page.html")

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request,"login/login.html")

def register(request):
    
    form = UserCreationForm()

    if request.method == 'PSOT':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request,"register/register.html", context)

def starting(request):
    return render(request, "home/starting.html")
    

