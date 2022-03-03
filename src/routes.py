from flask import render_template, request, redirect, url_for
from app import app
from services.recommendation_service import RecommendationService as recommendation_service
from services.app_service import AppService as app_service
from services.user_service import UserService as user_service
from repositories.recommendation_repository import RecommendationRepository as recommendation_repository


@app.route("/")
def index():
    recommendations_list = recommendation_repository.fetch_all_recommendations(recommendation_repository)
    return render_template("index.html", sort_option="1", recommendations_list=recommendations_list)


@app.route("/sort_by", methods=["POST"])
def sort_by():
    sort_option = request.form["sort_option"]
    return redirect(url_for("index_sorted", sort_option=sort_option))


@app.route("/<sort_option>")
def index_sorted(sort_option):

    recommendations_list = recommendation_repository.fetch_all_recommendations(
        recommendation_repository, sort_option)
    return render_template("index.html", sort_option=sort_option, recommendations_list=recommendations_list)


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success, error = app_service.login(app_service, username, password)
        if not success:
            return render_template("login.html", error=error)
        return redirect("/")


@app.route("/logout")
def logout():
    app_service.logout(app_service)
    return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password_again = request.form["password_again"]

        valid, error = app_service.register(
            app_service, username, password, password_again)
        if not valid:
            return render_template("register.html", error=error)
        app_service.login(app_service, username, password)
        return redirect("/")

@app.route("/add_recommendation", methods=["get", "post"])
def add_recommendation():

    if request.method == "GET":
        return render_template("add_recommendation.html")

    if request.method == "POST":
        #csfr-token

        media = request.form["media"]
        if "header" not in request.form or "url" not in request.form:
            return render_template("add_recommendation.html", media=media, input_error="Täytä kaikki tiedot")
        if media == "book":
            if "author" not in request.form or "isbn" not in request.form:
                return render_template("add_recommendation.html", media=media, input_error="Täytä kaikki tiedot")
        
        return render_template("add_recommendation.html", media_added=True)


        
        return render_template("add_recommendation.html", media=media)

@app.route("/choose_media", methods=["post"])
def choose_media():

    if request.method == "POST":
        #csfr-token

        media = request.form["media"]
        if media == "":
            return render_template("add_recommendation.html", media_error="Valise media")

        
        return render_template("add_recommendation.html", media=media)
