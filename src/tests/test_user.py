import unittest
from entities.user import User
from entities.recommendation import Recommendation

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testi", "salasana")
        self.recommendation = Recommendation("Otsake", "linkki")

    def test_create_user(self):
        self.assertEqual(self.user.get_username(), "testi")
        self.assertEqual(self.user.get_password(), "salasana")

    def test_set_username(self):
        self.user.set_username("uusi")
        self.assertEqual(self.user.get_username(), "uusi")

    def test_set_password(self):
        self.user.set_password("toinen123")
        self.assertEqual(self.user.get_password(), "toinen123")

    def test_add_recommendation(self):
        self.user.add_recommendation(self.recommendation)
        self.assertEqual(self.user.get_recommendations()[0], self.recommendation)

    def test_remove_recommendation(self):
        self.user.add_recommendation(self.recommendation)
        self.user.remove_recommendation(self.recommendation)
        self.assertEqual(self.user.get_recommendations(), [])

    def test_remove_nonexisting_recommendation(self):
        self.user.add_recommendation(self.recommendation)
        self.user.remove_recommendation(Recommendation("toinen", "linkki"))
        self.assertEqual(self.user.get_recommendations()[0], self.recommendation)
