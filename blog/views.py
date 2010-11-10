# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from blog.models import Article, Tag, Author

def index(request):
    latest_entries_list = Article.objects.all().order_by('-date')[:5]
    return render_to_response('blog/index.html', {'latest_entries_list': latest_entries_list,})


def year_archive(request, year):
    year_archive_list = Article.objects.filter(date__year=year).order_by('-date')
    return render_to_response('blog/yearly_archives.html', {'year_archive_list': year_archive_list,})


def month_archive(request, year, month):
    month_archive_list = Article.objects.filter(date__year=year, date__month=month)
    return render_to_response('blog/monthly_archives.html', {'month_archive_list': month_archive_list,})


def article_entry(request, year, month, article_id):
    a = get_object_or_404(Article, date__year=year, date__month=month, id=article_id,)
    return render_to_response('blog/entry.html', {'entry': a}, context_instance=RequestContext(request))


def tag_cloud(request):
    tag_list = Tag.objects.all()
    return render_to_response('blog/tag_cloud.html', {'tag_list': tag_list})


def tag_cloud_result(request, tag_requested):
    tagged_articles_list = Article.objects.filter(tag__name=tag_requested)
    return render_to_response('blog/tag_cloud_results.html', {'tagged_articles_list': tagged_articles_list})


def author_list(request):
	author_list = Author.objects.all()
	return render_to_response('blog/alls_author.html', {'author_list': author_list})


def author(request, author):
	publications_list = Article.objects.filter(author__user__username=author)
	return render_to_response('blog/author_articles.html', {'publications_list': publications_list})


def compute_month(month):
    month_tab = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    return month_tab[month-1]


