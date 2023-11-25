from .. import db
import sqlalchemy as sa
from .base import BaseModel
from .user import User


class Transaction(BaseModel, db.Model):
    txn_type = sa.Column(sa.String(10), nullable=False)
    txn_time = sa.Column(sa.DateTime)
    txn_ref = sa.Column(sa.String)
    description = sa.Column(sa.String)
    txn_status = sa.Column(sa.String, default="pending")
    amount = sa.Column(sa.DOUBLE_PRECISION, nullable=False)
    currency_from = sa.Column(sa.String)
    currency_to = sa.Column(sa.String)
    from_user = sa.Column(sa.String(250), sa.ForeignKey("users.id"))
    to_user = sa.Column(sa.String(250), sa.ForeignKey("beneficiaries.id"))
