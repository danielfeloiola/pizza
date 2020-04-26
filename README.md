# Project 3

Web Programming with Python and JavaScript

Restaurant Website using Django
This site was developed as project 3 of CS50 Web.

Files:

orders/admin.py
- registered all the models from the menu on the admin

orders/apps.py
- class for setting up the orders app

orders/forms.py
- added classes for the forms for pizzas, subs and other menu items.

orders/models.py
- created a class for each menu item/topping
- created a class for the shopping cart
- created a class for each cart item in the shopping cart

orders/urls.py
- added url for the menu and index pages

orders/views.py:
- added the index funtion, to load the index page
- added the menu function, with GET (to to show the menu) and POST (to add items to cart)
- added the cart function w/ GET and POST (remove items from cart and place order)

orders/templates/registration
- added login and password reset templates

orders/templates/
- added the layout.html (template), index.html (homepage), and the menu.html (for the menu on orders/views)

users/views.py
- implemented the register system. Needs some cleaning. Double check the login part.

users/forms.py
- added classes inherithing/extending the class for user registration. Needs some cleaning

users/models.py
- Created a custom user class used in user/forms.py
- Added the number of cart items in the user model

users/urls.py
- added url for the registration

users/templates
- added register.html - the register page
- added email.html - the template for the welcome email

pizza/settings.py
- added a setup to send emails using an online service (SMTP)

pizza/urls.py
- added urls for admin, users and orders

Personal touch:
- Sending a email with a receipt for each order
- Also added email password reset feature


Features:
Sending emails for reseting passwords and confirming purchases.
Access to an admin page to add and remove menu items.
