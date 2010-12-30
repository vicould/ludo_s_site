# -*- coding: utf-8 -*-
import Image
from PIL.ExifTags import TAGS
from datetime import datetime


def get_decoded_tags(filename):
    """Decodes the tags from their raw form"""
    pic = Image.open(filename)
    tags = pic._getexif()
    ret = {}
    for tag, value in tags.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value

    return ret


def parse_date_tag(tags):
    """Gets the date from the DateTime tag in the EXIF"""
    return datetime.strptime(tags['DateTime'], '%Y:%m:%d %H:%M:%S')


def get_date(filename):
    """Retrieves the picture taken time from the given file"""
    return parse_date_tag(get_decoded_tags(filename))
