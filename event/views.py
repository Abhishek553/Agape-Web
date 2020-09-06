from django.shortcuts import redirect, render
from event.forms import EventForm
from event.models import Event

# Create your views here.
# def event(request):
#     return render(request, "event/create.html")


def event(request):
    print(request.POST)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        form.save()
        return redirect("/home")
    else:
        form = EventForm()

    return render(request, "event/create.html")

def delete(request,id):
    event = Event.objects.get(id=id)
    event.delete()
    return redirect("/attend")
