import unittest
from unittest.mock import Mock, ANY
from user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.us = UserService()
        self.user_mock = Mock()
        
        # palautetaan aina arvo 42
        self.user_mock.username.return_value = "nimi"
        self.user_mock.password.return_value = "salasana123"

    def test_create_user(self):
		user = self.us.create_user("nimi", "salasana123")
        self.assertEqual(user.get_name(), "nimi")
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
		recommendation = self.us.add_recommendation("Otsake", "linkki")
        self.assertEqual(recommendation.get_title(), "Otsake")
        self.assertEqual(recommendation.get_link(), "linkki")

    def test_user_adds_recommendation_without_title(self):
		recommendation = self.us.add_recommendation("", "linkki")
        self.assertEqual(recommendation, None)

    def test_user_adds_recommendation_without_link(self):
		recommendation = self.us.add_recommendation("Otsake", "")
        self.assertEqual(recommendation, None)

    def test_user_removes_recommendation(self):
		pass

    def test_user_removes_nonexisting_recommendation(self):
		pass
