from django.conf.urls.defaults import *
from django.views.generic import date_based
from blog.models import Article

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

year_re = '(?P<year>\d{4})'
month_re = '(?P<month>\d{2})'
article_id_re = '(?P<object_id>\d+)'
tags_string = 'tags'
authors_string = 'authors'
author_re = '(?P<author>\w+)'

query_basis_dictionary = { 'queryset' : Article.objects.all(), 'date_field' :
                     'date'}

urlpatterns = patterns('blog.views',
    (r'^$',
     date_based.archive_index,
     query_basis_dictionary),
    (r'^%(year_re)s/$' % locals(),
     date_based.archive_year,
     dict(query_basis_dictionary.items() + { 'make_object_list' : True }.items())),
    (r'^%(year_re)s/%(month_re)s/$' % locals(),
     date_based.archive_month,
     dict(query_basis_dictionary.items() + { 'month_format' : '%m' }.items())),
    (r'^%(year_re)s/%(month_re)s/%(article_id_re)/$', 'article_entry'),
    (r'^%(tags_string)s/$' % locals(), 'tag_cloud'),
    (r'^%(tags_string)s/(?P<tag_requested>)/$' % locals(), 'tag_cloud_result'),
    (r'^%(authors_string)s/$' % locals(), 'author_list'),
    (r'^%(authors_string)s/%(author_re)s/$' % locals(), 'author'),

)
