from os import getenv
from flask import Flask
from db import db
from config import DATABASE_FILE_PATH

def create_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////' + DATABASE_FILE_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app
