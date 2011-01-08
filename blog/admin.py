from ludo_s_site.blog.models import Article, Author, Tag, User, Category, Page
from ludo_s_site.blog.models import TopMenuElement, SideMenuElement
from django.contrib import admin


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Content', {'fields' : ['title', 'content', 'author', 'date',
                                     'excerpt', 'allow_comments']}),
            ('Classification', {'fields' : ['category', 'tag']})
            ]
    list_display = ('date', 'title', 'author')
    list_filter = ['date']
    search_fields = ['title']
    date_hierarchy = 'date'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(TopMenuElement)
admin.site.register(SideMenuElement)
