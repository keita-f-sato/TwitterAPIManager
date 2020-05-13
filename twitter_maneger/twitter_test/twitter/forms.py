# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length

from .models import Twitter


class RegisterForm(FlaskForm):
    """Register form."""

    twitter_id = StringField(
        "twitterId", validators=[DataRequired(), Length(min=3, max=25)]
    )
    ck = PasswordField(
        "consumerKey", validators=[DataRequired(), Length(min=6, max=40)]
    )
    csk = PasswordField(
        "consumerSecretKey", validators=[DataRequired(), Length(min=6, max=40)]
    )
    at = PasswordField(
        "accessToken", validators=[DataRequired(), Length(min=6, max=40)]
    )
    ast = PasswordField(
        "secretAccessToken", validators=[DataRequired(), Length(min=6, max=40)]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.twitter = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate()
        if not initial_validation:
            return False
        twitter = Twitter.query.filter_by(twitter_id=self.twitter_id.data).first()
        if twitter:
            self.twitter_id.errors.append("TwitterId already registered")
            return False
        return True
