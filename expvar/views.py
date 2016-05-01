import importlib
import inspect
import json


from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

from . import ExpVar


def run_single_class(name, obj):
    if not issubclass(obj, ExpVar):
        return dict()
    if name == "ExpVar":
        # skip the parent class
        return dict()
    c = obj()
    return {c.get_name(): c.value()}


def load_expvars_from_app(app):
    d = dict()
    a = None
    try:
        a = importlib.import_module("{}.vars".format(app))
    except ImportError:
        # no 'expvar' module for this app
        pass
    if a is not None:
        for name, obj in inspect.getmembers(a, inspect.isclass):
            d.update(run_single_class(name, obj))
    return d


class ExpVarView(View):
    def get(self, request):
        d = dict()
        for app in settings.INSTALLED_APPS:
            appvars = load_expvars_from_app(app)
            d.update(appvars)
        return HttpResponse(
            json.dumps(d),
            content_type="application/json",
        )
