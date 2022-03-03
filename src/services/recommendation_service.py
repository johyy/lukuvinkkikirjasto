from entities.user import UserAccount
from repositories.recommendation_repository import RecommendationRepository

class RecommendationService:
    """ Class responsible for media logic."""

    def __init__(self):
        """ Class constructor. Creates a new recommendation service.
        Args:"""
        self.user = UserAccount
        self.recommendations = RecommendationRepository

    def method1(self):
        """ Does something. """


    def method2(self):
        """ This too. """



resommendation_service = RecommendationService()
