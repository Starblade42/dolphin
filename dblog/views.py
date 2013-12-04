from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from dblog.models import Author

def index(request):
    author_list = Author.objects.order_by('lastName')
    context = {'author_list': author_list}
    return render(request, 'dblog/index.html', context)

def detail(request, author_id):
	author = get_object_or_404(Author, pk=author_id)
	return render(request, 'dblog/detail.html', {'author': author})
