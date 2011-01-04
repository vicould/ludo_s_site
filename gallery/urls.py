from django.conf.urls.defaults import *


collection_string = 'collections'
collection_re = '(?P<collection_id>\d+)'
set_re = '(?P<set_id>\d+)'
picture_re =  '(?P<pic_id>\d+)'
tag_string = 'tags'
tag_re = '(?P<tag_name>\w+)'


urlpatterns = patterns('ludo_s_site.gallery.views',
                       (r'^$', 'gallery_index'),
                       (r'^%(set_re)s/$' % locals(), 'set_detail'),
                       (r'^%(set_re)s/%(picture_re)s/$' % locals(), 'pic_detail'),
                       (r'^%(collection_string)s/$' % locals(), 'collection_index'),
                       (r'^%(collection_string)s/%(collection_re)s$' % locals(),
                        'collection_detail'),
                      )
