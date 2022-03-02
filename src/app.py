from entities.recommendation import Recommendation
from entities.user import User_account
from db import db
from create_application import create_app

app = create_app()


import routes

app.app_context().push()
with app.app_context():
    from entities.user import User_account
    from entities.recommendation import Recommendation
    db.create_all()
    db.session.commit()