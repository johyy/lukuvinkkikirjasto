import unittest
from entities import recommendation

class TestRecommendation(unittest.TestCase):
    def setUp(self):
        self.recommendation = recommendation.Recommendation(title="HTML-vinkkisivu", link="https://www.jediakatemia.fi/", user_id="1")

    def test_create_recommendation(self):
        self.assertEqual(self.recommendation.get_title(), "HTML-vinkkisivu")
        self.assertEqual(self.recommendation.get_link(), "https://www.jediakatemia.fi/")

    def test_set_title(self):
        self.recommendation.set_title("Hyötysivu")
        self.assertEqual(self.recommendation.get_title(), "Hyötysivu")

    def test_set_user_id(self):
        self.recommendation.set_user_id(1)
        self.assertEqual(self.recommendation.get_user_id(), 1)

    def test_set_link(self):
        self.recommendation.set_link("https://www.ärdetfredag.se/")
        self.assertEqual(self.recommendation.get_link(), "https://www.ärdetfredag.se/")

    def test_set_media(self):
        self.recommendation.set_media("Kirja")
        self.assertEqual(self.recommendation.get_media(), "Kirja")

    def test_set_author(self):
        self.recommendation.set_author("Kirjailija")
        self.assertEqual(self.recommendation.get_author(), "Kirjailija")

    def test_set_description(self):
        self.recommendation.set_description("Kuvaus")
        self.assertEqual(self.recommendation.get_description(), "Kuvaus")

    def test_set_isbn(self):
        self.recommendation.set_isbn("1100")
        self.assertEqual(self.recommendation.get_isbn(), "1100")