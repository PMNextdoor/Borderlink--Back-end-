from flask import Blueprint
from ..controllers.transaction import transaction_controller
from ..controllers.auth import auth_controller


transaction_bp = Blueprint("transaction", __name__, url_prefix="/api/txn")


# /pay
@transaction_bp.route("/fund-wallet", methods=["POST"], strict_slashes=False)
@auth_controller.login_required
def create_payment_link():
    return transaction_controller.fund_wallet()


# /payment-webhook
@transaction_bp.route("/webhook", methods=["POST"], strict_slashes=False)
def payment_webhook():
    return transaction_controller.webhook()


# /transfer
@transaction_bp.route("/payuser", methods=["POST"], strict_slashes=False)
@auth_controller.login_required
def pay_user():
    return transaction_controller.pay_app_user()
