import json

from django.http import HttpResponse
from django.views.generic import View


class ExpVarView(View):
    def get(self, request):
        return HttpResponse(
            dict(),
            content_type="application/json",
        )
