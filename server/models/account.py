from .. import db
import sqlalchemy as sa
from .base import BaseModel
from .user import User


class Account(BaseModel, db.Model):
    pass
