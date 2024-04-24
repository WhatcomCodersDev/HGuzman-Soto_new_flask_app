from flask import Flask
from .config import Config
from app.routes import main_routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(main_routes.bp)

    return app
