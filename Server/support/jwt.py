from db.models.user import UserModel


class User:
    # Document를 상속받은 User 클래스에서 id 속성을 다루면 MongoDB의 ObjectId가 들어가므로
    def __init__(self, id):
        self.id = id


def authenticate(id, pw):
    if id and pw and UserModel.objects(id=id, pw=pw):
        return User(id=id)


def identity(payload):
    return payload['identity']
