from flask import request, abort
from ..utils.response import generate_response
from ..models.beneficiary import Beneficiary
from .. import db


class BeneficiaryController:
    def get_all_beneficiaries(self):
        user_id = request.current_user.id
        beneficiaries = Beneficiary.query.filter_by(user_id=user_id).all()
        return (
            generate_response(
                data=[beneficiary.to_json() for beneficiary in beneficiaries],
                message="User Beneficiaries",
                status=200,
            ),
            200,
        )

    def create_beneficiary_r(self):
        user_id = request.current_user.id
        name = request.json.get("name")
        acc_number = request.json.get("acc_number")
        bank_code = request.json.get("bank_code")
        currency = request.json.get("currency")

        if name is None or acc_number is None or bank_code is None or currency is None:
            return abort(400)

        new_beneficiary = self.create_beneficiary(user_id, name, acc_number, bank_code)
        new_beneficiary.currency = currency
        db.session.add(new_beneficiary)
        db.session.commit()
        return (
            generate_response(
                data=new_beneficiary.to_json(),
                message="Beneficiary created",
                status=201,
            ),
            201,
        )

    def delete_beneficiary(self, id):
        beneficiary = Beneficiary.query.filter_by(id=id).first()
        if beneficiary is None:
            return abort(404)
        db.session.delete(beneficiary)
        db.session.commit()
        return generate_response(message="Beneficiary deleted", status=200), 200

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
