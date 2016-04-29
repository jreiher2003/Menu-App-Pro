from app import app, bcrypt
from flask import Blueprint, render_template, url_for, request, flash, redirect
from flask.ext.login import login_required, login_user, logout_user
from app.forms import RegistrationForm, LoginForm
from app.models import User 


users_blueprint = Blueprint("users", __name__, template_folder="templates") 

@users_blueprint.route("/login", methods=["GET", "POST"])
def login():
    error = None
    form = LoginForm(request.form) 
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print user.email
        if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("You have signed in successfully!", "success")
            return redirect(url_for("show_places"))
        else:
            flash("<strong>Invalid Credentials.</strong> Please try again.", "danger")
            return redirect(url_for("users.login"))
    return render_template("login.html", form=form, error=error)

@users_blueprint.route("/logout")
@login_required
def logout():
    logout_user()
    # session.pop('logged_in', None)
    flash("You just logged out", "warning")
    referer = request.headers.get("Referer")
    return redirect(referer or url_for("show_places"))

@users_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db.session.add(user)
        db.session.commit()
        referer = request.headers.get("Referer")
        flash('Thanks for registering')
        return redirect(referer or url_for('show_places'))
    return render_template('signup.html', form=form, error=error)