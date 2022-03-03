import unittest
from services.app_service import AppService
from entities.user import User_account
from create_application import create_app

class TestAppService(unittest.TestCase):
    def setUp(self):

        app = create_app()
        app.app_context().push()

        self.user = User_account(username="nimi", password="salasana456")
        self.apps = AppService()

    def test_register(self):
        self.assertTrue(self.apps.register("nimi1", "salasana123", "salasana123"))
 
    def test_register_with_too_short_username(self):
        self.assertEqual(self.apps.register("ni", "salasana123", "salasana123"), (False, 'Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.'))

    def test_register_with_too_short_password(self):
        self.assertEqual(self.apps.register("nimi2", "s123", "s123"), (False, 'Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.'))

    def test_register_with_password_missing_special_case(self):
        self.assertEqual(self.apps.register("nimi3", "salasana", "salasana"), (False, 'Tunnuksessa oltava vähintään 3 merkkiä ja salasanassa vähintään 8 merkkiä ja vähintään yksi numero tai erikoismerkki.'))

    def test_register_with_nonmatchin_passwords(self):
        self.assertEqual(self.apps.register("nimi3", "salasana333", "salasana334"), (None, 'Salasanat eivät täsmää'))
    
#    def test_login_with_incorrect_user(self):
#        self.assertEqual(self.apps.login("nimi", "salasana456"), (False, 'Käyttäjänimi tai salasana virheellinen'))
 
#    def test_login_with_correct_user(self):
#        self.apps.register("nimi1", "salasana123", "salasana123")
#        self.assertTrue(self.apps.login("nimi1", "salasana456"))
    
#    def test_login_with_incorrect_password(self):
#        self.apps.register("nimi1", "salasana123", "salasana123")
#        self.assertEqual(self.apps.login("nimi1", "salasana456"), (False, 'Käyttäjänimi tai salasana virheellinen'))
    
    def test_login_with_empty_user(self):
        self.assertEqual(self.apps.login("", "salasana456"), (False, 'Käyttäjänimi tai salasana virheellinen'))
    
    def test_login_with_empty_password(self):
        self.assertEqual(self.apps.login("nimi1", ""), (False, 'Käyttäjänimi tai salasana virheellinen'))
    
    def test_login_with_empty_user_and_empty_password(self):
        self.assertEqual(self.apps.login("", ""), (False, 'Käyttäjänimi tai salasana virheellinen'))
