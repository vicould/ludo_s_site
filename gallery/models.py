from django.db import models

# Create your models here.



class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name



class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name



class Set(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    place = models.CharField(max_length=200)
    collection = models.OneToOneField(Collection, blank=True)
    front_pic = models.OneToOneField('Picture', limit_choices_to = {'album' :
                                                                    id })

    def __unicode__(self):
        return self.name



class Picture(models.Model):
    pic = models.ImageField(upload_to='photo/%Y/%m/%d')
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    album = models.OneToOneField(Set)
    abstract = models.TextField(blank=True)

    def __unicode__(self):
        return self.title
