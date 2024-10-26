from flask import request
from flask_restful import Resource
from ..user_info import User
from ..db_fields import user_schema, users_schema
from marshmallow import ValidationError
from datetime import datetime
from mongoengine.errors import NotUniqueError, DoesNotExist

class UserListResource(Resource):
    def get(self):
        users = User.objects.all()
        return users_schema.dump(users), 200
    
    def post(self):
        try:
            data = user_schema.load(request.json)
            user = User(**data)
            user.hash_password()
            user.save()
            return user_schema.dump(user), 201
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400
        except NotUniqueError:
            return {'message': 'Email already exists'}, 409

class UserResource(Resource):
    def get(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user_schema.dump(user), 200
        except DoesNotExist:
            return {'message': 'User not found'}, 404
    
    def put(self, user_id):
        try:
            data = user_schema.load(request.json, partial=True)
            user = User.objects.get(id=user_id)
            
            for key, value in data.items():
                if key == 'password':
                    user.password = value
                    user.hash_password()
                else:
                    setattr(user, key, value)
            
            user.updated_at = datetime.utcnow()
            user.save()
            return user_schema.dump(user), 200
        except ValidationError as err:
            return {'message': 'Validation error', 'errors': err.messages}, 400
        except DoesNotExist:
            return {'message': 'User not found'}, 404
        except NotUniqueError:
            return {'message': 'Email already exists'}, 409
    
    def delete(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return '', 204
        except DoesNotExist:
            return {'message': 'User not found'}, 404