from flask import session
from repositories.user_repository import UserRepository as user_repository
from repositories.tip_repository import TipRepository as tip_repository
from entities.user import User_account
from services.user_service import UserService

class AppService:
    """ Class responsible for app logic."""

    def __init__(self):
        """ Class constructor. Creates a new app service.
        Args:"""

        self.user_service = UserService(user_repository, tip_repository)
        self._current_user = None

    def login(self, username, password):
        """ Log in user."""

        new_user = user_repository.get_user(user_repository, username)
        if new_user is not False:
            if new_user[1] == password:
                self._current_user = User_account(
                    username=username, password=new_user[1])
                #session["csrf_token"] = self.user_service.check_csrf()
                session["user_id"] = 1 # mita tahan tulee?
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

    def set_current_user(self, user):
        """ Sets a current user."""

        self._current_user = user

    def register(self, username, password, password_confirmation):
        """ Registers a new user."""

        if len(username) >= 3 and len(password) >= 8 and any(not c.isalpha() for c in password):
            if not password == password_confirmation:
                message = "Salasanat eivät täsmää"
                return None, message
            user = User_account(username=username, password=password)
            if user_repository.add_a_new_user(user_repository, user):
                return True, ""
            message = "Tunnus on jo olemassa."
        else:
            message = "Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki."
        return False, message


app_service = AppService()
