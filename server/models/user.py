from .. import db
import sqlalchemy as sa
from sqlalchemy.orm import relationship
from .base import BaseModel
from .account import Account
from .beneficiary import Beneficiary
from .transaction import Transaction


class User(BaseModel, db.Model):
    __tablename__ = "users"
    fname = sa.Column(sa.String(250), nullable=False)
    mname = sa.Column(sa.String(250))
    lname = sa.Column(sa.String(250), nullable=False)
    password = sa.Column(sa.String(250), nullable=False)
    email = sa.Column(sa.String(250), nullable=False, unique=True)
    tagname = sa.Column(sa.String(250), unique=True)
    default_currency = sa.Column(sa.String(3), default="NGN")
    beneficiaries = relationship("Beneficiary", backref="user")
    accounts = relationship("Account", backref="user")
    transactions = relationship("Transaction", backref="user")

    def __repr__(self) -> str:
        return f"<User {self.acc_balance} {self.default_currency} {self.fname} {self.lname}>"
