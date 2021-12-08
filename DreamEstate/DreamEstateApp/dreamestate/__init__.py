from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY']='thenightisyoung'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/dream.db'
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://username:password@hostname:port/databasename'


db=SQLAlchemy(app)
from dreamestate import routes