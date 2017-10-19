from db.mongo import *


class UserModel(Document):
    id = StringField(primary_key=True)
    pw = StringField(required=True)
    sex = StringField(required=True)
    age = IntField(required=True)
