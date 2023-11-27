from flask import Blueprint, request
from ..controllers.account import account_controller
from ..controllers.auth import auth_controller
from ..utils.response import generate_response


account_bp = Blueprint("account", __name__, url_prefix="/api/accounts")


@account_bp.route("/", strict_slashes=False)
@auth_controller.login_required
def accounts():
    accounts = account_controller.get_user_accounts()
    return generate_response(data=accounts, message="User accounts", status=200), 200


@account_bp.route("/", methods=["POST"], strict_slashes=False)
def create_account():
    user_id = request.current_user.id
    currency = request.json.get("currency")
    account = account_controller.create_account(user_id, currency)
    return (
        generate_response(
            data=account.to_json(), message="Account Created", status=201
        ),
        201,
    )
