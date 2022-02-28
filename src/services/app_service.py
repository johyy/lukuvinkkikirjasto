class AppService:
    """ Class responsible for app logic."""

    def __init__(user_repository):
        """ Class constructor. Creates a new app service.
        Args:"""
        
        self.user_repository = user_repository

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

        user_list = self._user_repository.find_by_username(username)
        if not user_list or user_list[0][1] != password:
            return False

        user = self.create_user_entity_from_db(user_list[0])
        self._user = user

        return user

    def logout(self):
        """ Sets the current user as None.
        """

        self._user = None

app_service = AppService()
