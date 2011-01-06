# -*- coding: utf-8 -*-

from django import template

register = template.Library()

from ludo_s_site.blog.models import TopMenuElement, SideMenuElement


class TopMenuElementsNode(template.Node):
    """Defines the node used to create the menu elements list. It sets the
    list of the elements as a variable of the context. The name of the variable
    is processed through the create_menu function, see below.
    """
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = \
                TopMenuElement.objects.all().order_by('position')
        return ''


import re

@register.tag('top_menu_content')
def create_top_menu(parser, token):
    """Parses the content of the token before calling the Node class."""
    try:
        # Splitting by None == splitting by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag syntax is to only specify \
                the variable name " % token.contents.split()[0]
    if (arg.split().__len__() > 2):
        raise template.TemplateSyntaxError, "%s tag requires no argument" % \
                tag_name
    var_name = arg.split()[1]
    return TopMenuElementsNode(var_name)



class SideMenuElementsNode(template.Node):
    """Defines the node used to create the menu elements list. It sets the
    list of the elements as a variable of the context. The name of the variable
    is processed through the create_menu function, see below.
    """
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = \
                SideMenuElement.objects.all().order_by('position')
        return ''


import re

@register.tag('side_menu_content')
def create_left_menu(parser, token):
    """Parses the content of the token before calling the Node class."""
    try:
        # Splitting by None == splittinh by spaces.
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%s tag syntax is to only specify \
                the variable name " % token.contents.split()[0]
    if (arg.split().__len__() > 2):
        raise template.TemplateSyntaxError, "%s tag requires no argument" % \
                tag_name
    var_name = arg.split()[1]
    return SideMenuElementsNode(var_name)
