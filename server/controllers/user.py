from flask import request, url_for, abort
import bcrypt
from .. import db
from ..models.user import User
from ..models.account import Account
from ..utils.response import generate_response


class UserController:
    def get_by_id(self, id: str) -> User:
        return User.query.filter_by(id=id).first()

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def get_by_tagname(self, tagname):
        return User.query.filter_by(tagname=tagname).first()

    def create_user(self):
        email = request.json.get("email")
        fname = request.json.get("fname")
        mname = request.json.get("mname")
        lname = request.json.get("lname")
        password = request.json.get("password")
        tagname = request.json.get("tagname")

        if (
            email is None
            or fname is None
            or lname is None
            or password is None
            or tagname is None
        ):
            return abort(400)

        new_user = {
            "email": email,
            "fname": fname,
            "mname": mname,
            "lname": lname,
            "tagname": tagname,
            "password": bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8"),
        }
        new_user = User(**new_user)
        db.session.add(new_user)
        db.session.commit()

        # create account
        account = Account()
        account.currency = new_user.default_currency
        account.user_id = new_user.id
        account.acc_number = tagname
        account.bank_code = "BDL"
        db.session.add(account)
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
