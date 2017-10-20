from flask_restful_swagger_2 import Resource, swagger

from db.models.rest_area import RestAreaModel
from routes.api.rest_area import rest_area_doc


class RestArea(Resource):
    @swagger.doc(rest_area_doc.REST_AREA)
    def get(self):
        return [{
            'code': rest_area.code,
            'name': rest_area.name,
            'route_name': rest_area.route_name,
            'x': rest_area.x,
            'y': rest_area.y
        } for rest_area in RestAreaModel.objects], 200
