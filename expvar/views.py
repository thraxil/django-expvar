import json

from django.http import HttpResponse
from django.views.generic import View


class ExpVarView(View):
    def get(self, request):
        return HttpResponse(
            json.dumps(dict()),
            content_type="application/json",
        )
