from flask import request
from ..utils.response import generate_response
from ..models.beneficiary import Beneficiary
from .. import db


class BeneficiaryController:
    def get_beneficiary(self, acc_number, bank_code, user_id):
        beneficiary = Beneficiary.query.filter_by(
            user_id=user_id, acc_number=acc_number, bank_code=bank_code
        ).first()
        return beneficiary

    def create_beneficiary(self, user_id, name, acc_number, bank_code):
        beneficiary = self.get_beneficiary(acc_number, bank_code, user_id)
        if beneficiary is not None:
            return beneficiary
        beneficiary = Beneficiary()
        beneficiary.name = name
        beneficiary.acc_number = acc_number
        beneficiary.bank_code = bank_code
        beneficiary.user_id = user_id

        db.session.add(beneficiary)
        db.session.commit()
        return beneficiary


beneficiary_controller = BeneficiaryController()
