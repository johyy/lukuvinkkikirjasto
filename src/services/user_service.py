from entities.user import User
from entities.recommendation import Recommendation


class UserService:
    """ Class responsible for user logic."""

    def __init__(self, user_repository, recommendation_repository, user=None):
        """ Class constructor. Creates a new user service.
        Args:"""

        self.user_repository = user_repository
        self.recommendation_repository = recommendation_repository
        self._current_user = user

    def get_current_user(self):
        """ Returns the current user.
        Returns:
            current user
        """

        return self._current_user

    def set_current_user(self, user):
        """ Sets a current user."""

        self._current_user = user

    def create_user(self, username, password):

        if len(username) >= 3 and len(password) >= 8:
            if any(not c.isalpha() for c in password):
                user = User(username, password)
                self.user_repository.add_a_new_user(self, user)
                return user
        return None

    def add_recommendation(self, title, link):
        """ Adds a recommendation to the current user."""
        if title != "" and link != "":
            recommendation = Recommendation(title, link)
            self._current_user.add_recommendation(recommendation)
            self.recommendation_repository.add_new_tip(self._current_user.get_id(), recommendation)

