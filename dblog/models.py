from django.db import models

#Authors	authorID	firstName	lastName
#This will create and Auto-Incrementing ID primary key!

class Author(models.Model):
	authorID = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	

#Blog	blogId	authorID	title	subtitle	editor
#This will create and Auto-Incrementing ID primary key!

class Blog(models.Model):
	blogId = models.CharField(max_length=50)
	authorID = models.ForeignKey(Author)
	title = models.CharField(max_length=120)
	subtitle = models.CharField(max_length=120)
	editor = models.ForeignKey(Author, blank=True)
	
#Article	articleId	title	subtitle	authorId	body	sources

class Article(models.Model):
	articleId = models.CharField(max_length=140)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256)
	authorId = models.ForeignKey(Author)
	body = models.TextField()
	sources = models.TextField()

#Updates	authorID	articleID	timestamp
#This will create and Auto-Incrementing ID primary key!

class Updates(models.Model):
	authorID = models.ForeignKey(Author)
	articleID = models.ForeignKey(Article)
	timestamp = models.TimeField()



#Review	reviewId	title	subtitle	body	score	datePosted	productId

class Review(models.Model):
	reviewId = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256)
	body = models.TextField()
	score = models.CharField(max_length=256)
	datePosted = models.DateField()
	productId = models.CharField(max_length=256)


#Media	mediaId	title	subtitle	authorId	type	location

class Media(models.Model):
	mediaId = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256)
	authorID = models.ForeignKey(Author)
	mediaType = models.CharField(max_length=256)
	location = models.CharField(max_length=256)

#Tutorial	tutorialId	title	subtitle	authorId	body	productId

class Tutorial(models.Model):
	tutorialId = models.CharField(max_length=256)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256)
	authorID = models.ForeignKey(Author)
	body = models.TextField()
	productId = models.CharField(max_length=256)

#FavoriteLink	authorID	title	description	URL

class FavoriteLink(models.Model):
	authorID = models.ForeignKey(Author)
	title = models.CharField(max_length=256)
	description = models.TextField()
	URL = models.CharField(max_length=256)

#Bio	authorID	title	subtitle	body	hometown	hobbies

class Bio(models.Model):
	authorID = models.ForeignKey(Author)
	title = models.CharField(max_length=256)
	subtitle = models.CharField(max_length=256)
	body = models.TextField()
	hometown = models.CharField(max_length=50)
	hobbies = models.TextField()
