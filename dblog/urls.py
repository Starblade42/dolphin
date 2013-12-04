from django.conf.urls import patterns, url

from dblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<author_id>\d+)/$', views.detail, name='detail')
)