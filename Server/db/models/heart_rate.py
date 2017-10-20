from datetime import date

from db.mongo import *


class HeartRateModel(Document):
    id = StringField(required=True)
    date = StringField(required=True, default=str(date.today()))
    rate = IntField(required=True, min_value=0)
