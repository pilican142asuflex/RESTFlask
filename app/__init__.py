from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .jwt_mongo_config import Config
from .db_initialise import db  # Importing from extensions.py
from .api.users import UserResource, UserListResource
from .api.auth import LoginResource, RefreshTokenResource
from .utils.error_handlers import register_error_handlers

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_object(Config)
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    
    # Initialize API
    api = Api(app)
    
    # Register resources
    api.add_resource(UserListResource, '/users')
    api.add_resource(UserResource, '/users/<string:user_id>')
    api.add_resource(LoginResource, '/auth/login')
    api.add_resource(RefreshTokenResource, '/auth/refresh')
    
    # Register error handlers
    register_error_handlers(app)
    
    return app