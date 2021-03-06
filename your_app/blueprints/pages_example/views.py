from flask import Blueprint, render_template

# registers a new page blueprint
page = Blueprint('page', __name__, template_folder='templates')


# creates custom routes for page blueprint
@page.route('/contact')
def contact():
    return render_template('page/contact.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')
