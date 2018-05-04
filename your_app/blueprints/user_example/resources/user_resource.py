from flask import jsonify
from flask_restful import Resource
from webargs.flaskparser import use_args
from your_app.blueprints.user_example.schemas.user_schema import UserSchema


class UserResource(Resource):
    def get(self):
        """
        The function simulates a /GET request for user resource

        This could be a database call to get a single user resource but for
        the sake of demo we would simulate the db call

        :return: jsonfied serialized UserSchema object
        """

        user_data = {
            'created_at': '2014-08-11T05:26:03.869245',
            'email': u'ken@yahoo.com',
            'name': u'Ken'
        }

        item_data = {
            'name': 'user item',
            'price': 20
        }

        items = [item_data]
        user_data['items'] = items

        result = UserSchema().load(user_data)

        return jsonify(result.data)

    @use_args(UserSchema())
    def post(self, args):
        """
        The function simulates /POST for user resource

        This could be a database call to create a single user resource but for
        the sake of demo we would simulate the db call

        :param args: user request args (which is validated by UserSchema using the decorator @user_args)
        :return: jsonfied serialized UserSchema object
        """
        new_user = dict(**args)
        result = UserSchema().dump(new_user)

        return jsonify(result.data)
