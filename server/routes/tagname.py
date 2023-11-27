from flask import Blueprint, jsonify
from ..controllers.tagname import tagname_controller


tagname_bp = Blueprint("tagname", __name__, url_prefix="/api/tagname")


@tagname_bp.route("/verify/<tagname>", strict_slashes=False)
def verify(tagname):
    if tagname_controller.verify(tagname):
        return jsonify({"message": "OK"}), 200
    return jsonify({"message": "in use"}), 400
