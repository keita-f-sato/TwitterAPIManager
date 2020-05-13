# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from twitter_test.extensions import login_manager
from twitter_test.public.forms import LoginForm
from twitter_test.user.forms import RegisterForm
from twitter_test.user.models import User
from twitter_test.utils import flash_errors
from twitter_test.accounts.models import IsAdmin
from twitter_test.accounts.models import Userque

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    admin_s = IsAdmin.query.all()
    if not admin_s:
        if form.validate_on_submit():
            User.create(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
                active=True,
                is_admin=True
            )
            IsAdmin.create(
                is_admin=True
            )
            flash("Thank you for registering. You can now log in.", "success")
            return redirect(url_for("public.home"))
        else:
            flash_errors(form)
    else:
        if form.validate_on_submit():
            Userque.create(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
                active=True
            )
            flash("Thank you for registering. You can now log in.", "success")
            return redirect(url_for("public.home"))
        else:
            flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)
