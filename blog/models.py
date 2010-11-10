from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    extract = models.CharField(max_length=200, blank=False)

    def __unicode__(self):
        return self.title


