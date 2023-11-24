from .. import db, app
from ..utils.response import generate_response


@app.teardown_appcontext
def close(exception=None):
    db.session.close()


@app.errorhandler(400)
def bad_request(e):
    return generate_response(message="Bad request", status=400), 400


@app.errorhandler(401)
def unauthorized(e):
    return generate_response(message="Unauthorized", status=401), 401


@app.errorhandler(403)
def forbidden(e):
    return generate_response(message="Forbidden", status=403), 403


@app.errorhandler(404)
def not_found(e):
    return generate_response(message="Resource Not Found", status=404), 404


@app.errorhandler(500)
def internal_error(e):
    return generate_response(message="Internal Server Error", status=500), 500
