from flask import jsonify
from flask_restful import Resource
from webargs.flaskparser import use_args
from your_app.blueprints.item_example.schemas.item_schema import ItemSchema


class SingleItemResource(Resource):
    def get(self, item_id=None):
        """
        The function simulates getting a particular user resource

        This could be a database call to get a single user resource but for
        the sake of demo we would simulate the db call

        :return: jsonfied serialized UserSchema object
        """

        item_data = {
            'price': 20,
            'name': 'chicken'
        }

        if item_id:
            item_data['id'] = item_id

        result = ItemSchema().dump(item_data)

        return jsonify(result.data)

    @use_args(ItemSchema())
    def post(self, args, item_id=None):
        """
        The function simulates a /POST request for Item resource

        This could be a database call to create an item but for
        the sake of demo we would simulate the db call

        :param
            args: user request args
            (which is validated by ItemSchema using the decorator @user_args)
            item_id = item id

        :return: jsonified deserialized UserSchema object
        """

        new_item = dict(id=item_id, **args)
        result = ItemSchema().dump(new_item)
        return jsonify(result.data)
