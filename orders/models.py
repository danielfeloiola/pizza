from django.db import models

# Create your models here.

# é necessario criar um model p os users?????
# Users model
#class Users(models.Model):
#    origin = models.Charfield(max_lenght=64)
#    destination = models.Charfield(max_lenght=64)
#    duration = models.Integerfield()


# Get rid of this and make a pizza orders model
class regularPizza(models.Model):
    toppings = models.CharField(max_length=64)
    size = models.CharField(max_length=64)

class sicilianPizza(models.Model):
    num_toppings = models.CharField(max_length=64)
    size = models.CharField(max_length=64)

    price_small = models.CharField(max_length=64)
    price_large = models.CharField(max_length=64)

#    destination = models.Charfield(max_lenght=64)
#    duration = models.Integerfield()
