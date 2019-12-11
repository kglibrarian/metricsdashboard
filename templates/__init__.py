#################################################
#Import Libraries
#################################################

from flask import Flask

# register the blueprints

#################################################
# Flask Setup
#################################################

app = Flask(__name__,
    static_folder = './public',
    template_folder='./static')

#import templates.dashboard.views
from templates.dashboard.views import dashboard_blueprint
app.register_blueprint(dashboard_blueprint)

#################################################
# Notes
#################################################
# This file initializes your application and brings together all of the various components.