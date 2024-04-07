#!/usr/bin/python3
"""
setting up blueprint modules
"""
from flask import Blueprint, abort

app_views = Blueprint("appviews", __name__)

from api.v1.views.index import *
from api.v1.views.users import *
#from api.v1.views.drugs import *
from api.v1.views.pharmacy import *
