# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from gallery.models import Picture, Set, Collection, Tag


def gallery_index(request):
    sets_list = Set.objects.all().order_by('-date')
    return render_to_response('gallery/index.html', {'sets_list' : sets_list})


def set_detail(request, set_id):
    pictures = Picture.objects.filter(album)
    return render_to_response('gallery/album.html', {'pictures_list' : pictures})


def pic_detail(request, pic_id):
    picture = get_object_or_404(Picture, id=pic_id)
    return render_to_response('gallery/picture.html', {'pic' : picture})

def collection_index(request):
    collections = Collection.objects.all()
    return render_to_response('gallery/collection.html', {'collection_list' :
                                                          collections })
