"""
This is where we define URLs (routes)
"""
# pylint: disable=cyclic-import
from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from znd4.models import User
from znd4.forms import LoginForm, RegistrationForm
from znd4 import app, db


@app.route("/")
@app.route("/index")
@login_required
def index():
    """The homepage"""
    posts = [{"author": {"username": "znd4"}, "body": "Gawsh, I love movies!!!"}]
    return render_template("index.html", title="Home", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    """The route/business logic for our registration page."""
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if not form.validate_on_submit():
        return render_template("register.html", title="Register", form=form)

    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("Welcome to the website!")
    return redirect(url_for("index"))


@app.route("/resume")
def resume():
    """The link to my resume"""
    return render_template("resume.html", title="Resume")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle log-ins due to"""
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/blog")
def blog():
    """The splash page for my blog"""
    posts = [
        {
            "title": "Beautiful, Awesome Animals",
            "content": "A tale of cute, furry doggos.",
        },
        {
            "title": "Making Games Matter",
            "content": "How we make a website with real blog posts",
        },
    ]
    return render_template("blog.html", title="Blog", posts=posts)
