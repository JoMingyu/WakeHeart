from flask_restful_swagger_2 import Resource, request, swagger
from flask_jwt import current_identity, jwt_required

from db.models.user import UserModel
from routes.api.account import after_signup_doc


class ChangePW(Resource):
    @swagger.doc(after_signup_doc.CHANGE_PW)
    @jwt_required()
    def post(self):
        pw = request.form.get('pw')

        UserModel.objects(id=str(current_identity)).first().update(pw=pw)

        return '', 201


class ChangeInfo(Resource):
    @swagger.doc(after_signup_doc.CHANGE_INFO)
    @jwt_required()
    def post(self):
        position = request.form.get('position', type=int)
        sex = request.form.get('sex')
        age = request.form.get('age', type=int)

        UserModel.objects(id=str(current_identity)).first().update(position=position, sex=sex, age=age)

        return '', 201
