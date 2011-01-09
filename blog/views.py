# Create your views here.
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext, Context, loader
from ludo_s_site.blog.models import Article, Tag, Author, Category, Page


@csrf_protect
def article_entry(request, year, month, article_id):
    try:
        a = Article.objects.defer('excerpt').get(date__year=year, date__month=month,
                                id=article_id)
    except Article.DoesNotExist:
        raise Http404
    path = request.build_absolute_uri()
    return render_to_response('blog/article_entry.html', 
                              {'article_entry': a, 'current_url' : path}, 
                              context_instance=RequestContext(request))


def tag_cloud(request):
    return render_to_response('blog/tag_cloud.html', context_instance=RequestContext(request))


def tag_cloud_result(request, tag_name):
    tagged_articles_list = Article.objects.filter(tag__name=tag_name)
    return render_to_response('blog/tag_cloud_results.html', {'object_list': tagged_articles_list}, context_instance=RequestContext(request))


def author_list(request):
	author_list = Author.objects.all()
	return render_to_response('blog/alls_author.html', {'object_list': author_list}, context_instance=RequestContext(request))


def author(request, author):
	publications_list = Article.objects.defer('content').filter(author__user__username=author)
	return render_to_response('blog/author_articles.html', {'object_list': publications_list}, context_instance=RequestContext(request))


def pages_index(request):
    pages_list = Page.objects.defer('content', 'allow_comments').all()
    return render_to_response('layout/page_archive_template.html', {'pages_list' :
                                                        pages_list}, context_instance=RequestContext(request))

def page_entry(request, page_title):
    try:
        p = Page.objects.defer('excerpt').get(title=page_title) 
    except Page.DoesNotExist:
        raise Http404
    path = request.build_absolute_uri()
    return render_to_response('blog/page_entry.html', 
                              {'page_entry' : p, 'current_url' : path },
                              context_instance=RequestContext(request))

def categories_index(request):
    categories_list = Category.objects.all()
    return render_to_response('blog/categories_index.html', 
                              {'categories_list' : categories_list}, context_instance=RequestContext(request))

def category_detail(request, category_name):
    related_articles_list = \
    Article.objects.filter(category__name=category_name).order_by('-date')
    related_pages_list = Page.objects.filter(category__name=category_name)
    return render_to_response('blog/category_detail.html',
                              {'related_articles_list' : related_articles_list,
                               'related_pages_list' : related_pages_list}, context_instance=RequestContext(request))
