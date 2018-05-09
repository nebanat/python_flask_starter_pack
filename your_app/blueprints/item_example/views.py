from flask import Blueprint, render_template
from flask_restful import Api
from your_app.blueprints.item_example.resources.item_resource \
    import ItemResource
from your_app.blueprints.item_example.resources.single_item_resource \
    import SingleItemResource

# registers a new item blueprint
item = Blueprint('item', __name__,
                 url_prefix='/items', template_folder='templates')

item_api = Api(item)


# creates custom routes for item blueprint
@item.route('/')
def item_index():
    return render_template('item/index.html')


# register all resources associated with the item blueprint
# do not forget the appended url_prefix when creating the item blueprint
item_api.add_resource(ItemResource, '/api')
item_api.add_resource(SingleItemResource, '/api/<int:item_id>')
