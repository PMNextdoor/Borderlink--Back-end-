from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .configs.config import Config

# from .routes.user import user_bp

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)
    migrate.init_app(app, db)

    # import models
    from .models.user import User
    from .models.transaction import Transaction
    from .models.beneficiary import Beneficiary

    with app.app_context():
        db.create_all()
    from .routes.auth import auth_bp
    from .routes.transaction import transaction_bp

    # import blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(transaction_bp)
    # app.register_blueprint(user_bp)
    return app


app = create_app()


@app.route("/")
def index():
    return {"message": "Hello world"}


from .configs.flask_app import *
