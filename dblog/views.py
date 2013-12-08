from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from dblog.models import Author
from dblog.models import Blog

def index(request):
    author_list = Author.objects.order_by('lastName')
    context = {'author_list': author_list}
    return render(request, 'dblog/index.html', context)

def detail(request, author_ID):
	author = get_object_or_404(Author, authorID__exact=author_ID)
	blog_list = Blog.objects.order_by('title')
	return render(request, 'dblog/detail.html', {'author': author, 'blog_list': blog_list}) 

def blog(request, author_ID, blog_ID):
	author = get_object_or_404(Author, authorID__exact=author_ID)
	return render(request, 'dblog/blog.html', {'author': author})
