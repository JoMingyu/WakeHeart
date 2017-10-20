import os

PORT = 7777

API_VER = '0.1'
API_TITLE = 'WakeHeart'
API_DESC = '''
[ENDPOINT] http://52.79.134.200:{0}
서버에서 반환되는 Status code 중 401 UNAUTHORIZED는 JWT 토큰이 만료되었음을 뜻합니다.
'''.format(PORT)

SECRET_KEY = os.getenv('SECRET_KEY')
JWT_AUTH_URL_RULE = '/signin'
JWT_AUTH_USERNAME_KEY = 'id'
JWT_AUTH_PASSWORD_KEY = 'pw'
