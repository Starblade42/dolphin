from django.db import models

#Authors	authorID	firstName	lastName
#This will create and Auto-Incrementing ID primary key!

class Author(models.Model):
	authorID = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.authorID + ": " + self.lastName + " " + self.firstName
	

#Blog	blogId	authorID	title	subtitle	editor
#This will create and Auto-Incrementing ID primary key!

class Blog(models.Model):
	blogID = models.CharField(max_length=50)
	authorID = models.ForeignKey(Author, related_name='author_blog')
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=120, null=True, blank=True)
	editor = models.ForeignKey(Author, null=True, blank=True, related_name='author_blog_editor')
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.blogID + ": " + self.title
	
#Article	articleId	title	subtitle	authorId	body	sources

class Article(models.Model):
	articleID = models.CharField(max_length=140)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256, null=True, blank=True)
	authorID = models.ForeignKey(Author, related_name='author_article')
	body = models.TextField()
	sources = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField()
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.articleID + ": " + self.title

#Updates	authorID	articleID	timestamp
#This will create and Auto-Incrementing ID primary key!

class Update(models.Model):
	authorID = models.ForeignKey(Author, related_name='author_update')
	articleID = models.ForeignKey(Article, related_name='article_update')
	timestamp = models.DateTimeField()
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.articleID + ": " + self.timestamp



#Review	reviewId	title	subtitle	body	score	datePosted	productId

class Review(models.Model):
	reviewID = models.CharField(max_length=256, null=True, blank=True)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256, null=True, blank=True)
	authorID = models.ForeignKey(Author, related_name='author_review')
	body = models.TextField()
	score = models.CharField(max_length=256, null=True, blank=True)
	timestamp = models.DateTimeField()
	productID = models.CharField(max_length=256, null=True, blank=True)
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.reviewID + ": " + self.title


#Media	mediaId	title	subtitle	authorId	type	location

class Media(models.Model):
	mediaID = models.CharField(max_length=256, null=True, blank=True)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256, null=True, blank=True)
	authorID = models.ForeignKey(Author, related_name='author_media')
	mediaType = models.CharField(max_length=256)
	location = models.CharField(max_length=256)
	timestamp = models.DateTimeField()
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.mediaID + ": " + self.title

#Tutorial	tutorialId	title	subtitle	authorId	body	productId

class Tutorial(models.Model):
	tutorialID = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256, null=True, blank=True)
	authorID = models.ForeignKey(Author, related_name='author_tutorial')
	body = models.TextField()
	timestamp = models.DateTimeField()
	def __unicode__(self):  # Python 3: def __str__(self):
        	return self.tutorialID + ": " + self.title

#FavoriteLink	authorID	title	description	URL

class FavoriteLink(models.Model):
	authorID = models.ForeignKey(Author, related_name='author_favoriteLink')
	title = models.CharField(max_length=256)
	description = models.TextField(null=True, blank=True)
	URL = models.CharField(max_length=256)
	def __unicode__(self):  # Python 3: def __str__(self):
        	return str(self.authorID) + ": " + self.title

#Bio	authorID	title	subtitle	body	hometown	hobbies

class Bio(models.Model):
	authorID = models.ForeignKey(Author, related_name='author_bio')
	title = models.CharField(max_length=256, null=True, blank=True)
	subtitle = models.CharField(max_length=256, null=True, blank=True)
	body = models.TextField()
	hometown = models.CharField(max_length=50)
	hobbies = models.TextField()
	def __unicode__(self):  # Python 3: def __str__(self):
        	return str(self.authorID) + ": " + self.title
