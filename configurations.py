# This file contains most of the configuration variables that your app needs.
#Default values, to be used for all environments or overridden by individual environments. 
# An example might be setting DEBUG = False in config/default.py and DEBUG = True in config/development.py.

######################
#Base config class
######################

class BaseConfig(object):
    DEBUG = True # Turns on debugging features in Flask. 
    
    TESTING = False

######################
#Production specific config
######################    
class ProductionConfig(BaseConfig):
    DEBUG = False
    #Make sure DEBUG is set to False in production. Leaving it on will allow users to run arbitrary Python code on your server.

######################
#Development environment specific configuration
######################

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    TEMPLATES_AUTO_RELOAD = True