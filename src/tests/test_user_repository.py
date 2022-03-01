import unittest
from repositories.user_repository import UserRepository
from entities.user import User_account

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.username = "testi"

    def test_insert_user_into_database(self):
        UserRepository.add_a_new_user(self, User_account(username="testi2", password="salasana11#"))
        user = UserRepository.get_user(self, "testi2")
        self.assertEqual(user[0], "testi2")
