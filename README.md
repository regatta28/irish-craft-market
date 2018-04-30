# A Django powered Ecommerce project - Irish Craft Market


[Link to Demo of site]("https://irish-craft-market-2.herokuapp.com")

### Technology Used

Note: All installations should be included in a requirements.txt file.

The project uses [django 1.11]("https://www.djangoproject.com/"), a python web framework.  [Download and install python 2.7]("https://www.python.org/downloads/") as it is required for this project. It is important to work on a virtual environment right from the start. Install django under the virtual environment. 

You start a project with the following code ```django-admin startproject nameofProject .```. This will create a subdirectory inside your directory and includes settings.py, the main urls.py and wsgi.py (used as an interface for webservers) and also creates a manage.py file. You can run the server and view your django app using the following command ```python manage.py runserver```. Next we create our apps. All apps must be included under INSTALLED_APPS in settings.py. You create an app with the following command ```python manage.py startapp nameofApp```.

#### Apps will consist of 

* views.py file - which contains views, classes and functions which take a  request and return a response.
* urls.py file - views are mapped to urls file which are included in the main urls.py file.
* models.py file - Essential fields and behaviours for data stored.
* tests.py file - for testing your code.
* apps.py file - for application configuration.
* admin.py file - an interface for reading metadata from your models.
* migrations folder - holds information on data  and data storage.


### You can also include

* forms.py file - recommended for storing code for any forms on the page.
* context.py - for viewing data across many pages of your website.
* templates folder - holds html files that contain the static parts of the HTML output as well as syntax describing how content will be inserted.

All template subdirectories must be included in the template search path in settings.py.

## Deployment

The website is deployed to Heroku and uses a Heroku Postgres add on for the database. dj_database_url must be installed and imported into settings. All secret keys for AWS/Stripe/Django have be included in config vars. [Tutorial here]("https://devcenter.heroku.com/articles/heroku-postgresql") for more information. You will also need to store all your secret keys in an env.py file and import to settings so that you don't have to store them in settings. Make sure to ADD ENV.PY TO .GITIGNORE. And don't include ```import env ```when committing to github. The site uses [TravisCI]("https://travis-ci.org/") for testing and deploying our code. [Tutorial here for TravisCI]("https://docs.travis-ci.com/user/for-beginners/"). Gunicorn must also be installed and procfile created.

## Features

* accounts app - For authenticating users, registration and users profile code.
* cart app - for adding products to your cart, viewing and adjusting the cart items.
* home app - for the index and about pages.
* products app - for user to add new products, for user or non-user to browse products, for editing products.
* search app - for finding products in the website.

* A templates folder which holds a base.html file with our base code like navbar, logo, body and footer. All other templates extend this base.html ```{% extends base.html %}``` and include their own code inbetween ```{% blockcontent %}``` and ```{% endblock %}``` tags. You must also add ```{% load static from staticfiles %}
{% load bootstrap_tags %} ``` to the beginning of all template htmls extending base.html.

#### Checkout App and Stripe

A [stripe]("https://stripe.com/ie") account must be created and stripe installed. The checkout app should have payment forms and order forms for payments. [Stripe Tutorial here]("https://stripe.com/docs/checkout") for further information. 

### Acknowledgments

This project was written on cloud9, an online integrated development environment developed by [Amazon Online Web Services]("https://aws.amazon.com/"). The project also used [Amazon Online Web Services]("https://aws.amazon.com/") for its cloud database storage. A S3 cloud bucket is created giving the public permission to access and modify their posts and products. An IAM is set up to control users authentication and permissions. Setting the bucket policy defines which groups and users are given access and the type of access. 
Bootstrap was used for styling.

[![Build Status](https://travis-ci.org/regatta28/irish-craft-market.svg?branch=master)](https://travis-ci.org/regatta28/irish-craft-market)