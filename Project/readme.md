Djongo setup: https://www.mongodb.com/compatibility/mongodb-and-django

Django documentation: https://docs.djangoproject.com/en/5.0/intro/tutorial02/, https://docs.djangoproject.com/en/5.0/intro/tutorial01/

How to run
First setup mongo db with the database name "restaurant-db"

BEFORE RUNNING THESE COMMANDS you need to be in the directory: ~root/restaurantSite

Needed installs:

django

pymongo==3.12.3

pytz

djongo

Run the server: 

python manage.py runserver
Migrate the database:  python manage.py makemigrations, python manage.py migrate

Must create an admin user: 

python manage.py createsuperuser
This will allow you to create a local admin user

going to ~siteDirectory/admin to see admin portal
