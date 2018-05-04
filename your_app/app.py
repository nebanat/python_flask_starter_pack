from flask import Flask, jsonify
from your_app.blueprints.user_example.views import user
from your_app.blueprints.pages_example.views import page
from your_app.blueprints.item_example.views import item


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    # reads app configuration settings from config/settings
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    # registers various application blueprints
    app.register_blueprint(user)
    app.register_blueprint(page)
    app.register_blueprint(item)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return 'hello python flask starter pack'

    @app.errorhandler(404)
    def resource_not_found(error):
        """

        :param error: error instance
        :return: 404 response of when a request resource is not found
        """

        response = jsonify(dict(error='Not found',
                                message='The requested URL was not found on the server.'))
        response.status_code = 404
        return response

    return app

