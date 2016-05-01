from django.conf.urls import include, url
from expvar.views import ExpVarView

urlpatterns = [
    url('^debug/vars$', ExpVarView.as_view()),
]
