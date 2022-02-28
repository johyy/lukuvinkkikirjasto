import unittest
from services.app_service import AppService
from entities.user import User

class TestAppService(unittest.TestCase):
    def setUp(self):
        self.user = User("nimi1", "salasana456")
        self.apps = AppService()

    def test_register(self):
        user = self.apps.register("nimi", "salasana123")
        self.assertEqual(user.get_username(), "nimi")
        self.assertEqual(user.get_password(), "salasana123")

    def test_register_with_too_short_username(self):
        user = self.apps.register("ni", "salasana123")
        self.assertEqual(user, None)

    def test_register_with_too_short_password(self):
        user = self.apps.register("nimi", "s123")
        self.assertEqual(user, None)

    def test_register_with_password_missing_special_case(self):
        user = self.apps.register("nimi", "salasana")
        self.assertEqual(user, None)
