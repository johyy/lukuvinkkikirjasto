from flask import render_template, request, redirect, url_for
from app import app
from services.user_service import user_service
from services.recommendation_service import recommendation_service


@app.route("/")
def index():
    recommendations_list = recommendation_service.list_all_recommendations()
    return render_template("index.html", sort_option="1", recommendations_list=recommendations_list)


@app.route("/sort_by", methods=["POST"])
def sort_by():
    sort_option = request.form["sort_option"]
    return redirect(url_for("index_sorted", sort_option=sort_option))


@app.route("/<sort_option>")
def index_sorted(sort_option):

    recommendations_list = recommendation_service.list_all_recommendations(
        sort_option)
    return render_template("index.html", sort_option=sort_option, recommendations_list=recommendations_list)


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        success, error = user_service.login(username, password)
        if not success:
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
        username = request.form["username"]
        password = request.form["password"]
        password_again = request.form["password_again"]

        valid, error = user_service.register(
            username, password, password_again)
        if not valid:
            return render_template("register.html", error=error)
        user_service.login(username, password)
        return redirect("/")


@app.route("/add_recommendation", methods=["get", "post"])
def add_recommendation():

    if request.method == "GET":
        return render_template("add_recommendation.html")

    if request.method == "POST":
        # csfr-token

        media = request.form["media"]
        title = request.form["title"]
        link = request.form["url"]

        # if media == "Kirja":
        #    author = request.form["author"]
        #    isbn = request.form["isbn"]

        succes, error = recommendation_service.add_recommendation(title, link)
        if succes:
            return render_template("add_recommendation.html", media_added=True)
        else:
            return render_template("add_recommendation.html", media=media, input_error=error)


@app.route("/choose_media", methods=["post"])
def choose_media():

    if request.method == "POST":
        # csfr-token

        media = request.form["media"]
        if media == "":
            return render_template("add_recommendation.html", media_error="Valise media")

        return render_template("add_recommendation.html", media=media)

@app.route("/likes", methods=["post"])
def add_like():
    recommendation_id  = request.form['recommendation_id']
    recommendation_like_amount = request.form['recommendation_like_amount']
    print(recommendation_id + " on id")
    total_likes = int(recommendation_like_amount) + 1
    recommendation_service.add_like(recommendation_id, total_likes)
    
    return redirect('/')
