from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home/home_page.html")

def login(request):
    return render(request,"login/login.html")

def register(request):
    return render(request,"register/register.html")
