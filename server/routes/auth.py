from flask import Blueprint
from ..controllers.auth import Auth
from ..controllers.user import UserController

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")
auth = Auth()
user_controller = UserController()


@auth_bp.route("/login", strict_slashes=False)
def login():
    return auth.login()


@auth_bp.route("/logout", strict_slashes=False)
def logout():
    return auth.logout()


@auth_bp.route("/register", strict_slashes=False)
def register():
    return user_controller.create_user()
