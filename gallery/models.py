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
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    pictures = models.ForeignKey('Picture', related_name='album')
    front_pic = models.OneToOneField('Picture')

    def __unicode__(self):
        return self.name

    
    def get_absolute_url(self):
        return '/gallery/%s' % self.id



class Picture(models.Model):
    pic = models.ImageField(upload_to='photo/%Y/%m/%d')
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    abstract = models.TextField(blank=True)

    def __unicode__(self):
        return self.title

    
    def get_absolute_url(self):
        return '/gallery/%s/%s' % (self.album, self.id)
