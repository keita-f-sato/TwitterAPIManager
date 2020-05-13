# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

from twitter_test.twitter.models import Twitter

blueprint = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@blueprint.route("/")
@login_required
def members():
    """List members."""
    twitterids = Twitter.query.all()

    return render_template(
        "users/members.html",
        twitterids=[t.twitter_id for t in twitterids],
        twitter_inf=zip([t.is_status for t in twitterids], [i.twitter_id for i in twitterids])
    )
