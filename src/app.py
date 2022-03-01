from os import getenv
from flask import Flask
from db import db

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
import routes
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


