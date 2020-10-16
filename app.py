from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Price, Brand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mymusic.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)