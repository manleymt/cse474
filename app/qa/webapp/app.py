from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from qa.webapp.public.routes import public_module
    

def start_app():
    app = _create_app()
    _configure_app(app)
    _extend_app(app)
    _register_modules(app)
    return app


def _create_app():
    return Flask(
        __name__, 
        template_folder='shared/templates',
        static_folder='shared/static'
    )


def _configure_app(app):
    app.config.from_object('qa.webapp.config')


def _extend_app(app):
    debug_toolbar = DebugToolbarExtension()
    debug_toolbar.init_app(app)


def _register_modules(app): app.register_blueprint(public_module)





