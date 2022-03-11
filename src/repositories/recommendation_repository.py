#from sqlalchemy.exc import IntegrityError
from sqlalchemy import select
from db import db


class RecommendationRepository:
    """Class that handles database queries for recommendations"""

    def __init__(self):
        """Class constructor"""

    def add_new_recommendation(self, recommendation):
        try:
            sql = """INSERT INTO recommendations (title, link, like_amount,
                     creation_time, visibility, user_id)
                     VALUES (:title, :link, 0, DATETIME('now'), 1, :user_id)"""

            db.session.execute(sql, {"title": recommendation.get_title(),  "link": recommendation.get_link(
            ), "user_id": recommendation.get_user_id()})

            db.session.commit()
            return True
        except:
            return False

    def order_by(self, sort_option):
        order_by = ""

        if sort_option == "1":
            order_by += "ORDER BY R.like_amount DESC, R.creation_time DESC"

        if sort_option == "2":
            order_by += "ORDER BY R.like_amount ASC, R.creation_time DESC"

        if sort_option == "3":
            order_by += "ORDER BY R.creation_time DESC"

        if sort_option == "4":
            order_by += "ORDER BY R.creation_time ASC"

        """
        if sort_option == "5":
            order_by += "ORDER BY R.author ASC"
        if sort_option == "6":
            order_by += "ORDER BY R.author DESC"
        if sort_option == "7":
            order_by += "ORDER BY U.username ASC"
        if sort_option == "8":
            order_by += "ORDER BY U.username DESC"
        """

        return order_by

    def fetch_recommendation_by_user_id(self, user_id):
        user_id_sql = (user_id,)
        print(user_id_sql)
        sql = """SELECT R.id, R.title, R.author, R.description, R.link, R.like_amount,
                 datetime(R.creation_time), date(R.creation_time) as date, time(R.creation_time) as time, U.username
		         FROM recommendations as R JOIN users as U WHERE R.user_id =:user_id AND R.user_id = U.id"""
        result = db.session.execute(sql, {"user_id": user_id})
        return result.fetchall()

    def fetch_all_recommendations(self, sort_option="1"):
        sql = """SELECT R.id, R.title, R.author, R.description, R.link,
                R.like_amount, datetime(R.creation_time), date(R.creation_time) as date, time(R.creation_time) as time, R.visibility, R.user_id, U.username
                FROM recommendations as R JOIN users as U WHERE visibility=1 AND R.user_id=U.id"""

        sql += " " + self.order_by(sort_option)
        result = db.session.execute(sql)
        return result.fetchall()

    def test_like_to_add(self, user_id, recommendation_id):
        sql = "SELECT * FROM likes WHERE user_id =:user_id AND recommendation_id =:recommendation_id"
        result = db.session.execute(
            sql, {"user_id": user_id, "recommendation_id": recommendation_id})
        if result.fetchone() is None:
            sql2 = """INSERT INTO likes (result, user_id, recommendation_id)
                      VALUES (1, :user_id, :recommendation_id)"""
            db.session.execute(
                sql2, {"user_id": user_id, "recommendation_id": recommendation_id})
            db.session.commit()
            return True
        return False
    
    def test_like_to_remove(self, user_id, recommendation_id):
        sql = "SELECT * FROM likes WHERE user_id =:user_id AND recommendation_id =:recommendation_id"
        result = db.session.execute(
            sql, {"user_id": user_id, "recommendation_id": recommendation_id})
        if result.fetchone() is not None:
            sql2 = "DELETE FROM likes WHERE user_id=:user_id AND recommendation_id=:recommendation_id"
            db.session.execute(
                sql2, {"user_id": user_id, "recommendation_id": recommendation_id})
            db.session.commit()
            return True
        return False

    def add_like(self, like_id, likes):
        sql = "UPDATE recommendations SET like_amount = :likes WHERE id = :id"
        db.session.execute(sql, {"likes": likes, "id": like_id})
        db.session.commit()
    
    def fetch_recommendations_liked_by_user_id(self, user_id):
        sql = "SELECT recommendation_id FROM likes WHERE user_id=:user_id"
        result = db.session.execute(sql, {"user_id": user_id})
        return result.fetchall()

    def delete_recommendation(self, rec_id):
        sql = "DELETE FROM recommendations WHERE id = :id"
        db.session.execute(sql, {"id": rec_id})
        db.session.commit()

    def delete_all_recommendations(self):
        sql = """DELETE FROM recommendations"""
        db.session.execute(sql)
        db.session.commit()

    def delete_all_likes(self):
        sql = """DELETE FROM likes"""
        db.session.execute(sql)
        db.session.commit()


recommendation_repository = RecommendationRepository()
