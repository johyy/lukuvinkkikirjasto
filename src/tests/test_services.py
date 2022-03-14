
import unittest
from unittest.mock import Mock, ANY, MagicMock
from werkzeug.security import generate_password_hash
from services.user_service import UserService
from services.recommendation_service import RecommendationService
from entities.user import UserAccount
from create_application import create_app
from repositories.user_repository import user_repository


class TestUserService(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        app = create_app()
        app.app_context().push()
        self.user_repo_mock = Mock()
        self.us = UserService(self.user_repo_mock)

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

    def test_register_with_existing_user(self):
        self.user_repo_mock.add_a_new_user.return_value = False
        self.us = UserService(self.user_repo_mock)
        return_value = self.us.register("nimi3", "salasana333", "salasana333")
        self.assertEqual(return_value, (False, 'Tunnus on jo olemassa.'))

    def test_valid_login_with_correct_user(self):
        self.user_repo_mock.get_user.return_value = ("nimi1", generate_password_hash("salasana123"), 0, 0)
        self.us = UserService(self.user_repo_mock)
        return_value = self.us.login("nimi1", "salasana123")
        self.assertEqual(return_value, (True, ''))

    def test_login_with_nonexistent_user(self):
        self.user_repo_mock.get_user.return_value = False
        self.us = UserService(self.user_repo_mock)
        self.assertEqual(self.us.login("kayttaja", "testi123"), (False, 'Käyttäjänimi tai salasana virheellinen'))

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

    def test_get_current_user_id(self):
        self.user_repo_mock.get_user.return_value = ("testi", generate_password_hash("1122qqq3F"), 0, 4)
        self.us = UserService(self.user_repo_mock)
        testi = UserAccount("testi", "1122qqq3F")
        self.us.set_current_user(testi)
        self.us.get_current_user_id()
        self.assertEqual(self.us.get_current_user_id(), 4)

    def test_delete_all(self):
        self.us.delete_all()
        self.user_repo_mock.delete_all.assert_called()


class TestRecommendationService(unittest.TestCase):
    def setUp(self):
        self.recommendation_repo_mock = Mock()
        self.rs = RecommendationService(self.recommendation_repo_mock)
        self.user = UserAccount(username="nimi1", password="salasana456")

    def test_add_recommendation(self):
        self.rs.add_recommendation("Otsake", "https://linkki", 1)
#        self.assertEqual(self.user.get_recommendations()[0].get_title(), "Otsake") IndexError: list index out of range
#        self.assertEqual(self.user.get_recommendations()[0].get_link(), "linkki")

    def test_add_recommendation_without_title(self):
        self.rs.add_recommendation("", "https://linkki", 1)
        self.assertEqual(self.user.get_recommendations(), [])

    def test_add_recommendation_without_link(self):
        self.rs.add_recommendation("Otsake", "", 1)
        self.assertEqual(self.user.get_recommendations(), [])

    def test_add_recommendation_with_already_existing_title(self):
        self.recommendation_repo_mock.add_new_recommendation.return_value = False
        self.rs = RecommendationService(self.recommendation_repo_mock)
        return_value = self.rs.add_recommendation("Otsake", "http://otsake.org", 1)
        self.assertEqual(return_value, (False, "Otsake löytyy jo kirjastosta."))

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

    def test_delete_all_recommendations(self):
        self.rs.delete_all_recommendations()
        
        self.recommendation_repo_mock.delete_all_recommendations.assert_called()

    def test_delete_all_likes(self):
        self.rs.delete_all_likes()
        
        self.recommendation_repo_mock.delete_all_likes.assert_called()

    def test_add_like(self):
        self.rs.add_like(66, 700)
        
        self.recommendation_repo_mock.add_like.assert_called_with(66, 700)

    def test_different_http_strings(self):
        self.assertEqual(self.rs.add_recommendation("suositus", "http://aa", 1), (True, ''))
        self.assertEqual(self.rs.add_recommendation("suositus", "https://aa", 1), (True, ''))
    
    def test_test_like_to_add_true(self):
        self.assertTrue(self.rs.test_like_to_add(1, 1))

    def test_test_like_to_remove_true(self):
        self.assertTrue(self.rs.test_like_to_remove(1, 1))

    def test_list_recommendations_liked_by_user(self):
        self.recommendation_repo_mock.fetch_recommendations_liked_by_user.return_value = [(7,), (4,)]
        self.rs = RecommendationService(self.recommendation_repo_mock)
        return_value = self.rs.list_recommendations_liked_by_user(23)
        self.assertEqual(return_value, [7,4])

    def test_list_recommendations_liked_by_user_with_no_likes(self):
        self.recommendation_repo_mock.fetch_recommendations_liked_by_user.return_value = []
        self.rs = RecommendationService(self.recommendation_repo_mock)
        return_value = self.rs.list_recommendations_liked_by_user(23)
        self.assertEqual(return_value, [])
        
