"""
This is where we define URLs (routes)
"""
# pylint: disable=cyclic-import
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from znd4.models import User
from znd4 import app


@app.route("/")
@app.route("/index")
def index():
    """The homepage"""
    return render_template("index.html", title="Home")


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
        return redirect(url_for("login"))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user
    return redirect(url_for())


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
