from flask_restful_swagger_2 import Resource, request, swagger

from db.models.wise_saying import WiseSayingModel
from routes.api.wise_saying import wise_saying_doc


class WiseSaying(Resource):
    @swagger.doc(wise_saying_doc.WISE_SAYING)
    def get(self):
        return [{
            'author': wise_saying.author,
            'say': wise_saying.say
        } for wise_saying in WiseSayingModel.objects], 200
