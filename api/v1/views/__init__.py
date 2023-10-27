#!/usr/bin/python3
"""the handler of package views/v1"""
from flask import Blueprint


# init global variables
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
