from flask_restful_swagger_2 import Resource, request, swagger
from db.models.user import UserModel


class Signup(Resource):
    def post(self):
        id = request.form.get('id')
        pw = request.form.get('pw')
        sex = request.form.get('sex')
        age = request.form.get('age', type=int)

        if UserModel.objects(id=id):
            return '', 204
        else:
            UserModel(id=id, pw=pw, sex=sex, age=age).save()

            return '', 201
