from flask import session
from werkzeug.security import check_password_hash
from repositories.user_repository import UserRepository
from entities.user import User
from services.user_service import UserService


class AppService:
    """ Class responsible for app logic."""

    def __init__(self):
        """ Class constructor. Creates a new app service.
        Args:"""

        self.user_repository = UserRepository
        self._current_user = None
        self.user_service = UserService

    def login(self, username, password):
        """ Log in user.
        Args:
            username: [String] Username of the user.
            password: [String] Password of the user.
        Returns:
            [User] User entity that is logged in.
        Raises:
            InvalidCredentialsError:
                Invalid username and/or password.
        """

        new_user = self.user_repository.get_user(username)
        if new_user is not False:
            if check_password_hash(new_user[1], password):
                self._current_user = User(new_user[0], new_user[1])
                session["csrf_token"] = self.user_service.check_csrf()
                return True, ""
        return False, "Käyttäjänimi tai salasana virheellinen"

    def logout(self):
        """ Sets the current user as None.
        """

        self._current_user = None

    def get_current_user(self):
        """ Returns the current user.
        Returns:
            current user
        """

        return self._current_user

    def set_current_user(self, user):
        """ Sets a current user."""

        self._current_user = user

    def register(self, username, password, password_confirmation):
        "Registers a new user"
        message = ""
        if len(username) >= 3 and len(password) >= 8:
            if not password == password_confirmation:
                message = "Salasanat eivät täsmää"
            if any(not c.isalpha() for c in password):
                user = User(username, password)
                if self.user_repository.add_a_new_user(user, False):
                    self.set_current_user(user)
                    return user, message
                message = "Tunnus on jo olemassa."
            message = """Tunnuksessa oltava yli 3 merkkiä ja salasanassa
            yli 8 merkkiä ja vähintään yksi numero"""
        return None, message


app_service = AppService()
