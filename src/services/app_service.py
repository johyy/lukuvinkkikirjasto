from werkzeug.security import check_password_hash
from repositories.user_repository import UserRepository
from entities.user import User_account

class AppService:
    """ Class responsible for app logic."""

    def __init__(self):
        """ Class constructor. Creates a new app service.
        Args:"""

        self.user_repository = UserRepository()
        self._current_user = None

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
            if check_password_hash(new_user[2], password):
                self.user = User_account(username=username, password=new_user[2])
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

    def register(self, username, password):

        if len(username) >= 3 and len(password) >= 8 and any(not c.isalpha() for c in password):
            user = User_account(username=username, password=password, admin=False)
            if self.user_repository.add_a_new_user(user):
                self.set_current_user(user)
                return user
        return None

app_service = AppService()
