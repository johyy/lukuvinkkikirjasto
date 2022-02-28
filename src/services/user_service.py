from entities import user
from werkzeug.security import check_password_hash
from repositories import user_repository

class UserService:
    """ Class responsible for user logic."""

    def __init__(self):
        self.user_repository = user_repository
        self.user = user
        """ Class constructor. Creates a new user service.
        Args:"""

    def get_current_user(self):
        """ Returns the current user.
        Returns:
            
        """

        return self._current_user

    def set_current_user(self, user):
        self._current_user = user

    def create_user(self, username, password):
        """ Creates a new user.
        Args:
            username: [String] The name of the user.
        """
    def login(self, username, password):
        new_user = self.user.get_user_db(username)
        if new_user != False:
            if check_password_hash(new_user[1], password):
                self._current_user = self.user(new_user[0], new_user[1])
                return True, ""
            else:
                return False, "Käyttäjänimi tai salasana virheellinen"
        return False, "Käyttäjänimi tai salasana virheellinen"

user_service = UserService()
