from db import db
from app import db
from werkzeug.security import generate_password_hash
import secrets

class UserRepository:
    """Class that handles database queries for users"""

    def __init__(self):
        """Class constructor"""

    def add_a_new_user(self, user, admin):
    def add_a_new_user(self, user):
        hash_value = generate_password_hash(user.get_password())
        try:
            sql = "INSERT INTO users (username,password, is_admin) VALUES (:username,:password, :admin)"
            db.session.execute(sql, {"username": user.get_username(), "password": hash_value, "admin": admin})
            db.session.commit()
        except Exception as e:
            print(e)
            return False

        db.session.add(user)
        db.session.commit()
        return True

    def get_user(self, username):
        try:
            sql = "SELECT username, password, is_admin, id FROM users WHERE username=:username"
            result = db.session.execute(sql, {"username": username})
            user = result.fetchone()
            if not user:
                return False
            else:
                return user
        except Exception:
        sql = "SELECT username, password, admin, id FROM user_account WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return False

        return user