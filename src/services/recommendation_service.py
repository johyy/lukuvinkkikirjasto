from entities.recommendation import Recommendation
from repositories.recommendation_repository import recommendation_repository as default_recommendation_repository


class RecommendationService:
    """ Class responsible for recommendation logic."""

    def __init__(self, recommendation_repository=default_recommendation_repository):
        """ Class constructor. Creates a new recommendation service.
        Args:"""
        self._recommendation = None
        self._recommendation_repository = recommendation_repository

    def list_recommendations_by_user(self, user_id):
        return self._recommendation_repository.fetch_recommendation_by_user_id(user_id)

    def list_all_recommendations(self, sort_option="1"):
        """ Lists all recommendations."""

        return self._recommendation_repository.fetch_all_recommendations(sort_option=sort_option)

    def add_recommendation(self, title, link, user_id):
        """ Adds new recommendation."""

        if title == "" or link == "":
            return False, "Täytä kaikki tiedot"

        message = ""
        self._recommendation = Recommendation(title, link, user_id)

        if self._recommendation_repository.add_new_recommendation(self._recommendation):
            return True, message

        message = f"{title} löytyy jo kirjastosta"
        return False, message

    def delete_recommendation(self, id):
        self._recommendation_repository.delete_recommendation(id)
        """ Deletes recommendation."""

    def test_like(self, user_id, recommendation_id):
        return self._recommendation_repository.test_like(user_id, recommendation_id)

    def add_like(self, recommendation_id, likes):
        self._recommendation_repository.add_like(recommendation_id, likes)


recommendation_service = RecommendationService()
