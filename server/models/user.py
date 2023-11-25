from .. import db
import sqlalchemy as sa
from .base import BaseModel


class User(BaseModel, db.Model):
    __tablename__ = "users"
    fname = sa.Column(sa.String(250), nullable=False)
    mname = sa.Column(sa.String(250))
    lname = sa.Column(sa.String(250), nullable=False)
    password = sa.Column(sa.String(250), nullable=False)
    email = sa.Column(sa.String(250), nullable=False, unique=True)
    tagname = sa.Column(sa.String(250), unique=True)
    acc_balance = sa.Column(sa.DOUBLE_PRECISION(), default=0)
    default_currency = sa.Column(sa.String(3))

    def __repr__(self) -> str:
        return f"<User {self.acc_balance} {self.default_currency} {self.fname} {self.lname}>"
