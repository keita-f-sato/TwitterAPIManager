# -*- coding: utf-8 -*-
"""User models."""

from twitter_test.database import (
    Column,
    Model,
    SurrogatePK,
    db
)
from twitter_test.extensions import bcrypt

class Twitter(SurrogatePK, Model):
    """A Twitter of the app."""

    __tablename__ = "TwitterInfos"
    twitter_id = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    consumer_key = Column(db.String(80), unique=True, nullable=False)
    consumer_secret_key = Column(db.String(80), unique=True, nullable=False)
    access_token = Column(db.String(80), unique=True, nullable=False)
    secret_access_token = Column(db.String(80), unique=True, nullable=False)
    max_send_message = Column(db.Integer(), nullable=True)
    direct_messages1 = Column(db.String(length=144), nullable=True)
    direct_messages2 = Column(db.String(length=144), nullable=True)
    direct_messages3 = Column(db.String(length=144), nullable=True)
    like_keyword = Column(db.String(length=144), nullable=True)
    like_interval = Column(db.Integer(), nullable=True)
    max_like = Column(db.Integer(), nullable=True)
    follow_keyword = Column(db.String(length=144), nullable=True)
    follow_interval = Column(db.Integer(), nullable=True)
    max_follow = Column(db.Integer(), nullable=True)
    is_status = Column(db.Boolean(), default=False)

    def __init__(self, twitter_id, consumer_key, consumer_secret_key, access_token, secret_access_token, **kwargs):
        """Create instance."""
        db.Model.__init__(self, twitter_id=twitter_id, **kwargs)
        self.consumer_key = bcrypt.generate_password_hash(consumer_key)
        self.consumer_secret_key = bcrypt.generate_password_hash(consumer_secret_key)
        self.access_token = bcrypt.generate_password_hash(access_token)
        self.secret_access_token = bcrypt.generate_password_hash(secret_access_token)

    def check_password(self, crypt, value):
        """Check password."""
        return bcrypt.check_password_hash(crypt, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"
