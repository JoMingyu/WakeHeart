WISE_SAYING = {
    'tags': ['명언'],
    'description': '명언 데이터 불러오기',
    'responses': {
        '200': {
            'description': '명언 데이터 조회 성공',
            'examples': {
                'application/json': [
                    {
                        'author': '정근철',
                        'say': 'ㅂㅇㄹ'
                    },
                    {
                        'author': '정윤재',
                        'say': '열심히 살자'
                    },
                    {
                        'author': '윤태훈',
                        'say': 'Boys be ambitious'
                    }
                ]
            }
        }
    }
}
