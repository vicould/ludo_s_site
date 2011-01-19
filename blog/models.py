from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return '/authors/%s' % self.user.username.replace(' ', '%20')


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/tags/%s' % self.name.replace(' ', '%20')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/categories/%s' % self.name.replace(' ', '%20')


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField()
    category = models.ForeignKey(Category)
    allow_comments = models.BooleanField(default=True)


    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/pages/%s" % self.title.replace(' ', '%20')


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category)
    content = models.TextField()
    excerpt = models.TextField()
    allow_comments = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.date.year, self.date.strftime("%m"), self.id)


class TopMenuElement(models.Model):
    element = models.CharField(max_length=20)
    url_suffix = models.CharField(max_length=100, blank=True) # blank is for home
    position = models.IntegerField()

    def __unicode__(self):
        return self.element

    def get_absolute_url(self):
        return '/%s' % self.url_suffix.replace(' ', '%20')


class SideMenuElement(models.Model):
    element = models.CharField(max_length=20)
    url_suffix = models.CharField(max_length=100, blank=True)
    position = models.IntegerField()

    def __unicode__(self):
        return self.element

    def get_absolute_url(self):
        return '/%s' % self.url_suffix.replace(' ', '%20')

