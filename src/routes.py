from app import app
from flask import render_template, request, redirect, url_for
from services.user_service import UserService as user_service
from services.recommendation_service import RecommendationService as recommendation_service
from repositories.tip_repository import TipRepository as tip_repository

@app.route("/sort_by", methods = ["POST"])
def sort_by():
    sort_option = request.form["sort_option"]
    return redirect(url_for("index", sort_option=sort_option))

@app.route("/<sort_option>")
def index(sort_option):
    
    print(sort_option)
    # tip_repository.add_new_tip(tip_repository, 2, "Book", "Third Book", "Jones", "It's a book", "google.com", "0000")
    recommendations_list = tip_repository.fetch_all_tips(tip_repository, sort_option)

    return render_template("index.html", sort_option=sort_option, recommendations_list=recommendations_list)


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        valid, error = user_service.login(name, password)
        # Erilaiset error-viestit luotava user_servicessä,
        # jolloin oikean viestin voi palauttaa suoraan kyseisestä virheestä
        # (esim. puuttuuko jostain kentästä jotain,
        # , onko salasana väärä tms.
        # validate palauttaa siis joko True, "" tai False, "*virheen syy*")

        if not valid:
            return render_template("login.html", error=error)
        return redirect("/")


@app.route("/logout")
def logout():
    user_service.logout()
    return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        password_again = request.form["password_again"]

        valid, error = user_service.validate(name, password, password_again)
        if not valid:
            return render_template("sign_up.html", error=error)

        # Erilaiset error-viestit luotava user_servicessä,
        # jolloin oikean viestin voi palauttaa suoraan kyseisestä virheestä
        # (esim. puuttuuko jostain kentästä jotain,
        # , onko nimimerkki varattu tai salasana epäkelpo tms.
        # validate palauttaa siis joko True, "" tai False, "*virheen syy*")

        valid, error = user_service.register(name, password)
        if valid:
            return redirect("/")
        return render_template("register.html", error=error)

