from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from dblog.models import Article
from dblog.models import Author
from dblog.models import Bio
from dblog.models import Blog
from dblog.models import FavoriteLink
from dblog.models import Media
from dblog.models import Review
from dblog.models import Tutorial
from dblog.models import Update

def index(request):
    author_list = Author.objects.order_by('lastName')
    context = {'author_list': author_list}
    return render(request, 'dblog/index.html', context)

def detail(request, author_ID):
	author = get_object_or_404(Author, authorID__exact=author_ID)
	blog_list = Blog.objects.order_by('title')
	link_list = FavoriteLink.objsects.order_by('authorID')
	bio_list = Bio.objects.order_by('authorID')
	return render(request, 'dblog/detail.html', {'author': author, 'blog_list': blog_list, 'link_list': link_list, 'bio_list': bio_list}) 

def blog(request, author_ID, blog_ID):
        author = get_object_or_404(Author, authorID__exact=author_ID)
	blog = get_object_or_404(Blog, blogID__exact=blog_ID)
        return render(request, 'dblog/blog.html', {'author': author})
