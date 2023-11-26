from ..utils.response import generate_response
from ..models.account import Account
from .. import db
from ..controllers.user import user_controller


class AccountController:
    def get_account_by_id(self, account_id):
        account = Account.query.filter_by(id=account_id).first()
        return account

    def get_account_by_currency(self, user_id, currency):
        account = Account.query.filter_by(user_id=user_id, currency=currency).first()
        return account

    def get_account_by_acc_number(self, acc_number, bank_code):
        account = Account.query.filter_by(
            acc_number=acc_number, bank_code=bank_code
        ).first()
        return account

    def create_account(self, user_id, currency):
        account = Account()
        account.currency = currency
        account.user_id = user_id
        account.acc_number = user_controller.get_by_id(user_id).tagname
        db.session.add(account)
        db.session.commit()
        return account

    def credit_account(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        account.balance += amount
        db.session.add(account)
        db.session.commit()
        return True

    def debit_account(self, account_id, amount):
        account = self.get_account_by_id(account_id)
        if account.balance < amount:
            return False
        account.balance -= amount
        db.session.add(account)
        db.session.commit()
        return True


account_controller = AccountController()
