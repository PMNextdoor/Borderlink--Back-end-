from .. import db
import sqlalchemy as sa
from .base import BaseModel


class Beneficiary(BaseModel, db.Model):
    __tablename__ = "beneficiaries"
    name = sa.Column(sa.String(250), nullable=False)
    acc_number = sa.Column(sa.String(250), nullable=False)
    bank_code = sa.Column(sa.String(4), nullable=False)
