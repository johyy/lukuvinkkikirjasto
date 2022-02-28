from db import db
from werkzeug.security import generate_password_hash
import secrets


class StubUserRepository:
    """Class that handles database queries for users"""

    def __init__(self):

        """Class constructor"""

    def add_a_new_user(self, username, password, admin):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO tests.users (username, password) VALUES (:username, :password, :admin)"
            sdb.session.execute(sql, {"username": username, "password": hash_value, "admin": admin})
            db.session.commit()
        except Exception:
            return False

    def get_user(self, username):
        try:
            sql = "SELECT username, password, is_admin, id FROM tests.users WHERE username=:username"
            result = db.session.execute(sql, {"username": username})
            user = result.fetchone()
            if not user:
                return False
            else:
                return user
        except Exception:
            return False
