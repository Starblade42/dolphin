from django.contrib import admin
from dblog.models import Author
from dblog.models import Blog
from dblog.models import Article
from dblog.models import Review
from dblog.models import Media
from dblog.models import Tutorial

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(Review)
admin.site.register(Media)
admin.site.register(Tutorial)
