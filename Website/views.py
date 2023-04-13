from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
5
@views.route('/About-Me')
def AboutMe():
    return render_template("AboutMe.html")