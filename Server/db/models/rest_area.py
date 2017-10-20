from db.mongo import *


class RestAreaModel(Document):
    code = IntField(primary_key=True)
    name = StringField(required=True)
    route_name = StringField(required=True)
    x = FloatField()
    y = FloatField()
