import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle
from flask_sqlalchemy import SQLAlchemy

# load machine leearning model
model = pickle.load(open('tfidf.pkl','rb'))

# app
APP = Flask(__name__)

# routes
@APP.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}
