from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('')
    return HttpResponse("<h1>... Welcome To Music ...</h1>")

