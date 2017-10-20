REST_AREA = {
    'tags': ['휴게소'],
    'description': '휴게소 리스트 조회',
    'responses': {
        '200': {
            'description': '휴게소 데이터 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'code': 100,
                        'name': '섬진강휴게소(순천)',
                        'route_name': '남해선',
                        'x': 127.768887,
                        'y': 34.984960
                    },
                    {
                        'code': 101,
                        'name': '진영휴게소(순천)',
                        'route_name': '남해선',
                        'x': 128.715812,
                        'y': 35.278434
                    },
                    {
                        'code': 102,
                        'name': '사천휴게소(부산)',
                        'route_name': '남해선',
                        'x': None,
                        'y': None
                    }
                ]
            }
        }
    }
}
