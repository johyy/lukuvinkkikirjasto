import unittest
from unittest.mock import Mock, ANY
from services.user_service import UserService
from entities.user import UserAccount

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repo_mock = Mock()
        recommendation_repo_mock = Mock()
        self.user = UserAccount(username="nimi1", password="salasana456")
        self.us = UserService(user_repo_mock, recommendation_repo_mock, self.user)

    def test_user_adds_recommendation(self):
        self.us.add_recommendation("Otsake", "linkki")
        self.assertEqual(self.user.get_recommendations()[0].get_title(), "Otsake")
        self.assertEqual(self.user.get_recommendations()[0].get_link(), "linkki")

    def test_user_adds_recommendation_without_title(self):
        self.us.add_recommendation("", "linkki")
        self.assertEqual(self.user.get_recommendations(), [])

    def test_user_adds_recommendation_without_link(self):
        self.us.add_recommendation("Otsake", "")
        self.assertEqual(self.user.get_recommendations(), [])

    def test_user_removes_recommendation(self):
        pass

    def test_user_removes_nonexisting_recommendation(self):
        pass
