from datetime import datetime,timedelta
from flask import Blueprint, Response, jsonify, render_template,current_app, request


app_Router = Blueprint('index',__name__)

@app_Router.route("/")
def page():
    return render_template("index.html")