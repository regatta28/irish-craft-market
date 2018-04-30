# A Django powered Ecommerce project - Irish Craft Market

[![Build Status](https://travis-ci.org/regatta28/irish-craft-market.svg?branch=master)](https://travis-ci.org/regatta28/irish-craft-market)

[Link to demo of site](https://irish-craft-market-2.herokuapp.com)
### Overview

The Irish Craft Market is designed in mind for people who have visited Ireland and would like to make purchases from the many wonderful country and city artists we have here. When you are travelling through a country it can be all too quick and people do not like spending money hastily. This site will provide the oportunity for previous visitors to purchase products they might have admired while here. The site is also geared towards the artists and craft artisans who would like to post their products. I hope to further develop the site. The UX is simple and straightforward. I personally like simple sites when I am purchasing products and submitting payment details as it makes me feel more secure. I have used bootstrap for creating a media responsive website. 

### Technology Used

All installations are included in a requirements.txt file.

The project uses [django 1.11](https://www.djangoproject.com/), a python web framework, [python 2.7](https://www.python.org/downloads/) has been used in this project. The project works on a virtual environment right from the start, installing django under the virtual environment. 

The project is started with the following code ```django-admin startproject nameofProject .```. This creates a subdirectory inside main directory and includes settings.py, the main urls.py and wsgi.py (used as an interface for webservers) and also creates a manage.py file. I ran the server with the following command ```python manage.py runserver```. Then I created the projects apps. All apps are included under INSTALLED_APPS in settings.py. I created the app with the following command ```python manage.py startapp nameofApp```.

#### Apps consist of 

* views.py file - which contains views, classes and functions which take a request and return a response.
* urls.py file - views are mapped to urls file which are included in the main urls.py file.
* models.py file - Essential fields and behaviours for data stored.
* tests.py file - for testing code.
* apps.py file - for application configuration.
* admin.py file - an interface for reading metadata from models.
* migrations folder - holds information on data and data storage.


### Also included

* forms.py file - recommended for storing code for any forms on the page.
* context.py - for viewing data across many pages of the website.
* templates folder - holds html files that contain the static parts of the HTML output as well as syntax describing how content will be inserted.

All template subdirectories are included in the template search path in settings.py.

## Deployment

The website is deployed to Heroku and uses a Heroku Postgres add on for the database. dj_database_url is installed and imported into settings. All secret keys for AWS/Stripe/Django are included in config vars. [Tutorial here](https://devcenter.heroku.com/articles/heroku-postgresql) for more information. Secret keys are also stored in an env.py file and import to settings so they are not stored settings. Made sure to ADD ENV.PY TO .GITIGNORE and I didnt include ```import env ```when committing to github. Gunicorn is installed and Procfile created.

## Testing

* The site uses [TravisCI](https://travis-ci.org/) for testing and deploying code. [Tutorial here for TravisCI](https://docs.travis-ci.com/user/for-beginners/).
* Testing for home page, about page completed, all links are sound. 
* Browsing products page and adding to cart is available for visitors to site.
* Registration and login tested, stores the information to profile page, logout tested - redirects to index. 
* Post ad page tested takes products and stores them to advertiser profile.
* Cart stores items and you can adjust quantity before purchasing at checkout
* Stripe test payment successfully
* Static and media files successfully loading from aws cloud.
* Travis Test passing.
* Heroku deploying.

## Features

* accounts app - For authenticating users, registration and users profile code.
* cart app - for adding products to cart, viewing and adjusting the cart items.
* home app - for the index and about pages.
* products app - for user to add new products, for user or non-user to browse products, for editing products.
* search app - for finding products in the website.

* A templates folder which holds a base.html file with base code like navbar, logo, body and footer. All other templates extend this base.html ```{% extends base.html %}``` and include their own code inbetween ```{% blockcontent %}``` and ```{% endblock %}``` tags. You must also add ```{% load static from staticfiles %}
{% load bootstrap_tags %} ``` to the beginning of all template htmls extending base.html.

#### Checkout App and Stripe

A [stripe](https://stripe.com/ie) account was created and stripe installed. The checkout app has payment and order forms for payments. [Stripe Tutorial here](https://stripe.com/docs/checkout) for further information. 

### Acknowledgments

This project was written on cloud9, an online integrated development environment developed by [Amazon Online Web Services](https://aws.amazon.com/). This project also used [Amazon Online Web Services](https://aws.amazon.com/) for cloud database storage. An S3 cloud bucket was created and I gave the public permission to access and modify their posts and products. An IAM was set up to control users authentication and permissions. Setting the bucket policy defined which groups and users are given access and the type of access. 
Bootstrap was used for styling and forms.

