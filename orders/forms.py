from django import forms
from .models import RegularPizza, SicilianPizza, Sub, DinnerPlatter, Salad, Pasta, Topping


class OrderForm(forms.Form):
    dish = forms.CharField()
    type = forms.CharField()
    size = forms.CharField()
    price = forms.CharField()


class SubForm(forms.Form):
    sub_name = forms.CharField(required=False)
    sub_type = forms.CharField(required=False)
    sub_size = forms.CharField(required=False)
    sub_price = forms.CharField(required=False)
    extra_cheese = forms.BooleanField(required=False)
    extra_green_pepper = forms.BooleanField(required=False)
    extra_mushroom = forms.BooleanField(required=False)
    extra_onion = forms.BooleanField(required=False)


class PizzaForm(forms.Form):
    pizza_dish = forms.CharField()
    pizza_type = forms.CharField()
    pizza_size = forms.CharField()
    pizza_price = forms.CharField()
    num_of_topings = forms.CharField()

    pizza_topping_1 = forms.ChoiceField(required=False)
    pizza_topping_2 = forms.ChoiceField(required=False)
    pizza_topping_3 = forms.ChoiceField(required=False)
    pizza_topping_4 = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        toppings = Topping.objects.values_list("name", "name")

        self.fields["pizza_topping_1"].choices = toppings
        self.fields["pizza_topping_2"].choices = toppings
        self.fields["pizza_topping_3"].choices = toppings
        self.fields["pizza_topping_4"].choices = toppings