from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from .forms import OrderForm, PizzaForm, SubForm
from .models import Salad,DinnerPlatter,Pasta,Sub,RegularPizza,SicilianPizza,Topping, Cart, CartItem
from users.models import CustomUser


# Create your views here.


def index(request):
    #return HttpResponse("Project 3: TODO")
    return render(request, "index.html")

def menu(request):

    ###########################################
    #               POST REQUEST              #
    ###########################################
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
            # for some reason size and price got mixed up
            price = order_form.cleaned_data['size']
            price = float(price)*100
            size = order_form.cleaned_data['price']

            # Make a cart item
            item = CartItem(dish=dish, type=type, size=size, price=price, num_of_topings=0,
                                topping1=None, topping2=None,topping3=None,topping4=None,
                                extra_cheese = None,
                                extra_green_pepper=None,
                                extra_mushroom = None,
                                extra_onion=None)
            item.save()

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

            # Make a cart item
            item = CartItem(dish=dish, type=type, size=size, price=price, num_of_topings=num_of_topings,
                                topping1=topping1, topping2=topping2,topping3=topping3,topping4=topping4,
                                extra_cheese = None,
                                extra_green_pepper=None,
                                extra_mushroom = None,
                                extra_onion=None)
            item.save()

        elif sub_form.is_valid():

            # get data from form
            sub_name = sub_form.cleaned_data['sub_name']
            sub_type = sub_form.cleaned_data['sub_type']
            sub_size = sub_form.cleaned_data['sub_size']
            sub_price = sub_form.cleaned_data['sub_price']
            extra_cheese = sub_form.cleaned_data['extra_cheese']
            extra_green_pepper = sub_form.cleaned_data['extra_green_pepper']
            extra_mushroom = sub_form.cleaned_data['extra_mushroom']
            extra_onion = sub_form.cleaned_data['extra_onion']

            # Make a cart item
            item = CartItem(dish = sub_name, type = sub_type, size = sub_size, price = sub_price, num_of_topings = 0,
                                topping1 = None, topping2 = None, topping3 = None, topping4 = None,
                                extra_cheese = extra_cheese,
                                extra_green_pepper = extra_green_pepper,
                                extra_mushroom = extra_mushroom,
                                extra_onion = extra_onion)
            item.save()




        ##########################################
        # FIX INT ISSUE ON THE PIZZA ITEMS!!!!!!!#
        ##########################################

        # Check for a shopping cart. If there is none, then make one
        try:
            cart = Cart.objects.filter(user = request.user).get()
        except:
            cart = Cart(user=request.user)
            cart.save()

        # add the selected item to the cart
        cart.item.add(item)

        # get the number of items in the cart, and the user id
        # save number of cart items on the user object
        # also update on the request so the number on top of tha page is updated
        num = cart.item.all().count()
        user = CustomUser.objects.filter(id = request.user.id).get()
        user.cart_items = num
        request.user.cart_items = num

        # and save
        user.save()



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




    ###########################################
    #               GET REQUEST               #
    ###########################################
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
