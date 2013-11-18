from django.db import models

#Authors	authorID	firstName	lastName

class Author(models.Model):
	authorID = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	firstName = models.CharField(max_length=50)
	



#Blog	blogId	authorID	title	subtitle	editor

#Updates	authorID	articleId	timestamp

#Reviews	reviewId	title	subtitle	body	score	datePosted	productId

#Articles	articleId	title	subtitle	authorId	body	sources

#Media	mediaId	title	subtitle	authorId	type	location

#Tutorials	tutorialId	title	subtitle	authorId	body	productId

#FavoriteLink	authorID	title	description	URL

#Bio	authorID	title	subtitle	body	hometown	hobbies