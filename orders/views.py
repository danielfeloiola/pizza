#from django.http import HttpResponse
#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum

from .forms import OrderForm, PizzaForm, SubForm

from .models import Salad,DinnerPlatter,Pasta,Sub,RegularPizza,SicilianPizza,Topping


# Create your views here.


def index(request):
    #return HttpResponse("Project 3: TODO")
    return render(request, "index.html")

def menu(request):

    if request.method == 'POST':

        # make the form
        order_form = OrderForm(request.POST)
        pizza_form = PizzaForm(request.POST)
        sub_form = SubForm(request.POST)

        # check whether it's valid:
        if order_form.is_valid():

            # get data from form
            dish = order_form.cleaned_data['dish']
            type = order_form.cleaned_data['type']
            size = order_form.cleaned_data['size']
            price = order_form.cleaned_data['price']

            # print for testing
            print("order form", dish, type, size, price)

        elif pizza_form.is_valid():

            # get data from form
            dish = pizza_form.cleaned_data['pizza_dish']
            type = pizza_form.cleaned_data['pizza_type']
            size = pizza_form.cleaned_data['pizza_size']
            price = pizza_form.cleaned_data['pizza_price']
            num_of_topings = pizza_form.cleaned_data['num_of_topings']
            topping1 = pizza_form.cleaned_data['pizza_topping_1']
            topping2 = pizza_form.cleaned_data['pizza_topping_2']
            topping3 = pizza_form.cleaned_data['pizza_topping_3']
            topping4 = pizza_form.cleaned_data['pizza_topping_4']

            # print for testing
            print("pizza form",dish,type,size,price,num_of_topings,topping1,topping2,topping3,topping4)

        elif sub_form.is_valid():
            print(sub_form)

            # get data from form
            sub_name = sub_form.cleaned_data['sub_name']
            sub_type = sub_form.cleaned_data['sub_type']
            sub_size = sub_form.cleaned_data['sub_size']
            sub_price = sub_form.cleaned_data['sub_price']

            # print for testing
            print("sub form", sub_name, sub_type, sub_size, sub_price)

        # make context and render template
        context = {
            "RegularPizza": RegularPizza.objects.all(),
            "SicilianPizza": SicilianPizza.objects.all(),
            "salads": Salad.objects.all(),
            "platters": DinnerPlatter.objects.all(),
            "pastas": Pasta.objects.all(),
            "subs": Sub.objects.all(),
            "toppings": Topping.objects.all(),
            "order_form": order_form,
            "pizza_form": pizza_form,
            "sub_form": sub_form,
            "messages": 'Item added to cart' # add message
        }
        return render(request, "menu.html", context)

    elif request.method == 'GET':

        order_form = OrderForm()
        pizza_form = PizzaForm()
        sub_form = SubForm()

        context = {
            "RegularPizza": RegularPizza.objects.all(),
            "SicilianPizza": SicilianPizza.objects.all(),
            "salads": Salad.objects.all(),
            "platters": DinnerPlatter.objects.all(),
            "pastas": Pasta.objects.all(),
            "subs": Sub.objects.all(),
            "toppings": Topping.objects.all(),
            "order_form": order_form,
            "pizza_form": pizza_form,
            "sub_form": sub_form
        }

        return render(request,"menu.html", context)
