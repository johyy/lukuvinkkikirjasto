from app import app
from db import db

def pytest_configure():
    db.init_app(app)