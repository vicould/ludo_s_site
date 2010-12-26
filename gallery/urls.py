from django.conf.urls.defaults import *


urlpatterns = patterns('gallery.views',
                       (r'^$', 'gallery_index'),
                      )
