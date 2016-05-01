from django.conf.urls import url
from expvar.views import ExpVarView

urlpatterns = [
    url('^debug/vars$', ExpVarView.as_view(), name='expvar'),
]
