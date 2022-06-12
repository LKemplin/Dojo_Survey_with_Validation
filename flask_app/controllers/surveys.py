from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.survey import Survey

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/survey", methods=["POST"])
def survey():
    if not Survey.validate_survey(request.form):
        return redirect ("/")
    data = {
        'name' : request.form['name'],
        'location' : request.form['location'],
        'language' : request.form['language'],
        'comment' : request.form['comment']
    }
    session["survey_id"] = Survey.create_survey(data)
    return redirect("/submission")

@app.route("/submission")
def submission():
    print(session["survey_id"])
    return render_template("submission.html", survey = Survey.get_one({"id": session["survey_id"]}))

@app.route("/clear")
def reset():
    session.clear()
    return redirect("/")