from django.shortcuts import render, redirect
from .forms import AddJourney
from .models import jrny
from django.http import HttpResponseRedirect
# Create your views here.


def aridess(request):
    rides = jrny.objects.all()
    context = {
        'rides': rides
    }
    return render(request, 'arides.html', context)

def journey(request):
    if request.method == 'POST':
        form = AddJourney(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aridess')
    else:
        form = AddJourney()
    context = {
        'form': form,
    }
    return render(request, 'ride.html', context)
