import unittest
from repositories.stub_user_repository import StubUserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.username = "testi"
        self.password = "salasana"
        self.admin = False

    def test_insert_user_into_database(self):
        StubUserRepository.add_a_new_user(self, "testi", "salasana", False)
        user = StubUserRepository.get_user(self, "testi")
        print(user)
        self.assertEqual(user[0], self.usernamer)
