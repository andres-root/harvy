from django.conf.urls import patterns, url

urlpatterns = patterns('api.views',
    url(r'^api/$', 'snippet_list'),
    url(r'^api/(?P<pk>[0-9]+)/$', 'snippet_detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
)
