from flask import Blueprint, render_template
from flask_restful import Api
from your_app.blueprints.user_example.resources.user_resource \
    import UserResource

# registers a new user blueprint
user = Blueprint('user', __name__,
                 url_prefix='/user', template_folder='templates')

user_api = Api(user)


# creates custom routes for user blueprint
@user.route('/')
def user_index():
    return render_template('user/index.html')


@user.route('/register')
def register():
    return render_template('user/registration.html')


# register all resources associated with the user blueprint
# do not forget the appended
user_api.add_resource(UserResource, '/api')
