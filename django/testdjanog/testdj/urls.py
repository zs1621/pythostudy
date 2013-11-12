from django.conf.urls import patterns, url

from testdj import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index')
        )
