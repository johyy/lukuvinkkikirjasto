from db import db


class UserRepository:
    """Class that handles database queries for users"""

    def __init__(self):
        """Class constructor"""

    def add_a_new_user(self, user):
        """Adds a new user"""
        try:
            sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
            db.session.execute(sql, {"username": user.get_username(), "password": user.get_password(), "admin": user.is_admin()})
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_user(self, username):
        """Gets user"""
        sql = "SELECT username, password, admin FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return False

        return user

user_repository = UserRepository()
