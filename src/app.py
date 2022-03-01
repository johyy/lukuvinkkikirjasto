from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///nomanoma"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

import routes
from entities.user import User_account
from entities.recommendation import Recommendation

db.create_all()
db.session.commit()