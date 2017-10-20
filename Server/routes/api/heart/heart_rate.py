from datetime import date, timedelta

from flask_restful_swagger_2 import Resource, request, swagger
from flask_jwt import current_identity, jwt_required

from db.models.heart_rate import HeartRateModel


def daterange(d1, d2):
    return (d1 + timedelta(days=i) for i in range((d2 - d1).days + 1))


class HeartRate(Resource):
    @jwt_required()
    def post(self):
        rate = request.form.get('rate', type=int)

        HeartRateModel.objects(id=current_identity, date=str(date.today())).first().delete()
        HeartRateModel(id=current_identity, rate=rate).save()

        return '', 201

    @jwt_required()
    def get(self):
        date_ = request.args.get('date')

        heart_rate = HeartRateModel.objects(id=current_identity, date=date_).first()

        if not heart_rate:
            return '', 204
        else:
            return {
                'rate': heart_rate.rate
            }, 200


class DateRangeBasedHeartRate(Resource):
    @jwt_required()
    def get(self):
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')

        dates = [str(d) for d in daterange(start_date, end_date)]
        heart_rates = list()
        for date_ in dates:
            heart_rate = HeartRateModel.objects(id=current_identity, date=date_).first()
            heart_rates.append({
                'date': heart_rate.date,
                'rate': heart_rate.rate
            })

        if not heart_rates:
            return '', 204
        else:
            return heart_rates, 200
