from marshmallow import Schema
from marshmallow.fields import String, Integer


class UserSchema(Schema):
    id = Integer()
    name = String()
    age = Integer()
