from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'comment.views.home', name='home'),
    # url(r'^comment/', include('comment.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app.views.comment'),
    url(r'^comment-list/$','app.views.comment_list'),
    url(r'^info/(?P<message>[\w\-]+)/$', 'app.views.info'),
)
