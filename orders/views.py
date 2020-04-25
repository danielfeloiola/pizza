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
    """Render the home page"""

    #return HttpResponse("Project 3: TODO")
    return render(request, "index.html")

def menu(request):
    """Show the menu cart and allows the user to add items to cart"""

    # TODO:
    ############################################################
    # FORCE 2 DECIMAL ON FLOAT VALUES
    # DO THE MATH USING INTEGERS
    ############################################################

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
            price = float(price)
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
            price = float(price)
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
            sub_price = float(sub_price)
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
        user.cart_items += 1
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


def cart(request):
    """Show the shopping cart and allows the user to place an order"""
    #return HttpResponse("this is the cart")

    # show the cart
    if request.method == 'GET':

        # filter carts by users
        cart = Cart.objects.filter(user = request.user).get()

        # add cart items to context
        context = {
            "CartItems": cart.item.all(),
        }

        # and render page
        return render(request,"cart.html", context)

    # if removing items or palcing oreders
    elif request.method == "POST":

        # check if placing an order or clearing cart or deleting item
        if request.POST['order'] == "Clear Cart":

            # get cart and user
            cart = Cart.objects.filter(user = request.user).get()
            user = CustomUser.objects.filter(id = request.user.id).get()

            # delete all the stuff and adjust num of itmes
            cart.item.all().delete()
            user.cart_items = 0
            request.user.cart_items = None

            # save data
            cart.save()
            user.save()

            # make context
            context = {
                "CartItems": cart.item.all(),
            }

            # and now render page
            return render(request,"cart.html", context)

        # placing the order
        elif request.POST['order'] == "Place Order":
            pass

            return render(request,"confirm.html")

        #if deleting a single item from the cart
        else:

            # get item to delete from post request
            item_to_delete = int(request.POST['order'])

            # get cart and user
            cart = Cart.objects.filter(user = request.user).get()
            user = CustomUser.objects.filter(id = request.user.id).get()

            # calculate the amount of items
            cart.item.filter()[item_to_delete - 1].delete()
            user.cart_items -= 1
            request.user.cart_items = user.cart_items

            # save data
            cart.save()
            user.save()

            # make context
            context = {
                "CartItems": cart.item.all(),
            }

            # and now render page
            return render(request,"cart.html", context)
