from flask import Blueprint
from ..controllers.user import user_controller
from . import auth


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/login", methods=["POST"], strict_slashes=False)
def login():
    return auth.login()


@auth_bp.route("/logout", strict_slashes=False)
def logout():
    return auth.logout()


@auth_bp.route("/register", methods=["POST"], strict_slashes=False)
def register():
    return user_controller.create_user()
