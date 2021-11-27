from django.http import HttpResponse
# Create your views here.


def hello_world_view(request):
    """ Simple hello_world view."""
    return HttpResponse("hello_world!")
