# -*- coding: utf-8 -*-

from django import template

register = template.Library()

from ludo_s_site.blog.models import Tag, Article

class CloudNode(template.Node):

    def __init__(self, var_name):
        self.var_name = var_name


    def render(self, context):
        tag_list = Tag.objects.all()
        tag_dict = {}
        total_tagged = 0

        for tag_item in tag_list:
            length = Article.objects.filter(tag__name__exact=tag_item).count()
            if (length == 0):
                continue
            tag_dict = dict(tag_dict.items() + 
                            { tag_item : length }.items())
            total_tagged += length

        for tag_entry in tag_dict.iterkeys():
            tag_dict[tag_entry] = tag_dict[tag_entry]/float(total_tagged)

        context[self.var_name] = tag_dict
        
        return ''

import re

@register.tag('tag_cloud')
def create_cloud(parser, token):

    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag syntax is to only specify\
                the variable name " % token.contents.split()[0]
    if (arg.split().__len__() > 2):
        raise template.TemplateSyntaxError, "%s tag requires no argument" % \
                tag_name
    var_name = arg.split()[1]
    return CloudNode(var_name)
