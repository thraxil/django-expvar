import importlib
import inspect
import json
import resource
import sys

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

from . import ExpVar


def get_memory_usage():
    memstats = resource.getrusage(resource.RUSAGE_SELF)
    return dict(
        utime=memstats.ru_utime,
        stime=memstats.ru_stime,
        maxrss=memstats.ru_maxrss,
        ixrss=memstats.ru_ixrss,
        idrss=memstats.ru_idrss,
        isrss=memstats.ru_isrss,
        minflt=memstats.ru_minflt,
        majflt=memstats.ru_majflt,
        nswap=memstats.ru_nswap,
        inblock=memstats.ru_inblock,
        oublock=memstats.ru_oublock,
        msgsnd=memstats.ru_msgsnd,
        msgrcv=memstats.ru_msgrcv,
        nsignals=memstats.ru_nsignals,
        nvcsw=memstats.ru_nvcsw,
        nivcsw=memstats.ru_nivcsw,
    )


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
        cmdline = [sys.executable] + sys.argv
        d = dict(
            cmdline=cmdline,
            memory=get_memory_usage(),
        )
        for app in settings.INSTALLED_APPS:
            appvars = load_expvars_from_app(app)
            d.update(appvars)
        return HttpResponse(
            json.dumps(d),
            content_type="application/json",
        )
