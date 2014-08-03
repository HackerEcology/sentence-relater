#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################
# SuggestU sentence relater #
#############################

import sys
import datetime

from app import app, verySimpleModelMikolov

from flask import Flask, \
    Response, \
    json, \
    make_response, \
    request, \
    redirect

from config import \
    HOST, \
    PORT, \
    DEBUG,\
    TEMPLATE_CONFIGURATION, \

@app.route('/')
def index():
    """
    Landing Page: contains links to login portals.
    """
    return Response("Hello! Welcome to SuggestU.")

@app.route('/<s1>/<s2>')
def relater(s1=None, s2=None):
    """
    API path
    """
    return Response(str(verySimpleModelMikolov(s1, s2)))


if __name__ == '__main__':
    try:
        app.run(host = HOST,
                port = PORT,
                debug = DEBUG)
    except:
        raise
