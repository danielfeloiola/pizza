from django.contrib import admin

from .models import DinnerPlatter, Salad, Pasta, Sub, RegularPizza, SicilianPizza

# Register your models here.

admin.site.register(DinnerPlatter)
admin.site.register(Salad)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
