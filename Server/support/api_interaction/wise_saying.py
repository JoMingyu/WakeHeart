from urllib.request import urlopen
import json

from db.models.wise_saying import WiseSayingModel

_URL = 'http://esplay.xyz:21218/API/phrase/all'


def parse():
    WiseSayingModel.objects.delete()

    phrases = json.loads(json.loads(urlopen(_URL).read().decode('utf-8'))['phrase'])
    for phrase in phrases:
        WiseSayingModel(author=phrase['author'], say=phrase['say']).save()

if __name__ == '__main__':
    parse()
