from django.shortcuts import render
from .forms import MasukForms
from django.contrib.auth.decorators import login_required
# Create your views here.

def customerin(request):
    if request.method == "POST":
        form = MasukForms(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MasukForms()
    return render(request, "newcustomer.html", {"form":form})

def pelanggan_saatini(request):
    return render(request, "newcustomer")