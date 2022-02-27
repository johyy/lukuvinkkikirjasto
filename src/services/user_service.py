from entities.user import User
from werkzeug.security import check_password_hash
from repositories.user_repository import UserRepository

class UserService:
    """ Class responsible for user logic."""

    def __init__(self):
        self.user_repository = UserRepository
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
        user = self.user_repository.get_user(username)
        if user != False:
            if check_password_hash(user[1], password):
                self._current_user = User(user[0], user[1])
                return True, ""
            else:
                return False, "Käyttäjänimi tai salasana virheellinen"
        return False, "Käyttäjänimi tai salasana virheellinen"

user_service = UserService()
