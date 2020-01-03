from django.db import models

# Create your models here.



# versao antiga que nao funcionou

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)



    # add additional fields in here
    def __str__(self):
        return self.username
