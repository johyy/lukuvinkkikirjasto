import unittest
from repositories.tip_repository import TipRepository
from entities.recommendation import Recommendation


class TestTipRepository(unittest.TestCase):

    def test_add_tip_to_db(self):
        TipRepository.add_new_tip()
