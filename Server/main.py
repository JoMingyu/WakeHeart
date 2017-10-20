from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT

import preprocessor
from support import jwt

from support.api_interaction import wise_saying, rest_area


def create_app():
    """
    :rtype: Flask
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    CORS(app)
    JWT(app, authentication_handler=jwt.authenticate, identity_handler=jwt.identity)

    preprocessor.decorate(app)
    preprocessor.add_resource(app)

    return app

_app = create_app()


if __name__ == '__main__':
    wise_saying.parse()
    rest_area.parse()
    _app.run(port=_app.config['PORT'], debug=True)
