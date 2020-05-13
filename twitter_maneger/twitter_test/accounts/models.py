import datetime as dt

from flask_login import UserMixin

from twitter_test.database import (
    Column,
    Model,
    SurrogatePK,
    db
)
from twitter_test.extensions import bcrypt


class IsAdmin(SurrogatePK, Model):

    __tablename__ = "IsAdmin"
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, is_admin, **kwargs):
        """Create instance."""
        db.Model.__init__(self, is_admin=is_admin, **kwargs)

class Userque(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = "userque"
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(30), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        self.password = password
        # if password:
        #     self.set_password(password)
        # else:
        #     self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    @property
    def full_name(self):
        """Full user name."""
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<User({self.username!r})>"
