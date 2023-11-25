from flask import request, url_for, abort
import bcrypt
from .. import db
from ..models.user import User
from ..utils.response import generate_response


class UserController:
    def get_by_id(self, id):
        return User.query.filter_by(id=id).first()

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_by_tagname(self, tagname):
        return User.query.filter_by(tagname=tagname)

    def create_user(self):
        email = request.json.get("email")
        fname = request.json.get("fname")
        mname = request.json.get("mname")
        lname = request.json.get("lname")
        password = request.json.get("password")
        if email is None or fname is None or lname is None or password is None:
            return abort(400)
        new_user = {
            "email": email,
            "fname": fname,
            "mname": mname,
            "lname": lname,
            "password": bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8"),
        }
        new_user = User(**new_user)
        db.session.add(new_user)
        db.session.commit()
        return (
            generate_response(
                data={"id": new_user.id, "login": url_for("auth.login")},
                message="User created",
                status=201,
            ),
            201,
        )


user_controller = UserController()
