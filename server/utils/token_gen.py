from datetime import datetime, timedelta, timezone
import os
import jwt
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class TokenGenerator:
    @staticmethod
    def encode_token(user):
        """
        The encode_token function takes in a user object and returns a token

        :param user: The user object that we want to encode
        :return: A token
        """

        payload = {
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "id": str(user.id),
        }
        token = jwt.encode(payload, os.environ.get("SECRET_KEY"), algorithm="HS256")
        return token

    @staticmethod
    def decode_token(token):
        """
        It takes a token, decodes it, and returns the decoded token

        :param token: The token to decode
        :return: A dictionary with the user's id and username.
        """
        return jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )

    @staticmethod
    def check_token(token):
        """
        It takes a token, and returns True if the token is valid, and False if it's not

        :param token: The token to be decoded
        :return: A boolean value.
        """
        try:
            jwt.decode(
                token,
                os.environ.get("SECRET_KEY"),
                algorithms="HS256",
                options={"require_exp": True},
            )
            return True
        except:
            return False

    @staticmethod
    def get_user_id(token):
        """
        It decodes the token, and returns the user's id

        :param token: The token that was sent to the server
        :return: The user id is being returned.
        """
        data = jwt.decode(
            token,
            os.environ.get("SECRET_KEY"),
            algorithms="HS256",
            options={"require_exp": True},
        )
        return data["id"]


token_generator = TokenGenerator()
