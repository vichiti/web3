from flask import Flask
from app.config import Config
from app.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize database
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Create tables if they don’t exist

    # Register blueprints
    from app.home.routes import home_bp
    from app.hedera.routes import hedera_bp
    from app.auth.routes import auth_bp
    app.register_blueprint(home_bp)
    # app.register_blueprint(hedera_bp, url_prefix='/hedera')
    # app.register_blueprint(auth_bp, url_prefix='/auth')

    return app