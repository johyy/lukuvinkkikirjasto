import unittest
import os
from repositories.recommendation_repository import recommendation_repository
from entities.recommendation import Recommendation
from create_application import create_app

class TestRecommendationRepository(unittest.TestCase):

    def setUpClass():
        app = create_app()
        app.app_context().push()

    def setUp(self):
        self.test_recom = Recommendation(title="Harry Potter", link="http://www.harrypotter.com")
        recommendation_repository.add_new_recommendation(self.test_recom)

    #def tearDown(self):
    #    os.remove('src/test-database.db')
    
    def test_one(self):
        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual("Harry Potter", fetch_all[0][1])
    
    def test_test_like_true(self):
        self.assertTrue(recommendation_repository.test_like(3, 3))
    
    def test_test_like_false(self):
        recommendation_repository.test_like(2, 2)
        self.assertFalse(recommendation_repository.test_like(2, 2))
    
    def test_add_like(self):
        recommendation_repository.add_like(1, 15)
        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual(15, fetch_all[0][5])

    """
    def setUpClass():
        # Create test users
        sql = "INSERT INTO tests.users (username, password, is_admin) VALUES ('jaakko', 'jaakko', False)"
        db.session.execute(sql)
        
        sql = "INSERT INTO tests.users (username, password, is_admin) VALUES ('pekka', 'pekka', False)"
        db.session.execute(sql)
        db.session.commit()
        
        # Get respective IDs from the username
        sql = "SELECT id FROM tests.users WHERE username='jaakko'"
        jaakko_id = db.session.execute(sql).fetchone()[0]
        
        sql = "SELECT id FROM tests.users WHERE username='pekka'"
        pekka_id = db.session.execute(sql).fetchone()[0]
        
        # Insert test data into recommendations table
        
        sql = "INSERT INTO tests.recommendations (user_id, media, header, author, description, url_link, isbn, creation_time)" \
                 " VALUES (:id, 'Book', 'Harry Potter', 'JK Rowling', 'It is magic', 'www.harrrypotter.com', 'None', NOW())"
        db.session.execute(sql, {"id":jaakko_id})
        
        sql = "INSERT INTO tests.recommendations (user_id, media, header, author, description, url_link, isbn, creation_time)" \
                 " VALUES (:id, 'Book', 'War And Peace', 'Leo Tolstoi', 'It is war and peace', 'None', 'None', NOW())"
        db.session.execute(sql, {"id":pekka_id})
        db.session.commit()
    
    def test_db(self):
        sql = "SELECT username FROM tests.users U WHERE username = 'jaakko'"
        result = db.session.execute(sql).fetchone()
        self.assertEqual('jaakko', result[0])
    
    def test_correct_default_order_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,testing=True)
        self.assertEqual('Harry Potter', result[0][0])
        self.assertEqual('jaakko', result[0][4])
    
    def test_correct_header_first_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,sort_option = "3", testing=True)
        self.assertEqual('Harry Potter', result[0][0])
        self.assertEqual('jaakko', result[0][4])
    
    def test_correct_header_last_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,sort_option = "4", testing=True)
        self.assertEqual('War And Peace', result[0][0])
        self.assertEqual('pekka', result[0][4])
    
    def test_correct_author_first_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,sort_option = "5", testing=True)
        self.assertEqual('JK Rowling', result[0][1])
    
    def test_correct_author_last_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,sort_option = "6", testing=True)
        self.assertEqual('Leo Tolstoi', result[0][1])
    
    def test_correct_username_first_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,sort_option = "7", testing=True)
        self.assertEqual('jaakko', result[0][4])
    
    def test_correct_username_last_fetch_all_tips(self): 
        result = self.tip_repository.fetch_all_tips(self.tip_repository,sort_option = "8", testing=True)
        self.assertEqual('pekka', result[0][4])
    
    def tearDownClass():
        sql = "DELETE FROM tests.recommendations CASCADE"
        db.session.execute(sql)
        sql = "DELETE FROM tests.users CASCADE"
        db.session.execute(sql)
        db.session.commit()"""

