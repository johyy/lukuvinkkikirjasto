from repositories import user_repository

class User:
    """ Class that represents a single user. """

    def __init__(self, username, password):
        """ Class constructor. Creates a new user.
        Attributes:
            _username: [String] Unique identifier of the user.
            _password: [String] Password of the user profile.
        """
        self.user_repository = user_repository
        self._username = username
        self._password = password

    ## Get
    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    ## Set
    def set_username(self, username):
        """ Sets username.
        Args:
            username: [String] The username to be set.
        """

        self._username = username

    def set_password(self, password):
        """ Sets user's password.
        Args:
            password: [String] The password to be set.
        """

        self._password = password
    
#    def get_user_db(self, username):
#        return self.user_repository.get_user(username)
