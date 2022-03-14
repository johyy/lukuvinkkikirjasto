# pylint: disable=no-member

class UserAccount():
    """ Class that represents a single user. """

    def __init__(self, username, password):
        """ Class constructor. Creates a new user.
        Attributes:
            _username: [String] Unique identifier of the user.
            _password: [String] Password of the user profile.
        """

        self._username = username
        self._password = password
        self._recommendations = []
        self._admin = False

    def get_username(self):
        """ Gets the name of the user."""

        return self._username

    def get_password(self):
        """ Gets the password of the user."""

        return self._password

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

    def set_admin(self, boolean):
        """ Sets user's admin status.
        Args:
            admin: [boolean] The admin status to be set.
        """

        self._admin = boolean

    def add_recommendation(self, recommendation):
        """ Adds a recommendation to the user."""

        self._recommendations.append(recommendation)

    def remove_recommendation(self, recommendation):
        """ Removes a recommendation to the user."""

        if recommendation in self._recommendations:
            self._recommendations.remove(recommendation)

    def get_recommendations(self):
        """ Returns user's recommendations."""

        return self._recommendations

    def is_admin(self):
        return self._admin
