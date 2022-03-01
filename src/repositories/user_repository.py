from werkzeug.security import generate_password_hash
from db import db


class UserRepository:
    """Class that handles database queries for users"""

    def __init__(self):
        """Class constructor"""

    def add_a_new_user(self, user):
        """Adds a new user"""
        hash_value = generate_password_hash(user.get_password())

        db.session.add(user)
        db.session.commit()
        return True

    def get_user(self, username):
        """Gets user"""
        sql = "SELECT username, password, admin, id FROM user_account WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return False

        return user

user_repository = UserRepository()
