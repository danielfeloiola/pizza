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

    return render(request,"menu.html")
