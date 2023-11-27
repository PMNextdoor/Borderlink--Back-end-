from flask import Blueprint
from ..controllers.beneficiary import beneficiary_controller
from ..controllers.auth import auth_controller


beneficiary_bp = Blueprint("beneficiary", __name__, url_prefix="/api/beneficiaries")


@beneficiary_bp.route("/", methods=["POST"], strict_slashes=False)
@auth_controller.login_required
def create_beneficiaries():
    return beneficiary_controller.create_beneficiary_r()


@beneficiary_bp.route("/", strict_slashes=False)
@auth_controller.login_required
def get_beneficiaries():
    return beneficiary_controller.get_all_beneficiaries()


@beneficiary_bp.route("/<id>", methods=["POST"], strict_slashes=False)
@auth_controller.login_required
def delete(id):
    return beneficiary_controller.delete_beneficiary(id)
