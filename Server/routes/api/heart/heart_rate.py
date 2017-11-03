from datetime import date, datetime, timedelta

from flask_restful_swagger_2 import Resource, request, swagger
from flask_jwt import current_identity, jwt_required

from db.models.heart_rate import HeartRateModel
from routes.api.heart import heart_rate_doc


def daterange(d1, d2):
    return (d1 + timedelta(days=i) for i in range((d2 - d1).days + 1))


class HeartRate(Resource):
    @swagger.doc(heart_rate_doc.HEART_RATE_POST)
    @jwt_required()
    def post(self):
        rate = request.form.get('rate', type=int)
        HeartRateModel.objects(id_=str(current_identity), date=str(date.today())).delete()
        HeartRateModel(id_=str(current_identity), date=str(date.today()), rate=rate).save()

        return '', 201

    @swagger.doc(heart_rate_doc.HEART_RATE_GET)
    @jwt_required()
    def get(self):
        date_ = request.args.get('date')

        heart_rate = HeartRateModel.objects(id_=str(current_identity), date=date_)

        if not heart_rate:
            return '', 204
        else:
            return {
                'rate': heart_rate.first().rate
            }, 200


class DateRangeBasedHeartRate(Resource):
    @swagger.doc(heart_rate_doc.DATE_RANGE_BASED_HEART_RATE)
    @jwt_required()
    def get(self):
        start_date = datetime.strptime(request.args.get('start_date'), '%Y-%m-%d').date()
        end_date = datetime.strptime(request.args.get('end_date'), '%Y-%m-%d').date()

        dates = [str(d) for d in daterange(start_date, end_date)]
        heart_rates = list()
        for date_ in dates:
            print(date_)
            heart_rate = HeartRateModel.objects(id_=str(current_identity), date=date_).first()
            heart_rates.append({
                'date': heart_rate.date if heart_rate else None,
                'rate': heart_rate.rate if heart_rate else None
            })

        if not heart_rates:
            return '', 204
        else:
            return heart_rates, 200
