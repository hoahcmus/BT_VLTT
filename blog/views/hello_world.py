from django.http import HttpResponse
# Create your views here.


def index(request):
    """ Simple hello_world view."""
    return HttpResponse("hello_world!")
