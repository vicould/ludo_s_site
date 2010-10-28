from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^first_project/', include('first_project.foo.urls')),
    (r'^blog/$', 'blog.views.index'),
    (r'^blog/(\d{4})/$', 'blog.views.year_archive'),
    (r'^blog/(\d{4})/(\d{1,2})/$', 'blog.views.month_archive'),
    (r'^blog/(\d{4})/(\d{1,2})/(\d+)/$', 'blog.views.article_entry'),
    (r'^blog/tags/$', 'blog.views.tag_cloud'),
    (r'^blog/tags/(\w+)/$', 'blog.views.tag_cloud_result'),
	(r'^blog/authors/$', 'blog.views.author_list'),
	(r'^blog/authors/(\w+)/$', 'blog.views.author'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
