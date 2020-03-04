from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from decouple import config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

DB = SQLAlchemy(app)

cannabis = DB.Table('cannabis_table', DB.metadata, autoload=True, autoload_with=DB.engine)

@app.route('/')
def index():
    results = DB.session.query(cannabis).all()
    cannabis.query.all()
    return ''

#class User(DB.Model):
    #"""Cannabis Names"""
    #id = DB.Column(DB.BigInteger, primary_key=True)
    #name = DB.Column(DB.String(15), nullable=False)

#class Cannabis(DB.Model):
    #"""Cannabis types we pull"""
    #id = DB.Column(DB.BigInteger, primary_key=True)
    #text = DB.Column(DB.Unicode(280))
