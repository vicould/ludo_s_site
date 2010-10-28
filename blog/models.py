from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    mail = models.EmailField()
    page = models.URLField(verify_exists=True, max_length=200, blank=True)

    def __unicode__(self):
        return u"user %s" % self.username

class Author(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    bio = models.TextField()

    def __unicode__(self):
        return self.user.username

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(Author)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)

    def __unicode__(self):
        return u"comment from %s at %s" % self.author % self.date 

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    date = models.DateTimeField()
    tag = models.ManyToManyField(Tag, blank=True)
    category = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    extract = models.CharField(max_length=200, blank=False)
    comments = models.ManyToManyField(Comment, blank=True)

    def __unicode__(self):
        return self.title
