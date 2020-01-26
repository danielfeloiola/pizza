from django.db import models

# Create your models here.

# ad topings to each model
class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.CharField(max_length=64)
    price_large = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"

class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.CharField(max_length=64)
    price_large = models.CharField(max_length=64)

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

class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"
