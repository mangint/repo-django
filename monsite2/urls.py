from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^xxx/', 'polls.views.bobo'),
    url(r'^pollstest/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
