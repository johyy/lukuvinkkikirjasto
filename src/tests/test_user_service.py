import unittest
from unittest.mock import Mock, ANY
from services.user_service import UserService
from entities.user import User

class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repo_mock = Mock()
        self.user = User("nimi", "salasana")
        self.us = UserService(user_repo_mock, self.user)

    def test_create_user(self):
        user = self.us.create_user("nimi", "salasana123")
        self.assertEqual(user.get_username(), "nimi")
        self.assertEqual(user.get_password(), "salasana123")

    def test_create_user_with_too_short_username(self):
        user = self.us.create_user("ni", "salasana123")
        self.assertEqual(user, None)

    def test_create_user_with_too_short_password(self):
        user = self.us.create_user("nimi", "s123")
        self.assertEqual(user, None)

    def test_create_user_with_password_missing_special_case(self):
        user = self.us.create_user("nimi", "salasana")
        self.assertEqual(user, None)

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
