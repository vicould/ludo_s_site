from django.db import models
# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=100)


    def __unicode__(self):
        return self.name

    
    def get_absolute_url(self):
        return '/gallery/tags/%s' % self.name



class Collection(models.Model):
    name = models.CharField(max_length=100)
    sets = models.ForeignKey('Set', blank=True)

    def __unicode__(self):
        return self.name

    
    def get_absolute_url(self):
        return '/gallery/collections/%s' % self.id



class Set(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    place = models.CharField(max_length=200, blank=True)
    pictures = models.ForeignKey('Picture', related_name='album')
    front_pic = models.OneToOneField('Picture', blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __unicode__(self):
        return self.name

    
    def get_absolute_url(self):
        return '/gallery/%s' % self.id



class Picture(models.Model):
    pic = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    abstract = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

    
    def get_absolute_url(self):
        return '/gallery/%s/%s' % (self.album, self.id)



# --- callback functions, called on a signal  ---

import re
from ludo-s-site.gallery import exif_utils

def fill_picture_set(sender, **kwargs):
    """Called on save of a picture in the database: retrieves the EXIF
    informations in order to fill the fields of the model"""
    try:
        instance = kwargs['instance']
    except KeyError:
        return

    filename_re = re.compile('[^/]*$')

    path = instance.pic.path
    filename = filename_re.search(path)

    exif_date = exif_utils.get_date(path)
    if (exif_date == instance.date):
        return # we already saved this one, pass
    instance.date = exif_date

    if (filename != None):
        instance.title = filename.group()

    instance.save()



# --- connecting the functions ---
from django.db.models.signals import post_save

# functions for the Picture model
post_save.connect(fill_picture_set, sender=Picture)
