import json
import sys

from django.http import HttpResponse
from django.views.generic import View


class ExpVarView(View):
    def get(self, request):
        cmdline = [sys.executable] + sys.argv
        return HttpResponse(
            json.dumps(dict(cmdline=cmdline)),
            content_type="application/json",
        )
