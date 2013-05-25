from django.conf.urls import patterns, url

urlpatterns = patterns('api.views',
k    url(r'^api/$', 'snippet_list'),
    url(r'^api/(?P<pk>[0-9]+)/$', 'snippet_detail'),
)
