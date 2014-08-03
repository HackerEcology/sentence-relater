# Import flask and template operators
from flask import Flask
import sys
import os

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

from sentence_relate_mikolov import verySimpleModelMikolov
