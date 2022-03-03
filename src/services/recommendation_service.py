
from entities.user import UserAccount
from repositories.recommendation_repository import RecommendationRepository

class RecommendationService:
    """ Class responsible for media logic."""

    def __init__(self):
        """ Class constructor. Creates a new recommendation service.
        Args:"""
        self.user = UserAccount
        self.recommendations = RecommendationRepository

    def add_recommendation(self, recommendation):
        """ Does something. """


    def method2(self):
        """ This too. """



recommendation_service = RecommendationService()
