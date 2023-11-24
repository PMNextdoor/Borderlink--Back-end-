from .. import db
import sqlalchemy as sa
from .base import BaseModel


class Transaction(BaseModel, db.Model):
    txn_type = sa.Column(sa.String(10), nullable=False)
    txn_time = sa.Column(sa.DateTime)
    ref_id = sa.Column(sa.String)
    txn_status = sa.Column(sa.String)
    amount = sa.Column(sa.DOUBLE_PRECISION, nullable=False)
