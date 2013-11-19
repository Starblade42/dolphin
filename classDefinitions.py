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
	editor = models.ForeignKey(Author, blank=true)
	
#Article	articleId	title	subtitle	authorId	body	sources

class Updates(models.Model):
	articleId = models.CharField(max_length=140)
	title = models.Charfield(max_length=256)
	subtitle = models.Charfield(max_length=256)
	authorId = models.ForeignKey(Author)
	body = model.TextField()
	sources = models.TextField()

#Updates	authorID	articleID	timestamp
#This will create and Auto-Incrementing ID primary key!

class Updates(models.Model):
	authorID = models.ForeignKey(Author)
	articleID = models.ForeignKey(Article)
	timestamp = models.TimeField()



#Review	reviewId	title	subtitle	body	score	datePosted	productId

#Media	mediaId	title	subtitle	authorId	type	location

#Tutorial	tutorialId	title	subtitle	authorId	body	productId

#FavoriteLink	authorID	title	description	URL

#Bio	authorID	title	subtitle	body	hometown	hobbies