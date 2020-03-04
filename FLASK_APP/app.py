from flask import Flask, request, jsonify
import pandas as pd
from FLASK_APP import utils
import pickle

pickle_dict = pickle.load(open("dict.p", "rb"))


def create_app():
    app = Flask(__name__)
    @app.route('/strain/<strain>', methods=['GET'])
    def myfunc(strain):
      #strain = request.values['strain']
      return jsonify({"race":pickle_dict[strain]})


    return app

if __name__ == "__main__":
    app = create_app()
