from app import app 
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask.ext.security import login_required, login_user, logout_user


users_blueprint = Blueprint("users", __name__, template_folder="templates") 

@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@users_blueprint.route("/logout")
def logout():
    logout_user()
    flash("You just logged out")
    referer = request.headers.get("Referer")
    return redirect(referer or url_for("show_places"))