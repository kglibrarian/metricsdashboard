
#################################################
#Import Libraries
#################################################

from flask import Flask

#################################################
# Flask Setup
#################################################

app = Flask(__name__,
    static_folder = './public',
    template_folder="./static")

import templates.dashboard.views

#################################################
# Notes
#################################################
# This file initializes your application and brings together all of the various components.