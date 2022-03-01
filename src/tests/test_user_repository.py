import unittest
from repositories.stub_user_repository import StubUserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.username = "testi"

    def test_insert_user_into_database(self):
        StubUserRepository.add_a_new_user(self, "testi2", "salasana23", False)
        user = StubUserRepository.get_user(self, "testi2")
        self.assertEqual(user[0], "testi2")
