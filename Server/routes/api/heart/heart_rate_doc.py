HEART_RATE_POST = {
    'tags': ['심박수'],
    'description': '심박수 상태 업로드',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str'
        },
        {
            'name': 'rate',
            'description': '심박수',
            'in': 'formData',
            'type': 'int'
        }
    ],
    'responses': {
        '201': {
            'description': '심박수 상태 업로드 성공'
        }
    }
}

HEART_RATE_GET = {
    'tags': ['심박수'],
    'description': '특정 날짜의 심박수 상태 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str'
        },
        {
            'name': 'date',
            'description': '조회할 날짜(YYYY-MM-DD)',
            'in': 'query',
            'type': 'str'
        }
    ],
    'responses': {
        '200': {
            'description': '심박수 상태 조회 성공',
            'examples': {
                'application/json': {
                    'rate': 98
                }
            }
        },
        '204': {
            'description': '해당 사용자에 대한 심박수 상태 없음'
        }
    }
}

DATE_RANGE_BASED_HEART_RATE = {
    'tags': ['심박수'],
    'description': '두 날짜 사이 심박수 상태 조회',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str'
        },
        {
            'name': 'start_date',
            'description': '시작 날짜(YYYY-MM-DD)',
            'in': 'query',
            'type': 'str'
        },
        {
            'name': 'end_date',
            'description': '끝 날짜(YYYY-MM-DD)',
            'in': 'query',
            'type': 'str'
        }
    ],
    'responses': {
        '200': {
            'description': '두 날짜 사이 심박수 데이터 있음',
            'examples': {
                'application/json': [
                    {
                        'date': '2017-10-17',
                        'rate': 108
                    },
                    {
                        'date': '2017, 10, 18',
                        'rate': 95
                    }
                ]
            }
        },
        '204': {
            'description': '두 날짜 사이 심박수 데이터 없음'
        }
    }
}
