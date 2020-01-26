from django.urls import path

from . import views

urlpatterns = [
    #path("login.html", views.login, name="login"),
    #path("register.html", views.register, name="register"),
    path("menu/", views.menu, name="menu"),
    path("", views.index, name="index"),
]
