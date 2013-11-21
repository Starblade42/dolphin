from django.contrib import admin
from dblog.models.dblog import Author
from dblog.models.dblog import Blog
from dblog.models.dblog import Article
from dblog.models.dblog import Updates
from dblog.models.dblog import Review
from dblog.models.dblog import Media
from dblog.models.dblog import Tutorial

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Article)
admin.site.register(Updates)
admin.site.register(Review)
admin.site.register(Media)
admin.site.register(Tutorial)
