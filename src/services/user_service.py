class UserService:
    """ Class responsible for user logic."""

    def __init__():
        """ Class constructor. Creates a new user service.
        Args:"""

    # GET
    def get_current_user(self):
        """ Returns the current user.
        Returns:
            
        """

        return self._current_user

    #SET
    def set_current_user(self, user):
        self._current_user = user

    # LOGIN AND LOGOUT
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
"""
        user_list = self._user_repository.find_by_username(username)
        if not user_list or user_list[0][1] != password:
            return False

        user = self.create_user_entity_from_db(user_list[0])
        self._user = user
"""
        return user

    def logout(self):
        """ Sets the current user as None.
        """

        self._user = None

    # CREATE NEW ENTITIES
    def create_user(self, username, password):
        """ Creates a new user.
        Args:
            username: [String] The name of the user.
        """

        user = User(username)

 
user_service = UserService()
