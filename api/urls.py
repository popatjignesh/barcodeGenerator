from django.conf.urls import patterns, include, url
from api.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^file/create/$',create_file, name='create-file'),
)


