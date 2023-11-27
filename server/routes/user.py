from flask import Blueprint, request
from ..utils.response import generate_response
from ..controllers.auth import auth_controller
from ..controllers.user import user_controller


user_bp = Blueprint("user", __name__, url_prefix="/api/users")


@user_bp.route("/me", strict_slashes=False)
@auth_controller.login_required
def me():
    user_id = request.current_user.id
    user = user_controller.get_by_id(user_id)
    return (
        generate_response(data=user.to_json(), message="User details", status=200),
        200,
    )
