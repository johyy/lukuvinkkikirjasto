from app import app
from flask import render_template, request, redirect, url_for
from services.recommendation_service import RecommendationService as recommendation_service
from services.app_service import AppService as app_service
from repositories.tip_repository import TipRepository as tip_repository
from services.user_service import UserService as user_service


@app.route("/")
def index():
    recommendations_list = tip_repository.fetch_all_tips(tip_repository)

    return render_template("index.html", sort_option="1", recommendations_list=recommendations_list)


@app.route("/sort_by", methods=["POST"])
def sort_by():
    sort_option = request.form["sort_option"]
    return redirect(url_for("index_sorted", sort_option=sort_option))


@app.route("/<sort_option>")
def index_sorted(sort_option):

    recommendations_list = tip_repository.fetch_all_tips(
        tip_repository, sort_option)
    return render_template("index.html", sort_option=sort_option, recommendations_list=recommendations_list)


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        valid, error = app_service.login(name, password)
        if not valid:
            return render_template("login.html", error=error)
        return redirect("/")


@app.route("/logout")
def logout():
    app_service.logout()
    return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        password_again = request.form["password_again"]

        valid, error = app_service.validate(name, password, password_again)
        if not valid:
            return render_template("register.html", error=error)

        valid, error = app_service.register(name, password)
        if valid:
            return redirect("/")
        return render_template("register.html", error=error)
