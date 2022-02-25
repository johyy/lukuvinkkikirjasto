from db import db

class TipRepository:
    """Class that handles database queries for tips"""

    def __init__(self):
        """Class constructor"""


    def add_new_tip(self, user_id, media, header, author, description, url_link, isbn):
        try:
            sql = "INSERT INTO recommendations (user_id, media, header, author," \
                "description, url_link, isbn) VALUES (:user_id, :media, :header, :author, :description," \
                ":url_link, :isbn)"
            db.session.execute(sql, {"user_id": user_id, "media": media, "header": header, "author": author,
                                          "description": description, "url_link": url_link, "isbn": isbn})
            db.session.commit()
            return True
        except Exception:
            return False