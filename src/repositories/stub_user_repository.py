import secrets
from werkzeug.security import generate_password_hash
from db import db
class StubUserRepository:
    """Class that handles database queries for users"""

    def __init__(self):
        """Class constructor"""

    def add_a_new_user(self, username, password, admin):
        """Adds a new user."""
        #hash_value = generate_password_hash(user.get_password())
        try:
            sql = """INSERT INTO tests.users (username, password, is_admin)
            VALUES (:username,:password, :admin)"""
            db.session.execute(sql, {"username": username,
            "password": password, "admin": admin})
            db.session.commit()
            return True
        except Exception:
            return False

    def get_user(self, username):
        """Gets user."""
        try:
            sql = """ SELECT username, password, is_admin, id
            FROM tests.users WHERE username=:username"""
            result = db.session.execute(sql, {"username": username})
            user = result.fetchone()
            if not user:
                return False
            return user
        except Exception:
            return False
