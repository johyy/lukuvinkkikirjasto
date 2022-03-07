#from sqlalchemy.exc import IntegrityError
from db import db


class RecommendationRepository:
    """Class that handles database queries for recommendations"""

    def __init__(self):
        """Class constructor"""

    def add_new_recommendation(self, recommendation):
        try:
            sql = """INSERT INTO recommendations (title, link, like_amount, visibility, user_id) VALUES (:title, :link, 0, 1, 
            :user_id)"""
            db.session.execute(sql, {"title": recommendation.get_title(),  "link": recommendation.get_link(
            ), "user_id": recommendation.get_user_id()})

            # sql = "INSERT INbO recommendations (user_id, media, title, author, " \
            #    "description, link, isbn, creation_time) VALUES (:user_id, :media, :title, :author, :description," \
            #    ":link, :isbn, NOW())"
            # db.session.execute(sql, {"user_id": user_id, "media": recommendation.get_media(), "title": recommendation.get_title(), "author": recommendation.get_author(),
            #                              "description": recommendation.get_description(), "link": recommendation.get_link(), "isbn": recommendation.get_isbn()})
            db.session.commit()
            return True
        except:
            return False

    def get_recommendation_by_id(self, id):
        try:
            sql = """SELECT * FROM recommendations WHERE id =: id"""
            result = db.session.execute(sql, {"id":id})
            result.fetchone()
        except:
            return False

    def order_by(self, sort_option):
        order_by = ""

        if sort_option == "1":
            order_by += "ORDER BY R.creation_time DESC"
        if sort_option == "2":
            order_by += "ORDER BY R.creation_time ASC"
        if sort_option == "3":
            order_by += "ORDER BY R.title ASC"
        if sort_option == "4":
            order_by += "ORDER BY R.title DESC"
        if sort_option == "5":
            order_by += "ORDER BY R.author ASC"
        if sort_option == "6":
            order_by += "ORDER BY R.author DESC"
        if sort_option == "7":
            order_by += "ORDER BY U.username ASC"
        if sort_option == "8":
            order_by += "ORDER BY U.username DESC"

        # return order_by
        return ""

    def fetch_recommendation_by_user_id(self, user_id):
        try:
            sql = """SELECT id, title, author, description, link, like_amount 
            FROM recommendations WHERE user_id =: user_id"""
            result = db.session.execute(sql, {"user_id": user_id})
            result.fetchall()
        except:
            return False


    def fetch_all_recommendations(self, sort_option="1", testing=False):
        result = db.session.execute("SELECT id, title, author, description, link, "
                                   "like_amount, user_id, visibility FROM recommendations WHERE visibility = 1")
        """
        sql = "SELECT R.title, R.author, R.description, U.username"\
              " FROM recommendations R LEFT JOIN users U ON R.user_id = U.id"
        if (testing):
            sql = "SELECT R.title, R.author, R.description, R.creation_time, U.username"\
              " FROM tests.recommendations R LEFT JOIN tests.users U ON R.user_id = U.id"
        sql += " " + self.order_by(self, sort_option)
        """
        rec_list = result.fetchall()

        return rec_list
    
    def test_like(self, user_id, recommendation_id):
        sql = "SELECT * FROM likes WHERE user_id =:user_id AND recommendation_id =:recommendation_id"
        result = db.session.execute(sql, {"user_id": user_id, "recommendation_id": recommendation_id})
        if result.fetchone() == None:
            sql2 = "INSERT INTO likes (result, user_id, recommendation_id) VALUES (1, :user_id, :recommendation_id)"
            db.session.execute(sql2, {"user_id": user_id, "recommendation_id": recommendation_id})
            db.session.commit()
            return True
        return False
       
    
    def add_like(self, id, likes):
        sql = "UPDATE recommendations SET like_amount = :likes WHERE id = :id"
        db.session.execute(sql, {"likes": likes, "id": id})
        db.session.commit()

    def delete_recommendation(self, id):
        visibility = 0
        sql = "UPDATE recommendations SET visibility = :visibility  WHERE id = :id"
        db.session.execute(sql, {"visibility": visibility, "id": id})
        db.session.commit()


recommendation_repository = RecommendationRepository()
