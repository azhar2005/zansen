from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'zansen.views.index', name='index'),
    url(r'^news', 'zansen.views.news', name='news'),
    url(r'^msg', 'zansen.views.msg', name='msg'),
    url(r'^send_msg', 'zansen.views.send_msg', name='send_msg'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
