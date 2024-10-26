from flask import jsonify
from mongoengine.errors import ValidationError as MongoValidationError
from marshmallow import ValidationError as MarshmallowValidationError
from flask_jwt_extended.exceptions import JWTExtendedException
from jwt.exceptions import PyJWTError

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': 'Resource not found'}), 404
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'message': 'Bad request'}), 400
    
    @app.errorhandler(MongoValidationError)
    def handle_mongo_validation_error(error):
        return jsonify({'message': 'Validation error', 'errors': str(error)}), 400
    
    @app.errorhandler(MarshmallowValidationError)
    def handle_marshmallow_validation_error(error):
        return jsonify({'message': 'Validation error', 'errors': error.messages}), 400
    
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        return jsonify({'message': 'Internal server error'}), 500
    @app.errorhandler(JWTExtendedException)
    def handle_jwt_extended_error(error):
        return jsonify({'message': 'JWT token error'}), 401
    
    @app.errorhandler(PyJWTError)
    def handle_jwt_error(error):
        return jsonify({'message': 'JWT token error'}), 401