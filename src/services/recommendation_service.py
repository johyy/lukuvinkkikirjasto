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

        message = ""
        if title == "" or link == "":
            return False, "Täytä kaikki tiedot"

        fixed_link = self._fix_link(link)
        self._recommendation = Recommendation(title, fixed_link, user_id)

        if self._recommendation_repository.add_new_recommendation(self._recommendation):
            return True, message

        message = f"{title} löytyy jo kirjastosta."
        return False, message

    def _fix_link(self, link):
        http = "http://"
        https = "https://"
        if http in link:
            fixed_link = link.replace(http, "")
        if https in link:
            fixed_link = link.replace(https, "")
        return fixed_link

    def delete_recommendation(self, recommendation_id):
        """ Deletes recommendation."""
        self._recommendation_repository.delete_recommendation(
            recommendation_id)

    def delete_all_recommendations(self):
        self._recommendation_repository.delete_all_recommendations()

    def delete_all_likes(self):
        self._recommendation_repository.delete_all_likes()

    def test_like_to_add(self, user_id, recommendation_id):
        return self._recommendation_repository.test_like_to_add(user_id, recommendation_id)

    def test_like_to_remove(self, user_id, recommendation_id):
        return self._recommendation_repository.test_like_to_remove(user_id, recommendation_id)

    def add_like(self, recommendation_id, likes):
        self._recommendation_repository.add_like(recommendation_id, likes)

    def list_recommendations_liked_by_user(self, user_id):
        list_of_liked = []
        list_of_liked_recommendations = self._recommendation_repository.fetch_recommendations_liked_by_user(
            user_id)
        for liked in list_of_liked_recommendations:
            list_of_liked.append(liked[0])
        return list_of_liked


recommendation_service = RecommendationService()
