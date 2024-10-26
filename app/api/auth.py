from flask import request
from flask_restful import Resource
from flask_jwt_extended import (create_access_token,create_refresh_token,get_jwt_identity,jwt_required)
from ..user_info import User
from ..db_fields import auth_schema
from marshmallow import ValidationError

class LoginResource(Resource):
    def post(self):
        try:
            data = auth_schema.load(request.json)
            user = User.objects.get(email=data['email'])
            
            if user.check_password(data['password']):
                access_token = create_access_token(identity=str(user.id))
                refresh_token = create_refresh_token(identity=str(user.id))
                
                return {'access_token': access_token,'refresh_token': refresh_token,'user_id': str(user.id)},200
                    
                    
                    
                
            else:
                return {'message': 'Invalid credentials'}, 401
                
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400
        except User.DoesNotExist:
            return {'message': 'Invalid credentials'}, 401

class RefreshTokenResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user_id = get_jwt_identity()
        access_token = create_access_token(identity=current_user_id)
        
        return {'access_token': access_token}, 200