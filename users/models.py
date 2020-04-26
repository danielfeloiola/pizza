from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    cart_items = models.IntegerField(default=0)
    cart_total = models.FloatField(default=0)

    # add additional fields in here
    def __str__(self):
        return self.username
