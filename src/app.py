from os import getenv
from create_application import create_app
from initialise_database import initialise_database

# Build the database if it does not exist
initialise_database()

app = create_app()
app.secret_key = getenv("SECRET_KEY")

import routes
