SIGNUP = {
    'tags': ['회원가입'],
    'description': '회원가입',
    'parameters': [
        {
            'name': 'id',
            'description': '사용자 ID',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'pw',
            'description': '사용자 PW',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'position',
            'description': '포지션(학생: 0, 운전자: 1, 일반: 2, 기본값 2)',
            'in': 'formData',
            'type': 'int'
        },
        {
            'name': 'sex',
            'description': '성별',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'age',
            'description': '나이',
            'in': 'formData',
            'type': 'int'
        }
    ],
    'responses': {
        '201': {
            'description': '회원가입 성공'
        },
        '204': {
            'description': '회원가입 실패(중복된 ID)'
        }
    }
}
