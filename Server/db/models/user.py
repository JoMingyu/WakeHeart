from db.mongo import *


class UserModel(Document):
    id = StringField(primary_key=True)
    pw = StringField(required=True)
    position = IntField(required=True, default=2)
    sex = StringField(required=True)
    age = IntField(required=True)
