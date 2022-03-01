from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#from entities.user import User_account
#from entities.recommendation import Recommendation

#db.create_all()
#db.session.commit()
