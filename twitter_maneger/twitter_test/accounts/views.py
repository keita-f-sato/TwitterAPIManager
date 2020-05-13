# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from twitter_test.utils import flash_errors
from .forms import RegisterForm
from twitter_test.user.models import User
from .models import Userque
from wtforms import BooleanField


blueprint = Blueprint("account", __name__, url_prefix="/account", static_folder="../static")


@blueprint.route("/", methods=["GET", "POST"])
@login_required
def account():
    """List members."""
    user_info = User.query.filter_by(username=current_user.username).first()

    if user_info.is_admin:
        user_que = Userque.query.all()

        for one_user in user_que:
            setattr(RegisterForm, one_user.username,
                    BooleanField("許可", default=False))

        form = RegisterForm(request.form)

        for one_user in user_que:
            if form.__dict__[one_user.username].data:
                if form.validate_on_submit():
                    uniq_user_data = Userque.query.filter_by(username=one_user.username).first()
                    User.create(
                        username=uniq_user_data.username,
                        email=uniq_user_data.email,
                        password=uniq_user_data.password,
                        active=True
                    )
                    Userque.delete(uniq_user_data)
                else:
                    flash_errors(form)

        que = zip([i.username for i in user_que], [i.email for i in user_que])

        return render_template(
            "users/account.html",
            form=form,
            que=que,
            isadmin=user_info.is_admin
        )
    else:
        form = RegisterForm(request.form)
        return render_template(
            "users/account.html",
            form=form,
            quename=["a"],
            queemail=["b"],
            isadmin=user_info.is_admin
        )
