```text
  _____  _                          _     _       _
 |  __ \(_)                        | |   (_)     ( )
 | |__) |_ _ __   ___   ___ ___ ___| |__  _  ___ |/ ___
 |  ___/| | '_ \ / _ \ / __/ __| __| '_ \| |/ _ \  / __|
 | |    | | | | | (_) | (_| (__| |_| | | | | (_) | \__ \
 |_|    |_|_| |_|\___/ \___\___|\__|_| |_|_|\___/  |___/
                                       PIZZA & SUBS
      // ""--.._
     ||  (_)  _ "-._
     ||    _ (_)    '-.
     ||   (_)   __..-'
      \\__..--""
```


# 🍕 Pinocchio's Pizza & Subs

![Status Completed](http://img.shields.io/static/v1?label=STATUS&message=COMPLETED&color=GREEN&style=for-the-badge)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

## 📖 Overview

**Pinocchio's Pizza** is a full-stack e-commerce platform built with Django. It was developed as part of **CS50’s Web Programming with Python and JavaScript**.

The system solves the challenge of digitizing a complex restaurant menu (handling multiple size variations and topping combinations) and managing the complete order flow, from ingredient selection to transactional email confirmations.

The project is deployed in the **cloud (Koyeb)** using a production-grade **PostgreSQL** database and **SMTP (Brevo)** for email services.

---

## ✨ Key Features

This project goes beyond a simple CRUD application. Here are the main features:

### 1. 🛍️ Advanced Content & Menu Management
* **Dynamic Opening Hours:** The store hours displayed on the Homepage are 100% managed via Django Admin. The administrator can update business hours without touching the code or redeploying.
* **Size & Price Variation:** Logic to handle items with multiple prices based on size (Small vs. Large) efficiently.
* **Topping Logic:** The system validates the exact number of allowed toppings.
    * *Example:* A "2-Topping Pizza" strictly requires the user to select exactly 2 ingredients before adding to the cart.

### 2. 🔐 Robust Authentication & Recovery
* **Full Account Flow:** Secure Registration and Login.
* **Password Recovery:** Real-world implementation of "Forgot Password". The system sends a unique, secure link via email (SMTP) allowing users to reset their credentials.
* **Email Validation:** Ensures only users with valid email addresses can operate on the platform.

### 3. 🛒 Smart Cart & Checkout Simulation
* **Data Persistence:** The shopping cart is saved in the database (`Cart Model`), allowing users to close the browser and resume their order later (unlike session-only carts).
* **Real-time Calculation:** Subtotal and Total update automatically as items are added.
* **Checkout Flow:** The system records the order in the database and clears the cart, simulating a real purchase flow.

### 4. 📧 Email Integration (SMTP)
* **Transactional Notifications:** Integrated with **Brevo (formerly Sendinblue)** API via SMTP.
* **Email Templates:** Automatic sending of order receipts to the client and password reset links.

### 5. ⚙️ Admin Panel (Back-office)
* **Total Management:** User-friendly interface to add new pizzas, toppings, change prices, or update store hours.
* **Order Workflow:** Administrators can view incoming orders in real-time.

---

## 🛠️ Tech Stack & Architecture

* **Backend:** Python 3.11 + Django 4.2
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5 (Responsive)
* **Database:** PostgreSQL 16 (Cloud Hosted)
* **Infrastructure:**
    * **Deploy:** Koyeb (PaaS)
    * **Web Server:** Gunicorn
    * **Static Files:** WhiteNoise
* **Email Service:** Brevo SMTP Relay

---

## 📸 Visual Demo

| Dynamic Menu | Topping Selection |
|:---:|:---:|
| ![Menu](static/img/menu_screenshot.png) | ![Toppings](static/img/toppings_screenshot.png) |

| Shopping Cart | Email Received |
|:---:|:---:|
| ![Cart](static/img/cart_screenshot.png) | ![Email](static/img/email_screenshot.png) |

---

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/project3.git](https://github.com/your-username/project3.git)
    cd project3
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables (.env):**
    Create a `.env` file or export these variables:
    ```env
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    EMAIL_HOST_USER=your_brevo_login
    EMAIL_HOST_PASSWORD=your_smtp_key
    DEFAULT_FROM_EMAIL=your_verified_email
    ```

4.  **Run Migrations and Start Server:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

Access: `http://127.0.0.1:8000`

---

## 📝 License

This project was developed for educational purposes (CS50 Web @ Harvard).






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
- added the orders function so we can view placed orders (needs some fixing)

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
Sending emails for reseting passwords and confirming purchases, using the Brevo API
Access to an admin page to add and remove menu items.

TODO: Improve this description!