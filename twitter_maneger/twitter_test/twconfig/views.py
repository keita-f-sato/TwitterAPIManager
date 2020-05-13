# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request, flash
from flask_login import login_required
from twitter_test.utils import flash_errors
from twitter_test.extensions import db

from .forms import RegisterForm
from twitter_test.twitter.models import Twitter

blueprint = Blueprint("twconfig", __name__, url_prefix="/twconfig", static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def twconfig():
    """List members."""
    form = RegisterForm(request.form)
    twitter_select_id = request.args.get('twid')
    twitterinfo = Twitter.query.filter_by(twitter_id=twitter_select_id).first()

    if request.method == 'POST':
        if request.form['stat']:
            twitterinfo.is_status = True if "start" == request.form['stat'] else False
            db.session.commit()

        if form.validate_on_submit():
            twitterinfo.max_send_message = form.max_send_message.data if form.max_send_message.data else twitterinfo.max_send_message
            twitterinfo.direct_messages1 = form.direct_messages1.data if form.direct_messages1.data else twitterinfo.direct_messages1
            twitterinfo.direct_messages2 = form.direct_messages2.data if form.direct_messages2.data else twitterinfo.direct_messages2
            twitterinfo.direct_messages3 = form.direct_messages3.data if form.direct_messages3.data else twitterinfo.direct_messages3
            twitterinfo.like_keyword = form.like_keyword.data if form.like_keyword.data else twitterinfo.like_keyword
            twitterinfo.max_like = form.max_like.data if form.max_like.data else twitterinfo.max_like
            twitterinfo.follow_keyword = form.follow_keyword.data if form.follow_keyword.data else twitterinfo.follow_keyword
            twitterinfo.max_follow = form.max_follow.data if form.max_follow.data else twitterinfo.max_follow
            db.session.commit()
            flash("値を変更しました!")
        else:
            flash_errors(form)
    return render_template(
        "twitter/twitter-setting.html",
        form=form,
        status=twitterinfo.is_status,
        twid=twitter_select_id,
        max_send_message=twitterinfo.max_send_message,
        direct_messages1=twitterinfo.direct_messages1,
        direct_messages2=twitterinfo.direct_messages2,
        direct_messages3=twitterinfo.direct_messages3,
        like_keyword=twitterinfo.like_keyword,
        max_like=twitterinfo.max_like,
        follow_keyword=twitterinfo.follow_keyword,
        max_follow=twitterinfo.max_follow
    )
