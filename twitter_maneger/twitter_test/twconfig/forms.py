# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import Length, NumberRange


class RegisterForm(FlaskForm):
    """Register form."""

    max_send_message = IntegerField(
        "maxSendMessage", validators=[NumberRange(min=0, max=10)]
    )
    direct_messages1 = StringField(
        "directMessages1", validators=[Length(min=0, max=144)]
    )
    direct_messages2 = StringField(
        "directMessages2", validators=[Length(min=0, max=144)]
    )
    direct_messages3 = StringField(
        "directMessages3", validators=[Length(min=0, max=144)]
    )
    like_keyword = StringField(
        "likeKeyword", validators=[Length(min=0, max=144)]
    )
    max_like = IntegerField(
        "maxLike", validators=[NumberRange(min=0, max=10)]
    )
    follow_keyword = StringField(
        "followKeyword", validators=[Length(min=0, max=144)]
    )
    max_follow = IntegerField(
        "maxFollow", validators=[NumberRange(min=0, max=10)]
    )

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.twitter = None

    def validate(self):
        """Validate the form."""

        return True
