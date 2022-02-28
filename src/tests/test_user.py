import unittest
from entities.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testi", "salasana")




    def test_create_user(self):
        self.assertEqual(self.user.get_username(), "testi")
        self.assertEqual(self.user.get_password(), "salasana")

    def test_set_username(self):
        self.user.set_username("uusi")
        self.assertEqual(self.user.get_username(), "uusi")

    def test_set_password(self):
        self.user.set_password("toinen123")
        self.assertEqual(self.user.get_password(), "toinen123")
