from app import app
from flask import render_template, request, redirect
from services.user_service import UserService
from services.recommendation_service import RecommendationService



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["get", "post"])
def login():
    pass


@app.route("/logout")
def logout():
    pass


@app.route("/sign_up", methods=["get", "post"])
def sign_up():
    pass
