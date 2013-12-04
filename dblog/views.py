from django.http import HttpResponse
from django.template import RequestContext, loader

from dblog.models import Author

def index(request):
    author_list = Author.objects.order_by('lastName')
    template = loader.get_template('dblog/index.html')
    context = RequestContext(request, {
        'author_list': author_list,
    })
    return HttpResponse(template.render(context))
