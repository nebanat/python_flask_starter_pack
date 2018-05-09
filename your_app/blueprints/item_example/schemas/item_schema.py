from marshmallow import Schema, fields, pre_load
# from your_app.blueprints.user_example.schemas.user_schema import UserSchema


class ItemSchema(Schema):
    """
        This defines an object schema for Item

        Object schemas can come in handy when you designing APIs
        especially for validating user input and serialization/deserialization

        for more info:
            https://marshmallow.readthedocs.io

    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    slug = fields.Str(required=True)
    price = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True, missing='')
    updated_at = fields.DateTime(dump_only=True, missing='')
    # user = fields.Nested(UserSchema, only=['name', 'email'])

    class Meta:
        strict = True

    @pre_load()
    def item_details_to_strip(self, data):
        """
        This functions shows an example of marshmallow preload event

         for more info:
            https://marshmallow.readthedocs.io

        :param data: user request data
        :return:
        """
        data['name'] = data['name'].lower().strip()
        return data

    @pre_load()
    def slugify_description(self, data):
        data['slug'] = data['description'].lower().strip().replace(' ', '-')
        return data
