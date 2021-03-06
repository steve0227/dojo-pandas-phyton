from flask import Blueprint
from flask import g

dashboard = Blueprint('dashboard', __name__, url_prefix='/<environment>')

@dashboard.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('environment', g.environment)


@dashboard.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.environment = values.pop('environment')
    g.check_request = True

from . import views
