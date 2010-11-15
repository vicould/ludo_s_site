from django.conf.urls.defaults import *
from django.views.generic import date_based
from blog.models import Article
from blog.feeds import RecentArticlesFeed

year_re = '(?P<year>\d{4})'
month_re = '(?P<month>\d{2})'
article_id_re = '(?P<article_id>\d+)'
tags_string = 'tags'
authors_string = 'authors'
author_re = '(?P<author>\w+)'
pages_string = 'pages'
page_re = '(?P<title>.+)'
category_string = 'categories'
category_re = '(?P<category_name>.+)'

article_query_basis_dictionary = { 'queryset' : Article.objects.all(), 'date_field' :
                     'date'}

urlpatterns = patterns('blog.views',
    (r'^$',
     date_based.archive_index,
     dict(article_query_basis_dictionary.items() + { 'template_object_name' :
                                            'object_list' }.items())),
    (r'^%(year_re)s/$' % locals(),
     date_based.archive_year,
     dict(article_query_basis_dictionary.items() + { 'make_object_list' : True }.items())),
    (r'^%(year_re)s/%(month_re)s/$' % locals(),
     date_based.archive_month,
     dict(article_query_basis_dictionary.items() + { 'month_format' : '%m' }.items())),
    (r'^%(year_re)s/%(month_re)s/%(article_id_re)s/$' % locals(), 'article_entry'),
    (r'^%(tags_string)s/$' % locals(), 'tag_cloud'),
    (r'^%(tags_string)s/(?P<tag_requested>)/$' % locals(), 'tag_cloud_result'),
    (r'^%(authors_string)s/$' % locals(), 'author_list'),
    (r'^%(authors_string)s/%(author_re)s/$' % locals(), 'author'),
    (r'^latest/feed/$', RecentArticlesFeed()),
    (r'^%(pages_string)s/$' % locals(), 'pages_index' ),
    (r'^%(pages_string)s/%(page_re)s/$' % locals(), 'page_entry' ),
    (r'^%(category_string)s/$' % locals(), 'categories_index'),
    (r'^%(category_string)s/%(category_re)s/$' % locals(), 'category_detail'),

)
