from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.CharField(max_length=64)
    price_large = models.CharField(max_length=64)

    toppings = models.ManyToManyField(Topping, blank=True, name="toppings")

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.CharField(max_length=64)
    price_large = models.CharField(max_length=64)

    toppings = models.ManyToManyField(Topping, blank=True, name="toppings")

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.CharField(max_length=64, blank=True)
    price_large = models.CharField(max_length=64)
    extra_cheese = models.BooleanField(max_length=64)

    if name == 'Steak + Cheese':
        mushrooms = models.BooleanField(max_length=64)
        peppers = models.BooleanField(max_length=64)
        onions = models.BooleanField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.CharField(max_length=64)
    price_large = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.price}"

class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.price}"

class CartItem(models.Model):

    dish = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.IntegerField()

    num_of_topings = models.IntegerField(blank=True, null=True)
    topping1 = models.CharField(max_length=64, blank=True, null=True)
    topping2 = models.CharField(max_length=64, blank=True, null=True)
    topping3 = models.CharField(max_length=64, blank=True, null=True)
    topping4 = models.CharField(max_length=64, blank=True, null=True)

    extra_cheese = models.NullBooleanField(blank=True)
    extra_green_pepper = models.NullBooleanField(blank=True)
    extra_mushroom = models.NullBooleanField(blank=True)
    extra_onion = models.NullBooleanField(blank=True)

    #orders.CartItem.extra_onion: (fields.E110) BooleanFields do not accept null values.
	#HINT: Use a NullBooleanField instead.

    def __str__(self):
        return f"{self.dish}, {self.type}, {self.size}, {self.price}"


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    item = models.ManyToManyField(CartItem, blank=True, name="item")
    #item = models.ForeignKey(CartItem, on_delete=models.CASCADE, name="item", blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
