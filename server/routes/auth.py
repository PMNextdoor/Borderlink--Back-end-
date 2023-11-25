from flask import Blueprint
from ..controllers.user import user_controller
from ..controllers.auth import auth_controller


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/login", methods=["POST"], strict_slashes=False)
def login():
    return auth_controller.login()


@auth_bp.route("/logout", strict_slashes=False)
def logout():
    return auth_controller.logout()


@auth_bp.route("/register", methods=["POST"], strict_slashes=False)
def register():
    return user_controller.create_user()
