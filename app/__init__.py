# Import flask and template operators
from flask import Flask
import sys
import os

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from sentence_relate_mikolov import verySimpleModelMikolov