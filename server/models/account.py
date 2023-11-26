from .. import db
import sqlalchemy as sa
from .base import BaseModel


class Account(BaseModel, db.Model):
    __tablename__ = "accounts"
    user_id = sa.Column(sa.String(250), sa.ForeignKey("users.id"), nullable=False)
    currency = sa.Column(sa.String(3), nullable=False)
    balance = sa.Column(sa.DECIMAL(precision=12, scale=2), default=0.00)
    acc_number = sa.Column(sa.String(250), nullable=False)
    bank_code = sa.Column(sa.String(4), nullable=False)
