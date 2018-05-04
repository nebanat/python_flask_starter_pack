from flask import jsonify
from flask_restful import Resource
from your_app.blueprints.item_example.schemas.item_schema import ItemSchema


class ItemResource(Resource):
    def get(self):
        """
        The function simulates /GET request for item resource

        This could be a database call to get all item resources but for
        the sake of demo we would simulate the db call

        :return: jsonified deserialized ItemSchema object (please see ItemSchema)
        """

        item_data_one = dict(name='some item', price=20)

        item_data_two = dict(name='another item', price=50)

        items = [item_data_one, item_data_two]

        result = ItemSchema(many=True).dump(items)

        return jsonify(dict(items=result.data, message='items successfully fetched'))

