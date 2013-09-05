from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'models_test.views.home', name='home'),
    # url(r'^models_test/', include('models_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'models_app.views.index', name='index'),
    url(r'^login/$','models_app.views.auth_login', name='auth_login'),
    url(r'^logout/$', 'models_app.views.auth_logout', name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logup/$', 'models_app.views.logup', name='logup'),
    url(r'^success/(?P<message>[\w]+)/$', 'models_app.views.success', name='success'),
)
