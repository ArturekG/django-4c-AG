from django.http import HttpResponse
from django.template import loader

def counter(request):
    template = loader.get_template('counter.html')
    context = {}
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))