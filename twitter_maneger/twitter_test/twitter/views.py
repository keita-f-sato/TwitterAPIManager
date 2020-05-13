# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
from flask_login import login_required
from twitter_test.utils import flash_errors

from .forms import RegisterForm
from .models import Twitter

blueprint = Blueprint("twitter", __name__, url_prefix="/twitter", static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def twiiter():
    """List members."""
    twitter_infos = Twitter.query.all()
    twitter_status = [t.is_status for t in twitter_infos]
    twitter_ids = [i.twitter_id for i in twitter_infos]

    form = RegisterForm(request.form)
    if form.validate_on_submit():
        Twitter.create(
            twitter_id=form.twitter_id.data,
            consumer_key=form.ck.data,
            consumer_secret_key=form.csk.data,
            access_token=form.at.data,
            secret_access_token=form.ast.data,
        )
        return render_template(
            "users/members.html",
            twitterids=[t.twitter_id for t in twitter_infos],
            twitter_inf=zip(twitter_status, twitter_ids)
        )
    else:
        flash_errors(form)

    return render_template("twitter/twitter.html", form=form)
