import os

PORT = 7777

API_VER = '0.1'
API_TITLE = 'WakeHeart'
API_DESC = '[ENDPOINT] http://52.79.134.200:' + str(PORT)

SECRET_KEY = os.getenv('SECRET_KEY')
JWT_AUTH_URL_RULE = '/signin'
JWT_AUTH_USERNAME_KEY = 'id'
JWT_AUTH_PASSWORD_KEY = 'pw'
