from .. import db
import sqlalchemy as sa
from .base import BaseModel


class Transaction(BaseModel, db.Model):
    __tablename__ = "transactions"
    txn_type = sa.Column(sa.String(10), nullable=False)
    txn_time = sa.Column(sa.DateTime)
    txn_ref = sa.Column(sa.String)
    description = sa.Column(sa.String)
    txn_status = sa.Column(sa.String, default="pending")
    amount = sa.Column(sa.DECIMAL(precision=12, scale=2), nullable=False)
    currency_from = sa.Column(sa.String)
    currency_to = sa.Column(sa.String)
    rate = sa.Column(sa.Float, default=1)
    from_acc = sa.Column(sa.String(250), sa.ForeignKey("accounts.id"))
    to_acc = sa.Column(sa.String(250), sa.ForeignKey("accounts.id"))
    credited = sa.Column(sa.String(1), default="N")
    action = sa.Column(sa.String, nullable=False)
    user_id = sa.Column(sa.String(250), sa.ForeignKey("users.id"), nullable=False)
