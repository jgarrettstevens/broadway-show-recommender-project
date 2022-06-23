# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_show_recommendation


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ["GET", "POST"])
def results():
  if request.method == "POST":
    user_name = request.form["name"]
    user_show_type = request.form["show_type"]
    user_location = request.form["show_location"]
    user_genre = request.form["show_genre"]
    show_recommendation =  get_show_recommendation(user_show_type, user_location, user_genre)
    return render_template("results.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    
  else:
    return render_template("error.html")