from django.conf.urls import patterns, url

from dblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<author_ID>\w+)/$', views.detail, name='detail'),
    url(r'^(?P<author_ID>\w+)/(?P<blog_ID>\w+)/$', views.blog, name='blog')
)
