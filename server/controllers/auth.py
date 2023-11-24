from functools import wraps
import bcrypt
from flask import request, abort
import jwt
from ..utils.token_gen import token_generator
from ..utils.response import generate_response
from ..utils.http_header import AUTH_TOKEN_HEADER
from .user import UserController


class Auth:
    user_controller = UserController()

    def login_required(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.cookies.get(AUTH_TOKEN_HEADER)
            if not token:
                return abort(401)
            try:
                token_generator.decode_token(token)
                request.current_user = self.current_user()
                if request.current_user is None:
                    return abort(403)
            except jwt.ExpiredSignatureError:
                return abort(403)
            except jwt.InvalidTokenError:
                return abort(403)
            return func(*args, **kwargs)

        return wrapper

    def login(self):
        email = request.json.get("email")
        password = request.json.get("password")
        if email is None or password is None:
            return abort(400)
        user = self.user_controller.get_by_email(email)
        if user is None or not bcrypt.checkpw(
            password.encode("utf-8"), user.password.encode("utf-8")
        ):
            return (
                generate_response(message="Username or Password incorrect", status=403),
                403,
            )
        token = token_generator.encode_token(user)
        res = generate_response(message="Login success", status=200)
        res.set_cookie(AUTH_TOKEN_HEADER, token, secure=True, httponly=True)
        return res, 200

    def current_user(self):
        token = request.cookies.get(AUTH_TOKEN_HEADER)
        if token_generator.check_token(token):
            user_id = token_generator.get_user_id(token)
            return self.user_controller.get_by_id(user_id)

    def logout(self):
        response = generate_response(message="Logout Success", status=200)
        response.delete_cookie(AUTH_TOKEN_HEADER, secure=True, httponly=True)
        return response
