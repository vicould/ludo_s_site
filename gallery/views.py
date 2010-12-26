# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context, loader
from gallery.models import Picture, Set, Collection, Tag


