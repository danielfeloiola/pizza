from django import forms
from .models import RegularPizza, SicilianPizza, Sub, DinnerPlatter, Salad, Pasta, Topping

# Form for the menu

class OrderForm(forms.Form):
    'form for dinner platters, salads and pasta'
    dish = forms.CharField()
    type = forms.CharField()
    size = forms.CharField()
    price = forms.CharField()

class SubForm(forms.Form):
    "form for subs"
    sub_name = forms.CharField(required=False)
    sub_type = forms.CharField(required=False)
    sub_size = forms.CharField(required=False)
    sub_price = forms.CharField(required=False)
    extra_cheese = forms.BooleanField(required=False)
    extra_green_pepper = forms.BooleanField(required=False)
    extra_mushroom = forms.BooleanField(required=False)
    extra_onion = forms.BooleanField(required=False)


class PizzaForm(forms.Form):
    "form for pizzas"
    pizza_dish = forms.CharField()
    pizza_type = forms.CharField()
    pizza_size = forms.CharField()
    pizza_price = forms.CharField()
    num_of_topings = forms.CharField()

    toppings = Topping.objects.all().values()

    final_toppings = []

    for i in toppings:
        final_toppings.append((i['name'],i['name']))

    pizza_topping_1 = forms.ChoiceField(widget=forms.Select, choices=final_toppings, required=False)
    pizza_topping_2 = forms.ChoiceField(widget=forms.Select, choices=final_toppings, required=False)
    pizza_topping_3 = forms.ChoiceField(widget=forms.Select, choices=final_toppings, required=False)
    pizza_topping_4 = forms.ChoiceField(widget=forms.Select, choices=final_toppings, required=False)

    label = {
        'pizza_topping_1': None,
        'pizza_topping_2': None,
        'pizza_topping_3': None,
        'pizza_topping_4': None

    }
