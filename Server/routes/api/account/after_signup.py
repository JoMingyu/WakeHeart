from flask_restful_swagger_2 import Resource, request, swagger
from flask_jwt import current_identity, jwt_required

from db.models.user import UserModel
from routes.api.account import after_signup_doc


class ChangePW(Resource):
    @jwt_required()
    def post(self):
        pw = request.form.get('pw')

        user = UserModel.objects(id=current_identity).first()
        if not user:
            return '', 204
        else:
            user.update(pw=pw)

            return '', 201
