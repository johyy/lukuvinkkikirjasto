from os import getenv
from flask import Flask
from db import db


def create_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///nomanoma"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

import routes

app = create_app()
app.app_context().push()
with app.app_context():
    from entities.user import User_account
    from entities.recommendation import Recommendation
    db.create_all()
    db.session.commit()