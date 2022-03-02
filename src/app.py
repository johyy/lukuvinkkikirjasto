from entities.recommendation import Recommendation
from entities.user import User_account
from db import db
from create_application import create_app
from initialise_database import initialise_database


# Build the database if it does not exist
initialise_database()
    
app = create_app()


import routes

    
