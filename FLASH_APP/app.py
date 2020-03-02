"""Minimal flask app"""

from flask import Flask

#make our app factory

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        return 'Welcome to Cannabis!'
    return app
