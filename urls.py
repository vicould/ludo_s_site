from django.conf.urls.defaults import *
from django.views.generic import date_based

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # the blog
    (r'^', include('blog.urls')),

    # For the comments
    (r'^comments/', include('django.contrib.comments.urls')),
)
