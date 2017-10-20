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

CHANGE_INFO = {
    'tags': ['회원가입 이후'],
    'description': '사용자 정보 변경',
    'parameters': [
        {
            'name': 'Authorization',
            'description': 'JWT Token',
            'in': 'header',
            'type': 'str'
        },
        {
            'name': 'position',
            'description': '변경할 포지션(학생: 0, 운전자: 1, 일반: 2)',
            'in': 'formData',
            'type': 'int'
        },
        {
            'name': 'sex',
            'description': '변경할 성별',
            'in': 'formData',
            'type': 'str'
        },
        {
            'name': 'age',
            'description': '변경할 나이',
            'in': 'formData',
            'type': 'int'
        }
    ],
    'responses': {
        '201': {
            'description': '사용자 정보 변경 완료'
        }
    }
}
