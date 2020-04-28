
# Create your views here.

# accounts/views.py

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from . forms import CustomUserCreationForm

from django.shortcuts import render

from django.contrib.messages import error

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


# register
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            # Get user data for the email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Email the user
            html_template = get_template('email.html')
            d = { 'username': username }
            subject, from_email, to = "Welcome to Pinocchio's ", "Pinocchio's Pizza & Subs", email
            html_content = html_template.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # Add a success message to the next page
            messages.success(request, 'Your account has been created')

            return redirect("login")

    else:
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

################ login forms###################################################
