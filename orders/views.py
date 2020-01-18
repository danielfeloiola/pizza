from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Sum

# Create your views here.
def index(request):
    #return HttpResponse("Project 3: TODO")
    return render(request, "index.html")

def login(request):

    return render(request,"login.html")

def register(request):

    return render(request,"register.html")

def menu(request):
    from .models import Salad,DinnerPlatter,Pasta,Sub,RegularPizza,SicilianPizza

    context = {
        "RegularPizza": RegularPizza.objects.all(),
        "SicilianPizza": SicilianPizza.objects.all(),
        "salads": Salad.objects.all(),
        "platters": DinnerPlatter.objects.all(),
        "pastas": Pasta.objects.all(),
        'subs': Sub.objects.all()
    }

    return render(request,"menu.html", context)
