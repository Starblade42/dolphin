from django.conf.urls import patterns, url

from dblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)