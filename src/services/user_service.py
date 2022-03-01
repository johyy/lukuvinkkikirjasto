import os
from entities.recommendation import Recommendation

class UserService:
    """ Class responsible for user logic."""

    def __init__(self, user_repository, recommendation_repository, user=None):
        """ Class constructor. Creates a new user service.
        Args:"""

        self.user_repository = user_repository
        self.recommendation_repository = recommendation_repository
        self._current_user = user
        self.user_token = None

    def add_recommendation(self, title, link):
        """ Adds a recommendation to the current user."""
        if title != "" and link != "":
            recommendation = Recommendation(title=title, link=link)
            self._current_user.add_recommendation(recommendation)
            self.recommendation_repository.add_new_tip(self._current_user.get_id(), recommendation)

    def create_csrf_token(self):
        """ Creates new CSRF token. """
        self.user_token = os.urandom(16).hex()
        return self.user_token

    def check_csrf(self, token):
        """ Checks CSRF token. """
        if self.user_token != token:
            return False
        return True
    