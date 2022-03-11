import os
from flask import session, request
from werkzeug.security import check_password_hash, generate_password_hash
from repositories.user_repository import user_repository as default_user_repository
from entities.user import UserAccount


class UserService:
    """ Class responsible for user logic."""

    def __init__(self, user_repository=default_user_repository):
        """ Class constructor. Creates a new user service.
        Args:"""

        self._user_repository = user_repository
        self._current_user = None

    def login(self, username, password):
        """ Log in user."""
        if username == "" or password == "":
            return False, "Käyttäjänimi tai salasana virheellinen"
        new_user = self._user_repository.get_user(username)
        if new_user is not False:

            if check_password_hash(new_user[1], password):

                self.set_current_user(UserAccount(
                    username=username, password=new_user[1]))
                session["csrf_token"] = os.urandom(16).hex()
                session["user_id"] = new_user[3]
                session["user_name"] = username
                return True, ""
        return False, "Käyttäjänimi tai salasana virheellinen"

    def logout(self):
        """ Sets the current user as None.
        """

        self._current_user = None
        del session["user_id"]
        del session["user_name"]

    def get_current_user(self):
        """ Returns the current user.
        Returns:
            current user
        """

        return self._current_user

    def get_current_user_id(self):
        """ Returns the current user's row id from db.
        Returns:
            current user's row id
        """
        
        user = self._user_repository.get_user(self._current_user.get_username())
        user_id = user[3]
        return user_id

    def set_current_user(self, user):
        """ Sets a current user."""

        self._current_user = user

    def register(self, username, password, password_confirmation):
        """ Registers a new user."""

        if len(username) >= 3 and len(password) >= 8 and any(not c.isalpha() for c in password):
            if not password == password_confirmation:
                message = "Salasanat eivät täsmää"
                return None, message

            password = generate_password_hash(password)
            user = UserAccount(username=username, password=password)
            if self._user_repository.add_a_new_user(user):
                return True, ""
            message = "Tunnus on jo olemassa."
        else:
            message = "Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki."
        return False, message

    def check_csrf(self):
        """ Checks CSRF token. """
        if session["csrf_token"] != request.form["csrf_token"]:
            return False
        return True

    def delete_all(self):
        self._user_repository.delete_all()


user_service = UserService()
