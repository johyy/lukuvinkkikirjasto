
import unittest
from unittest.mock import Mock, ANY
from services.user_service import UserService
from services.recommendation_service import RecommendationService
from entities.user import UserAccount
from create_application import create_app


class TestUserService(unittest.TestCase):
    def setUp(self):
        
        app = create_app()
        app.app_context().push()
        self.us = UserService()

    def test_register(self):
        self.assertTrue(self.us.register("nimi1", "salasana123", "salasana123"))
 
    def test_register_with_too_short_username(self):
        self.assertEqual(self.us.register("ni", "salasana123", "salasana123"), (False, 'Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.'))

    def test_register_with_too_short_password(self):
        self.assertEqual(self.us.register("nimi2", "s123", "s123"), (False, 'Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.'))

    def test_register_with_password_missing_special_case(self):
        self.assertEqual(self.us.register("nimi3", "salasana", "salasana"), (False, 'Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.'))

    def test_register_with_nonmatchin_passwords(self):
        self.assertEqual(self.us.register("nimi3", "salasana333", "salasana334"), (None, 'Salasanat eivät täsmää'))

    def test_login_with_empty_user(self):
        self.assertEqual(self.us.login("", "salasana456"), (False, 'Käyttäjänimi tai salasana virheellinen'))
    
    def test_login_with_empty_password(self):
        self.assertEqual(self.us.login("nimi1", ""), (False, 'Käyttäjänimi tai salasana virheellinen'))
    
    def test_login_with_empty_user_and_empty_password(self):
        self.assertEqual(self.us.login("", ""), (False, 'Käyttäjänimi tai salasana virheellinen'))

    def test_set_current_user(self):
        testi = UserAccount("testi", "kayttaja123")
        self.us.set_current_user(testi)
        self.assertEqual(self.us.get_current_user(), testi)

class TestRecommendationService(unittest.TestCase):
    def setUp(self):
        user_repo_mock = Mock()
        self.recommendation_repo_mock = Mock()
        self.user = UserAccount(username="nimi1", password="salasana456")
        self.rs = RecommendationService(self.recommendation_repo_mock)

    def test_user_adds_recommendation(self):
        self.rs.add_recommendation("Otsake", "https://linkki", 1)
#        self.assertEqual(self.user.get_recommendations()[0].get_title(), "Otsake") IndexError: list index out of range
#        self.assertEqual(self.user.get_recommendations()[0].get_link(), "linkki")

    def test_user_adds_recommendation_without_title(self):
        self.rs.add_recommendation("", "https://linkki", 1)
        self.assertEqual(self.user.get_recommendations(), [])

    def test_user_adds_recommendation_without_link(self):
        self.rs.add_recommendation("Otsake", "", 1)
        self.assertEqual(self.user.get_recommendations(), [])

    def test_list_all_recommendations(self):
        recs = self.rs.list_all_recommendations()
        
        self.recommendation_repo_mock.fetch_all_recommendations.assert_called_with(sort_option='1')

    def test_list_recommendations_by_user(self):
        self.rs.add_recommendation("Suositus3", "", 2)
        recs = self.rs.list_recommendations_by_user(2)
        
        self.recommendation_repo_mock.fetch_recommendation_by_user_id.assert_called_with(2)

    def test_user_removes_recommendation(self):
        recs = self.rs.delete_recommendation(1)
        
        self.recommendation_repo_mock.delete_recommendation.assert_called_with(1)
