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

    # dish info
    dish = models.CharField(max_length=64)
    type = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.FloatField()

    # pizza toppings
    num_of_topings = models.IntegerField(blank=True, null=True)
    topping1 = models.CharField(max_length=64, blank=True, null=True)
    topping2 = models.CharField(max_length=64, blank=True, null=True)
    topping3 = models.CharField(max_length=64, blank=True, null=True)
    topping4 = models.CharField(max_length=64, blank=True, null=True)

    sub_extras_count = models.IntegerField(blank=True, null=True)
    # subs extrs
    extra_1 = models.CharField(max_length=64, blank=True, null=True)
    extra_2 = models.CharField(max_length=64, blank=True, null=True)
    extra_3 = models.CharField(max_length=64, blank=True, null=True)
    extra_4 = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.dish}, {self.type}, {self.size}, {self.price}"


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ManyToManyField(CartItem, blank=True, name="item")

    def __str__(self):
        return f"{self.user} - {self.item}"

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item = models.ManyToManyField(CartItem, blank=True, name="item")
    order_total = models.FloatField(blank=True, null=True)

    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user}"

class Hour(models.Model):
    sun = models.CharField(max_length=64, blank=True, null=True)
    mon = models.CharField(max_length=64, blank=True, null=True)
    tue = models.CharField(max_length=64, blank=True, null=True)
    wed = models.CharField(max_length=64, blank=True, null=True)
    thu = models.CharField(max_length=64, blank=True, null=True)
    fri = models.CharField(max_length=64, blank=True, null=True)
    sat = models.CharField(max_length=64, blank=True, null=True)
    msg = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.sun}, {self.mon}, {self.tue}, {self.wed}"
