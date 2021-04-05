from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Sum
from .forms import OrderForm, PizzaForm, SubForm
from .models import Salad,DinnerPlatter,Pasta,Sub,RegularPizza,SicilianPizza,Topping, Cart, CartItem, Order, Hour
from users.models import CustomUser
from django.core.exceptions import PermissionDenied
from django.template.loader import get_template
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import os


# Create your views here.


def index(request):
    """Render the home page"""

    # get the hours
    hours = Hour.objects.all()

    # context
    context = {
        "hours": hours,
    }

    #return HttpResponse("Project 3: TODO")
    return render(request, "index.html", context)
    #return render(request, "index.html")


def menu(request):
    """Show the menu cart and allows the user to add items to cart"""


    if request.method == 'POST':

        # get the users
        user = CustomUser.objects.filter(id = request.user.id).get()

        # check for a cart and make one if there is none
        try:
            cart = Cart.objects.filter(user = request.user).get()
        except:
            cart = Cart(user=request.user)
            cart.save()

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
                                sub_extras_count = 0,
                                extra_1 = None,
                                extra_2 = None,
                                extra_3 = None,
                                extra_4 = None)
            item.save()

            user.cart_total += price

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
                                sub_extras_count = 0,
                                extra_1 = None,
                                extra_2 = None,
                                extra_3 = None,
                                extra_4 = None)
            item.save()

            user.cart_total += price

        elif sub_form.is_valid():

            # get data from form
            sub_name = sub_form.cleaned_data['sub_name']
            sub_type = sub_form.cleaned_data['sub_type']
            sub_size = sub_form.cleaned_data['sub_size']
            sub_price = sub_form.cleaned_data['sub_price']
            # transform in int to avoid floting point issues
            sub_price = int(round(float(sub_price)*100))
            extra_cheese = sub_form.cleaned_data['extra_cheese']
            extra_green_pepper = sub_form.cleaned_data['extra_green_pepper']
            extra_mushroom = sub_form.cleaned_data['extra_mushroom']
            extra_onion = sub_form.cleaned_data['extra_onion']

            extras_count = 0
            extras = []

            # add extras...
            if extra_cheese == True:
                sub_price += 50
                extras_count += 1
                extras.append("cheese")
            if extra_green_pepper == True:
                sub_price += 50
                extras_count += 1
                extras.append("green peppers")
            if extra_mushroom == True:
                sub_price += 50
                extras_count += 1
                extras.append("mushrooms")
            if extra_onion == True:
                sub_price += 50
                extras_count += 1
                extras.append("onions")

            # and back to floating point value for aesthetics
            sub_price = float(sub_price/100)

            if extras_count == 0:
                # Make a cart item
                item = CartItem(dish = sub_name, type = sub_type, size = sub_size, price = sub_price, num_of_topings = 0,
                                    topping1 = None, topping2 = None, topping3 = None, topping4 = None,
                                    sub_extras_count = extras_count,
                                    extra_1 = None,
                                    extra_2 = None,
                                    extra_3 = None,
                                    extra_4 = None)
                item.save()

                user.cart_total += sub_price

            if extras_count == 1:
                # Make a cart item
                item = CartItem(dish = sub_name, type = sub_type, size = sub_size, price = sub_price, num_of_topings = 0,
                                    topping1 = None, topping2 = None, topping3 = None, topping4 = None,
                                    sub_extras_count = extras_count,
                                    extra_1 = extras[0],
                                    extra_2 = None,
                                    extra_3 = None,
                                    extra_4 = None)
                item.save()

                user.cart_total += sub_price

            if extras_count == 2:
                # Make a cart item
                item = CartItem(dish = sub_name, type = sub_type, size = sub_size, price = sub_price, num_of_topings = 0,
                                    topping1 = None, topping2 = None, topping3 = None, topping4 = None,
                                    sub_extras_count = extras_count,
                                    extra_1 = extras[0],
                                    extra_2 = extras[1],
                                    extra_3 = None,
                                    extra_4 = None)
                item.save()

                user.cart_total += sub_price


            if extras_count == 3:
                # Make a cart item
                item = CartItem(dish = sub_name, type = sub_type, size = sub_size, price = sub_price, num_of_topings = 0,
                                    topping1 = None, topping2 = None, topping3 = None, topping4 = None,
                                    sub_extras_count = extras_count,
                                    extra_1 = extras[0],
                                    extra_2 = extras[1],
                                    extra_3 = extras[2],
                                    extra_4 = None)
                item.save()

                user.cart_total += sub_price

            if extras_count == 4:
                # Make a cart item
                item = CartItem(dish = sub_name, type = sub_type, size = sub_size, price = sub_price, num_of_topings = 0,
                                    topping1 = None, topping2 = None, topping3 = None, topping4 = None,
                                    sub_extras_count = extras_count,
                                    extra_1 = extras[0],
                                    extra_2 = extras[1],
                                    extra_3 = extras[2],
                                    extra_4 = extras[3])
                item.save()

                user.cart_total += sub_price



        # add the selected item to the cart
        cart.item.add(item)

        # get the number of items in the cart, and the user id
        # save number of cart items on the user object
        # also update on the request so the number on top of th3 page is updated
        num = cart.item.all().count()

        # variables needed to show the num of cart items at the top
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
            "messages": "Item added to cart" # add message
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

    # show the cart
    if request.method == 'GET':

        # get user object
        user = CustomUser.objects.filter(id = request.user.id).get()

        # check for a cart and make one if there is none
        try:
            cart = Cart.objects.filter(user = request.user).get()
        except:
            cart = Cart(user=request.user)
            cart.save()

        # make context
        context = {
            "total": user.cart_total,
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
            user.cart_total = 0.00
            request.user.cart_items = None

            # save data
            cart.save()
            user.save()

            context = {
                "total": user.cart_total,
                "CartItems": cart.item.all(),
            }


            # and now render page
            return render(request,"cart.html", context)

        # placing the order
        elif request.POST['order'] == "Place Order":

            # create the order object
            order = Order(user=request.user)
            order.save()

            # get the user and cart
            user = CustomUser.objects.filter(id = request.user.id).get()
            cart = Cart.objects.filter(user = request.user).get()

            # Get user data for the email
            username = user.username
            email = user.email

            # set up the confirmation email
            html_template = get_template('email-receipt.html')
            d = {
                'username': username,
                "CartItems": cart.item.all(),
            }
            subject, from_email, to = "Your Pinocchio's order", "Pinocchio's Pizza <" + os.getenv("DEFAULT_FROM_EMAIL") + ">", email
            html_content = html_template.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")

            # add all cart items to the order and remove from cart
            for element in cart.item.all():
                order.item.add(element)
                cart.item.remove(element)

            # get the order total from the user object
            order.order_total = user.cart_total

            # clear the cart
            #cart.item.all().delete()
            user.cart_items = 0
            user.cart_total = 0.00
            request.user.cart_items = None

            # send the EMAIL
            msg.send()

            # save data
            cart.save()
            user.save()
            order.save()

            # render the confirmation page
            return render(request,"confirm.html")

        #if deleting a single item from the cart
        else:

            # get item to delete from post request
            item_to_delete = int(request.POST['order'])

            # get cart and user
            cart = Cart.objects.filter(user = request.user).get()
            user = CustomUser.objects.filter(id = request.user.id).get()

            # calculate the amount of items
            delete = cart.item.filter()[item_to_delete - 1]
            user.cart_items -= 1
            request.user.cart_items = user.cart_items

            # update cart total
            newtotal = user.cart_total - delete.price
            user.cart_total = newtotal

            # actually delete item from cart
            delete.delete()

            # save data
            user.save()
            cart.save()

            print(newtotal)

            # make context
            context = {
                "total": newtotal,
                "CartItems": cart.item.all(),
            }

            # and now render page
            return render(request,"cart.html", context)



def orders(request):
    """Show the placed orders"""

    # CHECK IF USER IS SUPERUSER
    user = CustomUser.objects.filter(id = request.user.id).get()
    if not user.is_superuser:
        raise PermissionDenied

    # get the orders
    orders = Order.objects.all()

    # DO AN ERROR CHECK HERE IN CASE THERE IS NO ORDERS!

    # get items for each order
    for order in orders:
        items = order.item.all()

    # make context to the webpage
    context = {
        "CartItems": items,
        "orders": orders
    }

    # and now render page
    return render(request,"orders.html", context)
