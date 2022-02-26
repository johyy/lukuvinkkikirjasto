import unittest
from entities import recommendation

class TestRecommendation(unittest.TestCase):
    def setUp(self):
        self.recommendation = recommendation.Recommendation("HTML-vinkkisivu", "https://www.jediakatemia.fi/")

    def test_create_recommendation(self):
        self.assertEqual(self.recommendation.get_title(), "HTML-vinkkisivu")
        self.assertEqual(self.recommendation.get_link(), "https://www.jediakatemia.fi/")

    def test_set_title(self):
        self.recommendation.set_title("Hyötysivu")
        self.assertEqual(self.recommendation.get_title(), "Hyötysivu")

    def test_set_link(self):
        self.recommendation.set_link("https://www.ärdetfredag.se/")
        self.assertEqual(self.recommendation.get_link(), "https://www.ärdetfredag.se/")
