from flask import Blueprint, render_template


public_module = Blueprint(
    'public_module',
    __name__,
    template_folder='templates',
    static_folder='static')


@public_module.route('/')
def index():
    # Do some stuff
    return render_template('public/index.html')


@public_module.route('/about')
def about():
    # Do some stuff
    return render_template('public/about.html')


@public_module.route('/privacy')
def privacy():
    # Do some stuff
    return render_template('public/privacy.html')


@public_module.route('/terms')
def terms():
    # Do some stuff
    return render_template('public/terms.html')
