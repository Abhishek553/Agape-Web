from django.shortcuts import render, redirect
from attend.models import Attend
from attend.forms import AttendForm
from event.models import Event
from home.models import User

# Create your views here.

def index(request):
    event = Event.objects.all()
    # user = User.object.all()
    return render(request, "attend/index.html", {'event':event})

def attend(request):

    if request.method == 'POST':
        form = AttendForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('')
    else:   
        form = AttendForm()

    return render(request,"register/register.html", {'form':form})