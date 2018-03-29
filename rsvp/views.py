from django.shortcuts import render
from .forms import Rsvp
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        rsvp = Rsvp(request.POST)
        if rsvp.is_valid():
            rsvp.save()
        else:
            print(rsvp.errors)
    return render(request, 'rsvp/rsvp.html')
