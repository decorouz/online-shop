# Online Shop

This repository contains the complete source-code for the 7th chapter (Building an Online Shop) from the book Django 3 By Example:

[Django 3 By Example - Third Edition By Antonio Melé](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)

## Instructions to install

1. Install python3.7 and pip3
2. Install redis

3. Create a python virtual environment using venv python -m venv ~/python-virtual-environments/kartpool

4. Activate virtual environment source ~/python-virtual-environments/kartpool/bin/activate

5. Install Django and other dependencies pip install -r requirements.text

## Instructions to run

1. Start rabbitmq-server: To handle asyschronous actions.
2. Initialize the Redis server using the following command
   from the shell in your Redis directory:
   src/redis-server
3. Start Django web server (Make sure the virtual environment is activated) python manage.py runserver

## TODO:

-   Modify the administration order detail template and the order PDF invoice to display the applied coupon in the same way you did for the cart.
-   Rating or Review System
-   Search Functionality
-   Update the styling
-   Implement User App
-   pagination for list products
-   Remove coupon after checkout
