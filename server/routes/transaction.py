from flask import Blueprint
from ..controllers.transaction import transaction_controller
from . import auth


transaction_bp = Blueprint("transaction", __name__, url_prefix="/api/tnx")


# /pay
@transaction_bp.route("/pay", methods=["POST"], strict_slashes=False)
@auth.login_required
def create_payment_link():
    return transaction_controller.create_payment_link()


# /payment-webhook
# /transfer
