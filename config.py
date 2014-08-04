#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################
# Web Application settings
##########################

# The host IP to run the application from
#HOST = "127.0.0.1"
HOST = "0.0.0.0"

# The port to run the application from
PORT = 5000

# Statement for enabling the development environment
DEBUG = False #True

# # Define the application directory
# import os
# BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
CSRF_SESSION_KEY = "#%^@^%^*THD3GHSVEJIOB%udjehaxiry02%%"

# Secret key for signing cookies
SECRET_KEY = "#$FSDFSETE^^AUEFV#$%$&"

###################
# Template settings
###################

# # Dictionary that holds all the template configuration
# TEMPLATE_CONFIGURATION = {

#     # The title of the application as shown by the browser
#     "title" : "SuggestU sentence relater API",
#     # # Define the category and subcategory font-weifht CSS attribute [normal|bold]
#     # "category_font_weight" : "normal",
#     # "subcategory_font_weight" : "normal",
# }
