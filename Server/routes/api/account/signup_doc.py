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
