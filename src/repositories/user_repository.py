from db import db


class UserRepository:
    """Class that handles database queries for users"""

    def __init__(self):
        """Class constructor"""

    def add_a_new_user(self, user):
        """Adds a new user"""
        try:
            sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
            db.session.execute(sql, {"username": user.get_username(
            ), "password": user.get_password(), "admin": user.is_admin()})
            db.session.commit()
            return True
        except Exception as exception:
            print(exception)
            return False

    def get_user(self, username):
        """Returns user"""
        sql = "SELECT username, password, admin, rowid FROM users WHERE username=:username"
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()
        if not user:
            return False

        return user

    def get_user_by_id(self, user_id):
        """Returns user"""
        sql = "SELECT username, password, admin, rowid FROM users WHERE rowid=:rowid"
        result = db.session.execute(sql, {"rowid": user_id})
        user = result.fetchone()
        if not user:
            return False

        return user

    def delete_all(self):
        sql = """DELETE FROM users"""
        db.session.execute(sql)
        db.session.commit()


user_repository = UserRepository()
