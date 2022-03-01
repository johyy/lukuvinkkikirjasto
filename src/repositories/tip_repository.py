from db import db

class TipRepository:
    """Class that handles database queries for tips"""

    def __init__(self):
        """Class constructor"""

    def add_new_tip(self, user_id, recommendation):
        db.session.add(recommendation)
        db.session.commit()
        return True

    def order_by(self, sort_option):
        order_by = ""

        if sort_option=="1": order_by += "ORDER BY R.creation_time DESC"
        if sort_option=="2": order_by += "ORDER BY R.creation_time ASC"
        if sort_option=="3": order_by += "ORDER BY R.header ASC"
        if sort_option=="4": order_by += "ORDER BY R.header DESC"
        if sort_option=="5": order_by += "ORDER BY R.author ASC"
        if sort_option=="6": order_by += "ORDER BY R.author DESC"
        if sort_option=="7": order_by += "ORDER BY U.username ASC"
        if sort_option=="8": order_by += "ORDER BY U.username DESC"

        return order_by

    def fetch_all_tips(self, sort_option="1", testing=False):
    
        sql = "SELECT R.header, R.author, R.description, R.creation_time, U.username"\
              " FROM recommendations R LEFT JOIN users U ON R.user_id = U.id"

        if (testing):
            sql = "SELECT R.header, R.author, R.description, R.creation_time, U.username"\
              " FROM tests.recommendations R LEFT JOIN tests.users U ON R.user_id = U.id"

        sql += " " + self.order_by(self, sort_option)

        result = db.session.execute(sql)
        
        return result.fetchall()
        

tip_repository = TipRepository()
