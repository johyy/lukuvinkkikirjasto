import unittest
from repositories.recommendation_repository import recommendation_repository
from entities.recommendation import Recommendation


class TestRecommendationRepository(unittest.TestCase):

    def setUp(self):
        recommendation_repository.delete_all_recommendations()
        recommendation_repository.delete_all_likes()
        self.test_recom = Recommendation(
            title="Harry Potter", link="http://www.harrypotter.com", user_id=3)
        recommendation_repository.add_new_recommendation(self.test_recom)

    def test_fetch_first(self):
        test_recom = (Recommendation(
            title="Kirja", link="https://linkki", user_id=1))
        recommendation_repository.add_new_recommendation(test_recom)
        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual("Kirja", fetch_all[1][1])
        recommendation_repository.delete_recommendation(2)

    def test_fetch_multiple_order_default(self):
        recom_one = (Recommendation(title="one", link="https://linkki", user_id=1))
        recom_two = (Recommendation(title="two", link="https://linkki", user_id=1))
        recom_three = (Recommendation(title="three", link="https://linkki", user_id=1))
        recommendation_repository.add_new_recommendation(recom_one)
        recommendation_repository.add_new_recommendation(recom_two)
        recommendation_repository.add_new_recommendation(recom_three)

        fetch_all_default = recommendation_repository.fetch_all_recommendations()
        self.assertEqual("one", fetch_all_default[1][1])
        self.assertEqual("two", fetch_all_default[2][1])
        self.assertEqual("three", fetch_all_default[3][1])

        fetch_all = recommendation_repository.fetch_all_recommendations(
            sort_option="1")
        self.assertEqual(fetch_all, fetch_all_default)

    def test_fetch_multiple_order_likes(self):
        recom_one = (Recommendation(title="one", link="https://linkki", user_id=1))
        recom_two = (Recommendation(title="two", link="https://linkki", user_id=1))
        recom_three = (Recommendation(title="three", link="https://linkki", user_id=1))
        recommendation_repository.add_new_recommendation(recom_one)
        recommendation_repository.add_new_recommendation(recom_two)
        recommendation_repository.add_new_recommendation(recom_three)

        recommendation_repository.add_like(3, 2)
        fetch_all = recommendation_repository.fetch_all_recommendations(
            sort_option="2")
        self.assertEqual("three", fetch_all[2][1])
        self.assertEqual("one", fetch_all[1][1])

        recommendation_repository.add_like(3, 6)

        fetch_all = recommendation_repository.fetch_all_recommendations()

        self.assertEqual("two", fetch_all[0][1])

    def test_fetch_multiple_order_time(self):
        recom_one = (Recommendation(title="one", link="https://linkki", user_id=1))
        recom_two = (Recommendation(title="two", link="https://linkki", user_id=1))
        recom_three = (Recommendation(title="three", link="https://linkki", user_id=1))
        recommendation_repository.add_new_recommendation(recom_one)
        recommendation_repository.add_new_recommendation(recom_two)
        recommendation_repository.add_new_recommendation(recom_three)
        fetch_all_newest = recommendation_repository.fetch_all_recommendations(
            sort_option="3")
        self.assertEqual("three", fetch_all_newest[3][1])
        self.assertEqual("one", fetch_all_newest[1][1])

        fetch_all_oldest = recommendation_repository.fetch_all_recommendations(
            sort_option="4")
        self.assertEqual("three", fetch_all_oldest[3][1])
        self.assertEqual("one", fetch_all_oldest[1][1])

    def test_test_like_true(self):
        self.assertTrue(recommendation_repository.test_like(3, 3))

    def test_test_like_false(self):
        recommendation_repository.test_like(2, 2)
        self.assertFalse(recommendation_repository.test_like(2, 2))

    def test_add_like(self):
        recommendation_repository.add_like(1, 15)
        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual(15, fetch_all[0][5])

    def test_delete_recommendation(self):
        recommendation_repository.delete_recommendation(1)
        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual([], fetch_all)

    def test_get_recommendation_by_user_id(self):
        test_recom = Recommendation(
            title="Porri Hatter", link="http://www.porrihatter.com", user_id=1)
        recommendation_repository.add_new_recommendation(test_recom)
        test_recom = Recommendation(
            title="Kirja", link="http://www.kirja.kirja", user_id=3)
        recommendation_repository.add_new_recommendation(test_recom)
        test_recom = Recommendation(
            title="Testi", link="http://www.tes.ti", user_id=1)
        recommendation_repository.add_new_recommendation(test_recom)
        fetch_all = recommendation_repository.fetch_recommendation_by_user_id(1)

        self.assertEqual(fetch_all[1][1], "Testi")
        self.assertEqual(fetch_all[0][1], "Porri Hatter")
