import unittest
from repositories.user_repository import user_repository
from entities.user import UserAccount


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        user_repository.delete_all()
        self.test_user = UserAccount("jtyope", "kayttaja123")

    def test_insert_user_into_database(self):
        user_repository.add_a_new_user(self.test_user)
        user = user_repository.get_user(self.test_user.get_username())
        self.assertEqual(user[0], self.test_user.get_username())

    def test_false_user_into_database(self):
        self.assertFalse(user_repository.add_a_new_user("testi"))

    def test_get_user_by_id(self):
        user_repository.add_a_new_user(self.test_user)
        self.assertEqual(user_repository.get_user_by_id(1), ('jtyope', 'kayttaja123', 0, 1))

    def test_false_id(self):
        user_repository.add_a_new_user(self.test_user)
        self.assertFalse(user_repository.get_user_by_id(2), False)

    def test_delete_all(self):
        user_repository.add_a_new_user(self.test_user)
        user_repository.delete_all()
        self.assertEqual(user_repository.get_user(self.test_user.get_username()), False)