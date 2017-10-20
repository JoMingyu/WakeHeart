from db.mongo import *


class WiseSayingModel(Document):
    author = StringField(required=True)
    say = StringField(required=True)
