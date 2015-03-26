from django.conf.urls import patterns, include, url

urlpatterns = patterns('server.views',
    url(r'^$', 'index'),
    url(r'^fetch/$', 'fetch_pdf'),
)
