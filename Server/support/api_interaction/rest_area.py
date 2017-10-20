from urllib.request import urlopen
import json

from db.models.rest_area import RestAreaModel

_URL = 'http://esplay.xyz:21218/API/rest/all'


def parse():
    RestAreaModel.objects.delete()

    areas = json.loads(json.loads(urlopen(_URL).read().decode('utf-8'))['list'])['list']
    for area in areas:
        RestAreaModel(code=area['unitCode'], name=area['unitName'], route_name=area['routeName'], x=area['xValue'], y=area['yValue']).save()

if __name__ == '__main__':
    parse()
