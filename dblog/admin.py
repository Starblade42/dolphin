from django.contrib import admin
from dblog.models import Author
from dblog.models import Blog
from dblog.models import Article
from dblog.models import Review
from dblog.models import Media
from dblog.models import Tutorial

admin.site.register(Author)
admin.site.register(Blog)

class ArticleAdmin(admin.ModelAdmin):
	fieldsets = [
		('Main Info',		{'fields':	['articleID', 'title', 'subtitle', 'authorID']}),
		('Content',			{'fields':	['body', 'sources']}),
		('Date',			{'fields':	['timestamp']})
	] 	

admin.site.register(Article, ArticleAdmin)
admin.site.register(Review)
admin.site.register(Media)
admin.site.register(Tutorial)
