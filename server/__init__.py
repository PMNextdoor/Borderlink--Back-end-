from os import getenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .configs.config import Config
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    cors = CORS(app, supports_credentials=True)
    app.config.from_object(Config())

    db.init_app(app)
    migrate.init_app(app, db)

    # import models
    from .models.user import User
    from .models.transaction import Transaction
    from .models.beneficiary import Beneficiary
    from .models.account import Account

    with app.app_context():
        db.create_all()
    # import blueprints
    from .routes.auth import auth_bp
    from .routes.transaction import transaction_bp
    from .routes.beneficiary import beneficiary_bp
    from .routes.user import user_bp
    from .routes.tagname import tagname_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(beneficiary_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(tagname_bp)
    return app


app = create_app()


@app.route("/")
def index():
    return {"message": "Hello world"}


from .configs.flask_app import *
