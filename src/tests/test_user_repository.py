import unittest
from repositories.user_repository import user_repository
from entities.user import UserAccount
from create_application import create_app

class TestUserRepository(unittest.TestCase):

    def setUpClass():
        app = create_app()
        app.app_context().push()

    def setUp(self):
        self.test_user = UserAccount("jtyope", "kayttaja123")

    def test_insert_user_into_database(self):
        user_repository.add_a_new_user(self.test_user)
        user = user_repository.get_user(self.test_user.get_username())
        self.assertEqual(user[0], self.test_user.get_username())
