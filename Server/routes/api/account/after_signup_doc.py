CHANGE_PW = {
    'tags': ['회원가입 이후'],
    'description': '비밀번호 변경',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str'
        },
        {
            'name': 'pw',
            'description': '변경할 비밀번호',
            'in': 'formData',
            'type': 'str'
        }
    ],
    'responses': {
        '201': {
            'description': '비밀번호 변경 완료'
        }
    }
}
