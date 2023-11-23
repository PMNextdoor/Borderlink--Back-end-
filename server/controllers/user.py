from flask import request, url_for
import bcrypt
from .. import db
from ..models.user import User
from ..utils.response import generate_response


class UserController:
    def get_by_id(self, id):
        return db.Query(User).filter_by(id=id).first()

    def get_by_email(self, email):
        return db.Query(User).filter_by(email=email).first()

    def get_by_tagname(self, tagname):
        return db.Query(User).filter_by(tagname=tagname)

    def create_user(self):
        newUser = {
            "email": request.json.get("email"),
            "fname": request.json.get("fname"),
            "mname": request.json.get("mname"),
            "lname": request.json.get("lname"),
            "password": bcrypt.hashpw(
                request.json.get("password").encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8"),
        }
        newUser = User(**newUser)
        db.session.add(newUser)
        db.session.commit()
        return (
            generate_response(
                data={"id": newUser.id, "login": url_for("auth.login")},
                message="User created",
                status=201,
            ),
            201,
        )
