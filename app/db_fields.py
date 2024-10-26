from marshmallow import Schema, fields, validate, ValidationError

class UserFields(Schema):
    id=fields.String(dump_only=True)
    name=fields.String(required=True, validate=validate.Length(min=1))
    email=fields.Email(required=True)
    password=fields.String(required=True,load_only=True,validate=validate.Length(min=6))
    created_at=fields.DateTime(dump_only=True)
    updated_at=fields.DateTime(dump_only=True)
class AuthFields(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)

auth_schema = AuthFields()
user_schema = UserFields()
users_schema = AuthFields(many=True)