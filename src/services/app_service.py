from repositories.user_repository import UserRepository
from entities.user import User
from werkzeug.security import check_password_hash

class AppService:
    """ Class responsible for app logic."""

    def __init__(self):
        """ Class constructor. Creates a new app service.
        Args:"""

        self._user_repository = UserRepository
        self._user = None

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
        new_user = self._user_repository.get_user(username)
        if new_user is not False:
            if check_password_hash(new_user[1], password):
                self._user = User(new_user[0], new_user[1])
                return True, ""
            return False, "Käyttäjänimi tai salasana virheellinen"
        return False, "Käyttäjänimi tai salasana virheellinen"

    def logout(self):
        """ Sets the current user as None.
        """

        self._user = None

app_service = AppService()
