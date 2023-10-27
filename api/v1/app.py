#!/usr/bin/python3
"""
version 1 of flask web application api
"""
import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views


# init global variables
app = Flask(__name__)
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', '5000'))
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
CORS(app, resources={'/*': {'origins': host}})


@app.teardown_appcontext
def teardown_flask(exception):
    """close the storage after when app finished"""
    storage.close()


@app.errorhandler
def error_404(error):
    """function that handles the 404 error"""
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))
    app.run(
        host=host,
        port=port,
        threaded=True
    )
