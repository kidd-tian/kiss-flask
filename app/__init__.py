# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask import _request_ctx_stack as stack

from .extensions import db

from .index import index

DEFAULT_BLUEPRINTS = (
    index,
)


def load_configuration(app):
    config = app.config

    from . import default_settings

    config.from_object(default_settings)


def configure_hook(app):
    @app.before_request
    def before_request():
        method = request.form.get('_method', '').upper()
        if method:
            request.environ['REQUEST_METHOD'] = method
            ctx = stack.top
            ctx.url_adapter.default_method = method
            assert request.method == method


def configure_blueprints(app, blueprints=None):
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_extensions(app):
    db.init_app(app)


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template("403.html"), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template("500.html"), 500


app = Flask(__name__)

load_configuration(app)
configure_hook(app)
configure_blueprints(app)
configure_extensions(app)
configure_error_handlers(app)
