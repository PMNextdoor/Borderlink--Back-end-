""" Utils Function """
from flask import jsonify
from .http_code import HTTP_200_OK, HTTP_201_CREATED


def generate_response(data=None, message=None, status=400):
    """
    It takes in a data, message, and status, and returns a dictionary with the data, message, and status

    :param data: The data that you want to send back to the client
    :param message: This is the message that you want to display to the user
    :param status: The HTTP status code, defaults to 400 (optional)
    :return: A dictionary with the keys: data, message, status.
    """
    if status in [HTTP_200_OK, HTTP_201_CREATED]:
        status_bool = True
    else:
        status_bool = False

    return jsonify(
        {
            "data": data,
            "message": message,
            "status": status_bool,
        }
    )
