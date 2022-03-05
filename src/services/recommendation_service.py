
from entities.recommendation import Recommendation
from repositories.recommendation_repository import recommendation_repository as default_recommendation_repository


class RecommendationService:
    """ Class responsible for recommendation logic."""

    def __init__(self, recommendation_repository=default_recommendation_repository):
        """ Class constructor. Creates a new recommendation service.
        Args:"""
        self._recommendation = None
        self._recommendation_repository = recommendation_repository

    def list_all_recommendations(self, sort_option="1"):
        """ Lists all recommendations."""

        return self._recommendation_repository.fetch_all_recommendations(sort_option)

    def add_recommendation(self, title, link):
        """ Adds new recommendation."""

        if title == "" or link == "":
            return False, f"Täytä kaikki tiedot"
        else:
            message = ""
            self._recommendation = Recommendation(title, link)
            if self._recommendation_repository.add_new_recommendation(self._recommendation):
                return True, message
            else:
                message = f"{title} löytyy jo kirjastosta"
                return False, message

    def delete_recommendation(self, recommendation):
        """ Deletes recommendation."""
        pass

    def list_likes_of_recommendation(self, recommendation):

        return self._recommendation_repository.fetch_likes_of_recommendation(recommendation)


recommendation_service = RecommendationService()
