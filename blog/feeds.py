from django.contrib.syndication.views import Feed
from  blog.models import Article

class RecentArticlesFeed(Feed):
    title = "Ludo's blog last updates"
    link = "/"
    description = "Last articles feed"

    def items(self):
        return Article.objects.order_by('-date')[:5]

    def items_title(self, item):
        return item.title

    def item_description(self, item):
        return item.extract
