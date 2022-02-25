class UserService:
    """ Class responsible for user logic."""

    def __init__(self):
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

	
        user = User(username)

 
user_service = UserService()
