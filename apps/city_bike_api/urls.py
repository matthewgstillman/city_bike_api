from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^company$', views.company, name='company'),
    url(r'^company/(?P<id>[-\w]+)/$', views.company_name, name='company_name'),
]