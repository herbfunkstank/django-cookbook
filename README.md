### README.md for Cookbook - Django 1.4.2
# Based on cookbook app found here: 
[http://django-workshop.de](http://django-workshop.de)

I created this just to demonstrate what I can do:

### Created Middleware to handle 403 errors

Replaced index and detail functions with class-based-generic-views

Added frontend forms for adding and editing recipes to cookbook for users.

Updated render_to_response to render shortcut - DRY.

Created userauth to extend django.contrib.auth and provide user management.

Added staticfiles and HTML5 Boiler.

De-coupled URLconf and templates for best practice - DRY.

Database import with 3 German recipes: import.json

Database backup with banana pancakes and hummus recipes: backup.json

Setup local_settings.py to hold local development environment settings for best practice.

Add recipes to your cookbook through superuser login to admin interface
