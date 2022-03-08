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
        self.test_recom = Recommendation(title="Harry Potter", link="http://www.harrypotter.com", user_id=3)
        recommendation_repository.add_new_recommendation(self.test_recom)

    #def tearDown(self):
    #    os.remove('src/test-database.db')
    
    def test_fetch_first(self):
        self.test_recom = (Recommendation(title="Kirja", link="linkki", user_id=1))
        recommendation_repository.add_new_recommendation(self.test_recom)
        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual("Kirja", fetch_all[0][1])
        recommendation_repository.delete_recommendation(2)

    def test_fetch_multiple_order_default(self):
        self.assertEqual([], recommendation_repository.fetch_all_recommendations())
        recom_one = (Recommendation(title="one", link="linkki", user_id=1))
        recom_two = (Recommendation(title="two", link="linkki", user_id=1))
        recom_three = (Recommendation(title="three", link="linkki", user_id=1))
        recommendation_repository.add_new_recommendation(recom_one)
        recommendation_repository.add_new_recommendation(recom_two)
        recommendation_repository.add_new_recommendation(recom_three)

        recommendation_repository.add_like(4, 6)
        fetch_all_default = recommendation_repository.fetch_all_recommendations()
        self.assertEqual("two", fetch_all_default[0][1])
        self.assertEqual("one", fetch_all_default[1][1])
        self.assertEqual("three", fetch_all_default[2][1])

        fetch_all = recommendation_repository.fetch_all_recommendations(sort_option="1")
        self.assertEqual(fetch_all, fetch_all_default)

    def test_fetch_multiple_order_likes(self):

        recommendation_repository.add_like(3, 2)
        fetch_all = recommendation_repository.fetch_all_recommendations(sort_option="2")
        self.assertEqual("three", fetch_all[0][1])
        self.assertEqual("one", fetch_all[1][1])

        recommendation_repository.add_like(3, 6)
        recommendation_repository.add_like(5, 6)

        fetch_all = recommendation_repository.fetch_all_recommendations()
        self.assertEqual("one", fetch_all[0][1])
        self.assertEqual("three", fetch_all[2][1])
    
    def test_fetch_multiple_order_time(self):
        fetch_all_newest = recommendation_repository.fetch_all_recommendations(sort_option="3")
        self.assertEqual("three", fetch_all_newest[2][1])
        self.assertEqual("one", fetch_all_newest[0][1])
        
        fetch_all_oldest = recommendation_repository.fetch_all_recommendations(sort_option="4")
        self.assertEqual("three", fetch_all_oldest[2][1])
        self.assertEqual("one", fetch_all_oldest[0][1])

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

