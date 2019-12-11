#################################################
#Import Libraries
#################################################

from flask import *
from flask_cors import CORS
from templates import app
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#Load this config object for development mode
app.config.from_object('configurations.DevelopmentConfig')
app.run()

@app.route('/')

def hello_world():
    return 'Hello to the World of Flask!'


    
if __name__ == "__main__":
    app.debug = True
    app.run()

################################################
#Notes
################################################

# This is the file that is invoked to start up a development server. 
# It gets a copy of the app from your package and runs it. 
# This won’t be used in production, but it will see a lot of 
# mileage in development.
#https://itnext.io/a-template-for-creating-a-full-stack-web-application-with-flask-npm-webpack-and-reactjs-be2294b111bd


