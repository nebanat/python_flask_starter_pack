from marshmallow import Schema, fields, pre_load
from your_app.blueprints.item_example.schemas.item_schema import ItemSchema


class UserSchema(Schema):
    """
        This defines an object schema for the user blueprint

        Object schemas can come in handy when you designing APIs

    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    created_at = fields.DateTime(dump_only=True, missing='')
    updated_at = fields.DateTime(dump_only=True, missing='')
    items = fields.Nested(ItemSchema, many=True, missing=[])  # nested schema to reflect db relationship

    class Meta:
        strict = True

    @pre_load()
    def user_details_to_strip(self, data):
        data['name'] = data['name'].lower().strip()
        data['email'] = data['email'].lower().strip()
