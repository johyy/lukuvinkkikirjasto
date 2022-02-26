from db import db
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

class UserRepository:
    """Class that handles database queries for users"""

    def __init__(self):
        """Class constructor"""

    def add_a_new_user(self, username, password, admin):
        hash_value = generate_password_hash(password)
        try:
            sql = "INSERT INTO users (username,password, is_admin) VALUES (:username,:password, :admin)"
            db.session.execute(sql, {"username": username, "password": hash_value, "admin": admin})
            db.session.commit()
        except Exception:
            return False

    def get_user(self, username):
        try:
            sql = "SELECT * FROM users WHERE username=:username"
            result = db.session.execute(sql, {"username": username})
            user = result.fetchone()
            if not user:
                return False
            else:
                return user
        except Exception:
            return False
    
    def login(self, username, password):
        sql = "SELECT password, id, is_admin FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username":username})
        user = result.fetchone()
        if not user:
            return False
        if not check_password_hash(user[0], password):
            return False
        db.session["user_id"] = user[1]
        db.session["user_name"] = username
        db.session["is_admin"] = user[2]
        return True