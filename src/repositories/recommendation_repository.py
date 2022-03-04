from sqlalchemy.exc import IntegrityError
from db import db


class RecommendationRepository:
    """Class that handles database queries for recommendations"""

    def __init__(self):
        """Class constructor"""

    def add_new_recommendation(self, recommendation):
        try:
            sql = """INSERT INTO recommendations (title, link) VALUES (:title, :link)"""
            db.session.execute(sql, {"title": recommendation.get_title(),  "link": recommendation.get_link(
            )})

            # sql = "INSERT INbO recommendations (user_id, media, title, author, " \
            #    "description, link, isbn, creation_time) VALUES (:user_id, :media, :title, :author, :description," \
            #    ":link, :isbn, NOW())"
            # db.session.execute(sql, {"user_id": user_id, "media": recommendation.get_media(), "title": recommendation.get_title(), "author": recommendation.get_author(),
            #                              "description": recommendation.get_description(), "link": recommendation.get_link(), "isbn": recommendation.get_isbn()})
            db.session.commit()
            return True
        except IntegrityError:
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

    def fetch_all_recommendations(self, sort_option="1", testing=False):
        sql = "SELECT title, author, description, link"\
              " FROM recommendations"
        """
        sql = "SELECT R.title, R.author, R.description, U.username"\
              " FROM recommendations R LEFT JOIN users U ON R.user_id = U.id"
        if (testing):
            sql = "SELECT R.title, R.author, R.description, R.creation_time, U.username"\
              " FROM tests.recommendations R LEFT JOIN tests.users U ON R.user_id = U.id"
        sql += " " + self.order_by(self, sort_option)
        """
        result = db.session.execute(sql)

        return result.fetchall()


recommendation_repository = RecommendationRepository()
