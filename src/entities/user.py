# pylint: disable=no-member
import uuid
from app import db

class User_account(db.Model):
    """ Class that represents a single user. """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, default=False, nullable=False)

    '''
    def __init__(self, username, password):
        """ Class constructor. Creates a new user.
        Attributes:
            _username: [String] Unique identifier of the user.
            _password: [String] Password of the user profile.
        """

        self._id = uuid.uuid1()
        self._username = username
        self._password = password
        self.recommendations = []
    '''

    def get_id(self):
        """ Gets the id of the user."""

        return self.id

    def get_username(self):
        """ Gets the name of the user."""

        return self.username

    def get_password(self):
        """ Gets the password of the user."""

        return self.password

    def set_username(self, username):
        """ Sets username.
        Args:
            username: [String] The username to be set.
        """

        self.username = username

    def set_password(self, password):
        """ Sets user's password.
        Args:
            password: [String] The password to be set.
        """

        self.password = password

    def set_admin(self, boolean):
        """ Sets user's admin status.
        Args:
            admin: [boolean] The admin status to be set.
        """

        self.admin = boolean

    def add_recommendation(self, recommendation):
        """ Adds a recommendation to the user."""

        self.recommendations.append(recommendation)

    def remove_recommendation(self, recommendation):
        """ Removes a recommendation to the user."""

        if recommendation in self.recommendations:
            self.recommendations.remove(recommendation)

    def get_recommendations(self):
        """ Returns user's recommendations."""

        return self.recommendations

    def is_admin(self):
        if self.admin == None:
            return False
        return self.admin
