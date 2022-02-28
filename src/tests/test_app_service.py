import unittest
from services.app_service import AppService
from entities.user import User_account

class TestAppService(unittest.TestCase):
    def setUp(self):
        self.user = User_account(username="nimi", password="salasana456")
        self.apps = AppService()

    def test_register(self):
        user = self.apps.register("nimi1", "salasana123")
        self.assertEqual(user.get_username(), "nimi1")
        self.assertEqual(user.get_password(), "salasana123")

    def test_register_with_too_short_username(self):
        user = self.apps.register("ni", "salasana123")
        self.assertEqual(user, None)

    def test_register_with_too_short_password(self):
        user = self.apps.register("nimi2", "s123")
        self.assertEqual(user, None)

    def test_register_with_password_missing_special_case(self):
        user = self.apps.register("nimi3", "salasana")
        self.assertEqual(user, None)
