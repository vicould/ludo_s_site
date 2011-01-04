# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from ludo_s_site.gallery.models import Picture, Set, Collection, Tag


def gallery_index(request):
    sets_list = Set.objects.all().order_by('-date')
    return render_to_response('gallery/index.html', {'sets_list' : sets_list},
                             context_instance=RequestContext(request))


def set_detail(request, set_id):
    set_entry = get_object_or_404(Set, id=set_id)
    return render_to_response('gallery/album.html', {'set_entry' : set_entry},
                             context_instance=RequestContext(request))


def pic_detail(request, set_id, pic_id):
    picture = get_object_or_404(Picture, id=pic_id)
    return render_to_response('gallery/picture.html', {'pic_entry' : picture},
                             context_instance=RequestContext(request))


def collection_index(request):
    collections = Collection.objects.all()
    return render_to_response('gallery/collection.html', 
                              {'collection_list' : collections },
                              context_instance=RequestContext(request))


def collection_detail(request, collection_id):
    collection_entry = get_object_or_404(Collection, id=collection_id)
    return render_to_response('gallery/collection.html', 
                              {'collection_entry' : collection_entry},
                              context_instance=RequestContext(request))
