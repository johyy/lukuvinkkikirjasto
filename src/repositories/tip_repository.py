from db import db

class TipRepository:
    """Class that handles database queries for tips"""

    def __init__(self):
        """Class constructor"""

    def add_new_tip(self, user_id, recommendation):
        try:
            sql = "INSERT INTO recommendations (user_id, media, header, author, " \
                "description, url_link, isbn, creation_time) VALUES (:user_id, :media, :header, :author, :description," \
                ":url_link, :isbn, NOW())"
            db.session.execute(sql, {"user_id": user_id, "media": recommendation.get_media(), "header": recommendation.get_title(), "author": recommendation.get_author(),
                                          "description": recommendation.get_description(), "url_link": recommendation.get_link(), "isbn": recommendation.get_isbn()})
            db.session.commit()
            return True
        except Exception:
            return False
    
    def order_by(self, sort_option):
        order_by = ""
        
        if sort_option=="1": order_by += " ORDER BY R.creation_time DESC"
        if sort_option=="2": order_by += " ORDER BY R.creation_time ASC"
        if sort_option=="3": order_by += " ORDER BY R.header ASC"
        if sort_option=="4": order_by += " ORDER BY R.header DESC"
        if sort_option=="5": order_by += " ORDER BY R.author ASC"
        if sort_option=="6": order_by += " ORDER BY R.author DESC"
        if sort_option=="7": order_by += " ORDER BY U.username ASC"
        if sort_option=="8": order_by += " ORDER BY U.username DESC"

        return order_by

    def fetch_all_tips(self, sort_option="1"):
        sql = "SELECT R.header, R.author, R.description, R.creation_time, U.username"\
              " FROM recommendations R LEFT JOIN users U ON R.user_id=U.id"

        sql += " " + self.order_by(self, sort_option); 

        result = db.session.execute(sql)
        return result.fetchall()

tip_repository = TipRepository() 

