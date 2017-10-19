from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT

import preprocessor
from support import jwt


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
    _app.run(port=_app.config['PORT'], debug=True)
