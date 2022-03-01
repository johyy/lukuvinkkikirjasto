import unittest
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class TestTipRepository(unittest.TestCase):
    def setUpClass():
        pass

    def setUp(self):
        sql = "SELECT R.header, R.author, R.description, R.creation_time, U.username"\
              " FROM recommendations R LEFT JOIN users U ON R.user_id=U.id"

        result = db.session.execute(sql)
        result.fetchall()
        pass

    def tearDown(self):
        pass

    def test_db(self):
        pass

    # def tearDownClass():
    #     sql = "DROP TABLE tests ON CASCADE"
    #     db.session.execute(sql)
