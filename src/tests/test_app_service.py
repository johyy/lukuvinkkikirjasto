import unittest
from services.app_service import AppService
from entities.user import User_account
from app import create_app
from db import db

class TestAppService(unittest.TestCase):
    def setUp(self):
        app = create_app()
        app.app_context().push()
        with app.app_context():
            from entities.user import User_account
            from entities.recommendation import Recommendation
            db.create_all()
            db.session.commit()
        self.user = User_account(username="nimi", password="salasana456")
        self.apps = AppService()

    def test_register(self):
        user = self.apps.register("nimi1", "salasana123", "salasana123")
        self.assertEqual(user.get_username(), "nimi1")
        self.assertEqual(user.get_password(), "salasana123")

    def test_register_with_too_short_username(self):
        user = self.apps.register("ni", "salasana123", "salasana123")
        self.assertEqual(user[0], None)

    def test_register_with_too_short_password(self):
        user = self.apps.register("nimi2", "s123", "s123")
        self.assertEqual(user[0], None)

    def test_register_with_password_missing_special_case(self):
        user = self.apps.register("nimi3", "salasana", "salasana")
        self.assertEqual(user[0], None)

    def test_register_with_nonmatchin_passwords(self):
        user = self.apps.register("nimi3", "salasana333", "salasana334")
        self.assertEqual(user[0], None)
