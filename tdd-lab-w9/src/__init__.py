# src/__init__.py

from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)

api = Api(app)

class Ping(Resource):
 def get(self):
  return {
   'status': 'success',
   'message': 'pong!'
  }
 
api.add_resource(Ping, '/ping')


# src/__init__.py

import os # new

import sys
print(app.config, file=sys.stderr)

from flask import Flask, jsonify
from flask_restx import Resource, Api

# instantiate the app
app = Flask(__name__)
api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS') # new
app.config.from_object(app_settings) # new

# set config
app.config.from_object('src.config.DevelopmentConfig') # new
class Ping(Resource):
 def get(self):
  return {
  'status': 'success',
  'message': 'pong!'
 }

api.add_resource(Ping, '/ping')


