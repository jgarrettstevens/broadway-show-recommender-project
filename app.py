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
    if show_recommendation == "MJ: The Musical":
      return render_template("results_MJ.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "A Strange Loop":
      return render_template("results_SL.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "POTUS":
      return render_template("results_POTUS.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "...what the end will be":
      return render_template("results_WTEWB.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "Slave Play":
      return render_template("results_SP.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "Little Shop of Horrors":
      return render_template("results_LS.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "SUFFS":
      return render_template("results_SUFFS.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    elif show_recommendation == "Fat Ham":
      return render_template("results_FH.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    # return render_template("results.html", user_name = user_name, user_show_type = user_show_type, user_location = user_location, user_genre = user_genre, show_recommendation = show_recommendation)
    
  else:
    return render_template("error.html")