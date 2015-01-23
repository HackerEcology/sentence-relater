#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################
# SuggestU sentence relater #
#############################

import sys
import datetime

from app import app, \
    verySimpleModelMikolov

from flask import Flask, \
    Response, \
    json, \
    make_response, \
    request, \
    redirect

@app.route('/')
def index():
    """
    Landing Page: contains links to login portals.
    """
    tmp = "Hello! Welcome to SuggestU. Try this URL:\n" + \
          "http://0.0.0.0:5000/cat loves milk/cat is an animal/"
    return Response(tmp)

@app.route('/<s1>/<s2>/')
def relater(s1=None, s2=None):
    """
    API path
    """
    return Response(str(verySimpleModelMikolov(s1, s2)))


if __name__ == '__main__':
    try:
        app.run(host = app.config['HOST'],
                port = app.config['PORT'],
                debug = app.config['DEBUG'])
    except:
        raise
